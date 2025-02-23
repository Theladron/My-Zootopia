import requests

API_KEY = "W2lsKCIZ613ogZrhdObafg==GDrSg3BXhnOk2y5e"


def load_data(user_input):
    """Loads a JSON file"""
    response = requests.get("https://api.api-ninjas.com/v1/animals?name=" + user_input, headers={"X-Api-Key": API_KEY})
    data = response.json()
    return data


def replace_html(animal_data):
    """
    replaces filler data from a specific given html
    file with the created animal data
    :param animal_data: created html code as str
    :return: complete html site code as str
    """
    with open("animals_template.html", "r") as handle:
        data = handle.read()

    new_data = data.replace("__REPLACE_ANIMALS_INFO__", animal_data)
    return new_data


def write_new_html(data):
    """
    creates/writes a html file with the data
    :param data: html code as str
    """
    with open("animals.html", "w") as handle:
        handle.write(data)


def serialize_animal(entry):
    """
    creates html string with the different found
    entries
    :param entry: dict
    :return: corrected html as str
    """
    output = ""
    output += '<li class="cards__item">\n'

    name = get_animal_name(entry)
    if name:
        output += f'  <div class="card__title">{name}</div>\n'

    output += '  <div class="card__text">\n'
    output += "    <ul>\n"

    diet = get_animal_diet(entry)
    if diet:
        output += f"      <li><strong>Diet:</strong> {diet}</li>\n"

    location = get_animal_location(entry)
    if location:
        output += f"      <li><strong>Location:</strong> {location[0]}</li>\n"

    animal_type = get_animal_type(entry)
    if animal_type:
        output += f"      <li><strong>Type:</strong> {animal_type}</li>\n"

    prey = get_animal_prey(entry)
    if prey:
        output += f"      <li><strong>Prey:</strong> {prey}</li>\n"

    output += "    </ul>\n  </div>\n</li>\n"

    return output.replace("â€™s ", "&#x27;S ")  # corrects the formatting error happening for ' symbol


def get_animal_name(entry):
    """
    gets the value from the entry 'name',
    {} if not found
    :param entry: dict
    :return: value as str, {} if not found
    """
    return entry.get("name", {})


def get_animal_diet(entry):
    """
    gets the value from the entry diet',
    {} if not found
    :param entry: dict
    :return: value as str, {} if not found
    """
    return entry.get("characteristics", {}).get("diet")


def get_animal_location(entry):
    """
    gets the first value from the 'location' list,
    None if not found
    :param entry: dict
    :return: value as str, None if not found
    """
    return entry.get("locations", [None])


def get_animal_type(entry):
    """
    gets the value from the entry 'type',
    {} if not found
    :param entry: dict
    :return: value as str, {} if not found
    """
    return entry.get("characteristics", {}).get("type")


def get_animal_prey(entry):
    """
    gets the value from the entry 'prey',
    {} if not found
    :param entry: dict
    :return: value as str, {} if not found
    """
    return entry.get("characteristics", {}).get("prey")


def create_animal_html(data, user_input):
    """
    loops through the json file, checks if skin type is matched,
    gets animal data, informs user if no matching data found
    :param user_input: input as str
    :return: html created as str
    """
    output = ""

    for animal_obj in data:
        output += serialize_animal(animal_obj)

    if output == "":
        return (f'<div class="card__title">No animals found for '
                f'your search of "{user_input}".')
    return output


def get_user_input():
    """
    gets input from the user
    :return: input as str
    """
    print("""Enter the name of an animal: """, end="")
    user_input = input("")
    return user_input


def main():
    """calls for user_input and html site creation"""
    user_input = get_user_input()
    data = load_data(user_input)
    output = create_animal_html(data, user_input)
    new_data = replace_html(output)
    write_new_html(new_data)


if __name__ == "__main__":
    main()

import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def replace_html(animal_data):

    with open("animals_template.html", "r") as handle:
        data = handle.read()

    new_data = data.replace("            __REPLACE_ANIMALS_INFO__", animal_data)
    return new_data


def write_new_html(data):

    with open("animals.html", "w") as handle:
        handle.write(data)


def serialize_animal(entry):

    output = ""
    output += '<li class="cards__item">\n'

    name = get_animal_name(entry)
    if name is not None:
        output += f'  <div class="card__title">{name}</div>\n'

    output += '  <div class="card__text">\n'
    output += "    <ul>\n"

    diet = get_animal_diet(entry)
    if diet is not None:
        output += f"      <li><strong>Diet:</strong> {diet}</li>\n"

    location = get_animal_location(entry)
    if location is not None:
        output += f"      <li><strong>Location:</strong> {location}</li>\n"

    animal_type = get_animal_type(entry)
    if animal_type is not None:
        output += f"      <li><strong>Type:</strong> {animal_type}</li>\n"

    prey = get_animal_prey(entry)
    if prey is not None:
        output += f"      <li><strong>Prey:</strong> {prey}</li>\n"

    output += "    </ul>\n  </div>\n</li>\n"

    return output.replace("â€™s ", "&#x27;S ")  # corrects the formatting error happening for ' symbol


def get_animal_name(entry):

    return entry.get("name", {})


def get_animal_diet(entry):

    return entry.get("characteristics", {}).get("diet")


def get_animal_location(entry):

    return entry.get("locations", [None])[0]


def get_animal_type(entry):

    return entry.get("characteristics", {}).get("type")


def get_animal_prey(entry):

    return entry.get("characteristics", {}).get("prey")


def create_animal_html(user_input):

    data = load_data("animals_data.json")
    output = ""

    for animal_obj in data:
        skin_type = animal_obj.get("characteristics", {}).get("skin_type")
        if user_input.lower() in skin_type.lower():
            output += serialize_animal(animal_obj)

    if output == "":
        return (f'<div class="card__title">No Animals with '
                f'skin type "{user_input}" found</div>')
    return output


def get_user_input():

    print("""Possible skin types:
Hair
Fur
Scales
All   for every animal

Enter the skin type of the animals you want to see: """, end="")
    user_input = input("")
    return user_input


def main():

    user_input = get_user_input()
    output = create_animal_html(user_input)
    new_data = replace_html(output)
    write_new_html(new_data)


if __name__ == "__main__":
    main()

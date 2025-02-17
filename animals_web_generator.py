import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def replace_data(animal_data):
    with open("animals_template.html", "r") as handle:
        data = handle.read()

    new_data = data.replace("            __REPLACE_ANIMALS_INFO__", animal_data)
    return new_data


def write_html(data):
    with open("animals.html", "w") as handle:
        handle.write(data)


def get_animals_data():
    data = load_data("animals_data.json")
    output = ""
    for entry in data:
        output += '<li class="cards__item">'
        name = get_animal_name(entry)
        if name is not None:
            output += f"Name: {name}\n<br/>"

        diet = get_animal_diet(entry)
        if diet is not None:
            output += f"Diet: {diet}\n<br/>"

        location = get_animal_location(entry)
        if location is not None:
            output += f"Location: {location}\n<br/>"

        animal_type = get_animal_type(entry)
        if animal_type is not None:
            output += f"Type: {animal_type}\n<br/>"

        output += "</li>"

    return output


def get_animal_name(entry):
    return entry.get("name", {})


def get_animal_diet(entry):
    return entry.get("characteristics", {}).get("diet")


def get_animal_location(entry):
    return entry.get("locations", [None])[0]


def get_animal_type(entry):
    return entry.get("characteristics", {}).get("type")


def main():
    animal_data = get_animals_data()
    new_data = replace_data(animal_data)
    write_html(new_data)


if __name__ == "__main__":
    main()

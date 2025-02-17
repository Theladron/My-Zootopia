import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_animals():
    data = load_data("animals_data.json")
    for entry in data:
        name = get_animal_name(entry)
        if name is not None:
            print(name)

        diet = get_animal_diet(entry)
        if diet is not None:
            print(diet)

        location = get_animal_location(entry)
        if location is not None:
            print(location)

        animal_type = get_animal_type(entry)
        if animal_type is not None:
            print(animal_type)

        print()


def get_animal_name(entry):
    return entry.get("name", {})


def get_animal_diet(entry):
    return entry.get("characteristics", {}).get("diet")


def get_animal_location(entry):
    return entry.get("locations", [None])[0]


def get_animal_type(entry):
    return entry.get("characteristics", {}).get("type")


def main():
    print_animals()


if __name__ == "__main__":
    main()

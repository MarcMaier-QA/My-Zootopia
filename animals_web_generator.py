import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data("animals_data.json")


for animal in animals_data:
    print(f"Name: {animal.get('name')}")
    print(f"Diet: {animal.get('diet')}")


locations = animal.get('locations')
if locations:
    print(f"Locations: {locations[0]}")

animal_type = animal.get('type')
if animal_type:
    print(f"Type: {animal_type}")

print("-" * 20)

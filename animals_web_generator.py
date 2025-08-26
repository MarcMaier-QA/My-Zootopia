import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

# Loads data from JSON file
animals_data = load_data("animals_data.json")

# Iterate through the list of animals and print the information
for animal in animals_data:
    print(f"Name: {animal.get('name')}")
    print(f"Diet: {animal.get('diet')}")

    # Check if 'location' exists and is not empty
    locations = animal.get('locations')
    if locations:
        print(f"Locations: {locations[0]}")

    # Check if 'type' exists
    animal_type = animal.get('type')
    if animal_type:
        print(f"Type: {animal_type}")

print("-" * 20) # Seperator for better readability

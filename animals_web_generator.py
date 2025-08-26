import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

# Loads data from JSON file
animals_data = load_data("animals_data.json")

# 1. Read the HTML templates content
with open("animals_template.html", "r") as handle:
    html_template = handle.read()

# 2. Generate a string with the animal data
animals_info_string = ""
for animal in animals_data:
    animals_info_string += f"Name: {animal.get('name')}\n"
    animals_info_string += f"Diet: {animal.get('diet')}\n"

    # Check if 'location' exists and is not empty
    locations = animal.get('locations')
    if locations:
        animals_info_string += f"Locations: {locations[0]}\n"

    # Check if 'type' exists
    animal_type = animal.get('type')
    if animal_type:
        animals_info_string += "Type: {animal_type}\n"

    animals_info_string += "\n"  # Add an extra newline for separation

# 3. Replace the placeholder with the generated string
final_html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info_string)

# 4. Write the new HTML content to a file
with open("animals.html", "w") as handle:
    handle.write(final_html_content)

print("animals.html has been generated successfully")

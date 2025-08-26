import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


# Load data from the JSON file
animals_data = load_data('animals_data.json')

# Read the HTML template content
with open("animals_template.html", "r") as handle:
    html_template = handle.read()

# Generate a string with the animal data, now as HTML list items
animals_info_string = ""
for animal in animals_data:
    # Start of the list item with the CSS class
    animals_info_string += '<li class="cards__item">'

    # Add each piece of animal data with a <br/> for a line break
    animals_info_string += f"Name: {animal.get('name')}<br/>\n"
    animals_info_string += f"Diet: {animal.get('diet')}<br/>\n"

    locations = animal.get('locations')
    if locations:
        animals_info_string += f"Location: {locations[0]}<br/>\n"

    animal_type = animal.get('type')
    if animal_type:
        animals_info_string += f"Type: {animal_type}<br/>\n"

    # End the list item
    animals_info_string += "</li>\n"

# Replace the placeholder with the generated string
final_html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info_string)

# Write the new HTML content to the animals.html file
with open("animals.html", "w") as handle:
    handle.write(final_html_content)

print("animals.html has been generated successfully!")
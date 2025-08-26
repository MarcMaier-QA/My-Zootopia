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

# Generate a string with the animal data, now with a better HTML structure
animals_info_string = ""
for animal in animals_data:
    # Start of the list item with the CSS class
    animals_info_string += '<li class="cards__item">\n'

    # Add the animal's name as a title
    animals_info_string += f'  <div class="card__title">{animal.get("name")}</div>\n'
    animals_info_string += '  <p class="card__text">\n'

    # Add the diet with a bold label
    animals_info_string += f'      <strong>Diet:</strong> {animal.get("diet")}<br/>\n'

    # Check and add locations if they exist
    locations = animal.get('locations')
    if locations:
        animals_info_string += f'      <strong>Location:</strong> {locations[0]}<br/>\n'

    # Check and add type if it exists
    animal_type = animal.get('type')
    if animal_type:
        animals_info_string += f'      <strong>Type:</strong> {animal_type}<br/>\n'

    # End the text block and the list item
    animals_info_string += '  </p>\n'
    animals_info_string += "</li>\n"

# Replace the placeholder with the generated string
final_html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info_string)

# Write the new HTML content to the animals.html file
with open("animals.html", "w") as handle:
    handle.write(final_html_content)

print("animals.html has been generated successfully with improved formatting!")
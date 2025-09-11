import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """
    Serializes a single animal object into an HTML string.
    """
    html_string = '<li class="cards__item">\n'
    html_string += f'  <div class="card__title">{animal.get("name")}</div>\n'
    html_string += '  <p class="card__text">\n'

    characteristics = animal.get("characteristics", {})

    diet = characteristics.get("diet")
    if diet:
        html_string += f'      <strong>Diet:</strong> {diet}<br/>\n'

    locations = animal.get('locations')
    if locations:
        html_string += f'      <strong>Location:</strong> {locations[0]}<br/>\n'

    animal_type = characteristics.get('type')
    if animal_type:
        html_string += f'      <strong>Type:</strong> {animal_type}<br/>\n'

    html_string += '  </p>\n'
    html_string += '</li>\n'

    return html_string


# --- Main script logic ---

# Load data from the JSON file
animals_data = load_data('animals_data.json')

# Read the HTML template content
with open("animals_template.html", "r") as handle:
    html_template = handle.read()

# Generate a string with the animal data by iterating and calling the new function
animals_info_string = ""
for animal in animals_data:
    animals_info_string += serialize_animal(animal)

# Replace the placeholder with the generated string
final_html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info_string)

# Write the new HTML content to the animals.html file
with open("animals.html", "w") as handle:
    handle.write(final_html_content)

print("animals.html has been generated successfully and code is now formatted!")
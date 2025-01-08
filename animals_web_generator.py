import json


def load_file(file_path):
    """Loads a file and returns its content."""
    with open(file_path, "r") as file:
        return file.read()


def save_file(file_path, content):
    """Saves content to a file."""
    with open(file_path, "w") as file:
        file.write(content)


#file paths
data_file = 'animals_data.json'  #JSON file with animal data
template_file = 'animals_template.html'  #HTML template file
output_file = 'animals.html'  #output the HTML file

try:
    #1:read JSON data
    with open(data_file, "r") as file:
        data = json.load(file)

    #2:read the HTML template
    template = load_file(template_file)

    #3:generate animals data string
    animals_output = ""
    for animal_data in data:
        animals_output += f"<li>\n"
        animals_output += f"  <strong>Name:</strong> {animal_data.get('name', 'N/A')}<br>\n"
        animals_output += f"  <strong>Diet:</strong> {animal_data.get('characteristics', {}).get('diet', 'N/A')}<br>\n"
        locations = animal_data.get('locations', [])
        location = locations[0] if locations else "N/A"
        animals_output += f"  <strong>Location:</strong> {location}<br>\n"
        animals_output += f"  <strong>Type:</strong> {animal_data.get('type', 'N/A')}<br>\n"
        animals_output += f"</li>\n\n"

    #4:replace the placeholder with the animals' data
    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_output)

    #5:write the final HTML to a new file
    save_file(output_file, final_html)
    print(f"HTML file generated successfully: {output_file}")

except FileNotFoundError as e:
    print(f"Error: {e}")
except json.JSONDecodeError:
    print("Error: Invalid JSON format in animals_data.json.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
output_file = 'animals.html'  #output HTML file
save_file(output_file, final_html)
print(f"File saved to: {output_file}")




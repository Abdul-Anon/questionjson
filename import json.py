import json
import docx

# Open the .docx file
document = docx.Document('document.docx')

# Extract the lines from the document
lines = []
for paragraph in document.paragraphs:
    lines.append(paragraph.text)

# Convert the lines to a JSON object
json_data = json.dumps(lines)

# Write the JSON object to a file
with open('document.json', 'w') as f:
    f.write(json_data)
import json
from docx import Document
from tkinter import *

# Open the Word document
document = Document("document.docx")

# Create an empty dictionary to store the data
data = {}

# Iterate over the paragraphs in the document
for paragraph in document.paragraphs:
  # Get the text of the paragraph
  text = paragraph.text
  # Split the text into lines
  lines = text.split("\n")
  # Iterate over the lines
  for line in lines:
    # Split the line into key and value
    key, value = line.split(": ")
    # Store the key and value in the data dictionary
    data[key] = value

# Convert the data dictionary to a JSON string
json_data = json.dumps(data)

# Write the JSON string to a file
with open("data.json", "w") as f:
  f.write(json_data)
import json

# Provide the correct path to the JSON file
json_file_path = 'Server\events.json'

# Read the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Extract events from the JSON data
events = data['events']

# Print each event title in a new line
for event in events:
    print(event['title'])

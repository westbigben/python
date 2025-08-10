# Demonstrate saving and loading data using JSON

import json

data = {
    "name": "Alice",
    "age": 30
}

# Save data to JSON file
with open("data.json", "w") as f:
    json.dump(data, f)

# Load data back from JSON file
with open("data.json", "r") as f:
    loaded = json.load(f)

print("Loaded data:", loaded)


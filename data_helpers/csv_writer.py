import json
import csv

# Step 1: Import the necessary modules

# Step 2: Open and parse the JSON file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Step 3: Create or open a CSV file and set up a csv.DictWriter object
with open('data.csv', 'w', newline='') as csv_file:
    # Define the CSV headers based on the JSON keys
    fieldnames = list(data[0].keys())
    
    # Create a DictWriter object
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # Write the CSV headers
    csv_writer.writeheader()
    
    # Step 4: Write the JSON data to the CSV file
    for row in data:
        csv_writer.writerow(row)

print("CSV file has been created successfully.")

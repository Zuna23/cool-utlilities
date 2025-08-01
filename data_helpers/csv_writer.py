import json
import csv
from pathlib import Path

def json_to_csv(json_path, csv_path):
    with open(json_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    if not data:
        raise ValueError("JSON file is empty.")

    fieldnames = list(data[0].keys())

    with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"CSV file '{csv_path}' has been created successfully.")

if __name__ == "__main__":
    json_file = Path('data.json')
    csv_file = Path('data.csv')
    json_to_csv(json_file, csv_file)

import csv
import json

print("Step 1: Creating a random CSV file.")

csv_data = [
    ["name", "age", "city"],
    ["Prashant Joshi", "17", "Mahendranagar"],
    ["Pranish Joshi", "9", "Kathmandu"],
    ["Padam Raj Joshi", "46", "Dadeldhura"],
    ["Shanti Bhatta Joshi", "35", "Dadeldhura"]
]

with open("people.csv", "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

print("Created people.csv")

print("Step 2: Reading the CSV file.")

people_list = []

with open("people.csv", "r") as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        print(f"Read: {row}")
        people_list.append(row)

print(f"Read {len(people_list)} people from CSV.")

print("\nStep 3: Writing to JSON file...")

with open("people.json", "w") as file:
    json.dump(people_list, file, indent = 4)

print("Created people.json")

print("\nStep 4: Let's check the JSON file...")

with open("people.json", "r") as file:
    data = json.load(file)
    print("JSON content: ")
    for person in data:
        print(f" {person}")

def convert_csv_to_json(csv_filename, json_filename):
    data = []
    with open(csv_filename, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)

    with open(json_filename, "w") as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Converted {csv_filename} to {json_filename}")
    print(f"Total records: {len(data)}")

print("\n" + "=" * 50)
print("Testing our converter function:")
convert_csv_to_json("people.csv", "people_output.json")


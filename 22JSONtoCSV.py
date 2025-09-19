import json
import csv

print("Step 1: Creating a random JSON file.")

json_data = [
    {"name" : "Prashant Joshi", "age" : "17", "city" : "Mahendranagar"},
    {"name" : "Pranish Joshi", "age" : "9", "city" : "Kathmandu"},
    {"name" : "Padam Raj Joshi", "age" : "46", "city" : "Dadeldhura"},
    {"name" : "Trilok Joshi", "age" : "9", "city" : "Kathmandu"}
]

with open("family.json","w") as file:
    json.dump(json_data, file, indent = 4)

print("Created family.json")

print("Step 2: Reading the JSON file")

family_list = []

with open("family.json", "r") as file:
    json_data = json.load(file)

    for row in json_data:
        print(f"Read: {row}")
        family_list.append(row)

print(f"Read {len(family_list)} family from the JSON file.")

print("\nStep 3: Writing to CSV file...")

with open("family.csv", "w", newline ="") as file:
    headers = family_list[0].keys()
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(family_list)

print("Created family.csv")
print("\nStep 4: Let's check the CSV file...")

with open("family.csv","r") as file:
    csv_reader = csv.DictReader(file)
    print("CSV content: ")
    for person in csv_reader:
        print(f" {person}")

def convert_json_to_csv(json_filename, csv_filename):
    data = []
    with open(json_filename, "r") as json_file:
        data = json.load(json_file)

    with open(csv_filename, "w", newline = "") as csv_file:
        if data:
            headers = data[0].keys()
            writer = csv.DictWriter(csv_file, fieldnames = headers)
            writer.writeheader()
            writer.writerows(data)

    print(f"Converted {json_filename} to {csv_filename} successfully.")
    print(f"Total Records: {len(data)}")

print("\n" + "=" * 50)
print("Testing our converter function: ")
convert_json_to_csv("family.json", "family.csv")
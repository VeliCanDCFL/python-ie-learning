#open("output.txt", "w") → open file for writing. Creates it if it doesn't exist.
#open("output.txt", "r")
#"w" means write mode
#"r" means read mode
#\n → new line character
#with → context manager, automatically closes the file when done even if an error happens.
# Always use with instead of manually calling f.close()
#"a" mode adds to the existing file, doesn't overwrite it
#"w" mode would wipe everything and start fresh
#Looping over f reads one line at a time
#.strip() cleans the trailing \n from each line
# Writing to a file
with open("output.txt", "w") as f:
    f.write("Production Log\n")
    f.write("Date: 2024-01-15\n")
    f.write("Shift: Morning\n")
    f.write("Units produced: 450\n")

print("File written successfully")

# Reading from a file
with open("output.txt", "r") as f:
    content = f.read()
    print(content)

print("-"*20)

# Append mode — adds to file without deleting existing content
with open("output.txt", "a") as f:
    f.write("Units produced: 380\n")
    f.write("Shift: Evening\n")

# Reading line by line
with open("output.txt", "r") as f:
    for line in f:
        print(line.strip())   # .strip() removes the \n at the end of each line

print("-"*40)

import csv

# Writing a CSV file
workers = [
    ["Name", "Department", "Shift", "Units"],
    ["Ali", "Production", "Morning", 120],
    ["Sara", "Quality", "Morning", 95],
    ["John", "Logistics", "Evening", 110],
    ["Lena", "Production", "Evening", 130],
]

with open("workers.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(workers)

print("CSV written successfully")

# Reading a CSV file
with open("workers.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("-"*40)

# Writing CSV with DictWriter
workers_dict = [
    {"Name": "Ali", "Department": "Production", "Shift": "Morning", "Units": 120},
    {"Name": "Sara", "Department": "Quality", "Shift": "Morning", "Units": 95},
    {"Name": "John", "Department": "Logistics", "Shift": "Evening", "Units": 110},
    {"Name": "Lena", "Department": "Production", "Shift": "Evening", "Units": 130},
]

with open("workers2.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "Department", "Shift", "Units"])
    writer.writeheader()
    writer.writerows(workers_dict)

print("Dict CSV written successfully")

# Reading CSV with DictReader
with open("workers2.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']} from {row['Department']} produced {int(row['Units'])} units")

print("-"*40)

import json

# Writing JSON
factory_data = {
    "factory_name": "Istanbul Plant",
    "capacity": 5000,
    "departments": ["Production", "Quality", "Logistics"],
    "machines": [
        {"id": "M001", "type": "CNC", "speed": 1500},
        {"id": "M002", "type": "Conveyor", "speed": 300},
        {"id": "M003", "type": "Robotic Arm", "speed": 800},
    ]
}

with open("factory.json", "w") as f:
    json.dump(factory_data, f, indent=4)

print("JSON written successfully")

# Reading JSON
with open("factory.json", "r") as f:
    data = json.load(f)

print(f"Factory: {data['factory_name']}")
print(f"Capacity: {data['capacity']}")
print(f"Departments: {', '.join(data['departments'])}")
print("\nMachines:")
for machine in data['machines']:
    print(f"  {machine['id']} | {machine['type']} | Speed: {machine['speed']}")

print("-"*40)


from dataclasses import dataclass, asdict
import json

@dataclass
class WorkOrder:
    order_id: str
    product: str
    quantity: int
    priority: str = "normal"
    completed: bool = False

    def complete(self):
        self.completed = True


# Create some work orders
orders = [
    WorkOrder("WO001", "Steel Bolt", 500, "high"),
    WorkOrder("WO002", "Aluminum Plate", 200),
    WorkOrder("WO003", "Titanium Rod", 50, "urgent"),
]

orders[0].complete()

# Save to JSON
with open("work_orders.json", "w") as f:
    json.dump([asdict(o) for o in orders], f, indent=4)

print("Work orders saved")

# Load from JSON
with open("work_orders.json", "r") as f:
    loaded = json.load(f)

print("\nLoaded work orders:")
for o in loaded:
    status = "✓" if o['completed'] else "pending"
    print(f"[{status}] {o['order_id']} | {o['product']} x{o['quantity']} | {o['priority']}")
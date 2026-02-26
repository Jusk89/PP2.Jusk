import json

# Open JSON file
with open("sample-data.json") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("{:<50} {:<15} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

# Navigate through JSON structure
interfaces = data["imdata"]

for item in interfaces:
    attributes = item["l1PhysIf"]["attributes"]

    dn = attributes["dn"]
    descr = attributes["descr"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    print("{:<50} {:<15} {:<10} {:<10}".format(dn, descr, speed, mtu))
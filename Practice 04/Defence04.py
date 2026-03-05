import json
import math

with open("courses.json") as file:
    data = json.load(file)


Circle = data["Circle"]

Radius= Circle["radius"]
print(math.pi*Radius**2)
import json
import os
import string

#Open file, parse, and store as dictionary:

minerals = json.loads(open('minerals.json').read())
print("successful so far! About to go into for loop")

from models import Mineral

for mineral in minerals:
    print(mineral['name'])
    minEntry = Mineral(name=mineral['name']).save()
    print("mineral has been added to database!")


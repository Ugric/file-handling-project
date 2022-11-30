from faker import Faker
import json
import random

fake = Faker()
output = {}
for i in range(1000):
  output[fake.name()] = ([random.randint(0, 100) for _ in range(10)])
json.dump((output),
          open("data.txt", "w"),
          sort_keys=True,
          indent=4,
          separators=(',', ': '))

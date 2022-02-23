#!/usr/bin/python
from datetime import date
import json

with open("output.json", "r", encoding='ISO-8859-9') as read_file:
    data = json.load(read_file)

for k,v in data.items():
    print(v[''])
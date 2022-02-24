#!/usr/bin/python
from datetime import date
import json

with open("output.json", "r", encoding='utf-8-sig') as read_file:
    data = json.load(read_file)


for k,v in data.items():
    print(v['Sertifika İsmi'],':', v['Geçerlilik Bitiş Tarihi'])
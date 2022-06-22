#!/usr/bin/python
from datetime import date, datetime
import json

with open("output.json", "r", encoding='utf-8-sig') as read_file:
    data = json.load(read_file)


for k,v in data.items():
    #print((datetime.now() - datetime.strptime(v['Geçerlilik Bitiş Tarihi'], '%d.%m.%Y')).days)
    print(v['Sertifika İsmi'],':', v['Geçerlilik Bitiş Tarihi'], (datetime.strptime(v['Geçerlilik Bitiş Tarihi'], '%d.%m.%Y') - datetime.now()).days)
#!/usr/bin/python
from datetime import datetime
import json
import configparser
from pyzabbix import ZabbixMetric, ZabbixSender
import re

config   = configparser.ConfigParser()
config.read('config.txt')
zabbix_server   = config.get('zabbix', 'server')
zabbix_port     = config.get('zabbix', 'port')
zabbix_host     = config.get('zabbix', 'host')

with open("output.json", "r", encoding='utf-8-sig') as read_file:
    data = json.load(read_file)

def clean(varStr): return re.sub('\W+|^(?=\d)','_', varStr)
tr2eng = str.maketrans('çÇğĞıİöÖşŞüÜ', 'cCgGiIoOsSuU')




for k,v in data.items():
    #print((datetime.now() - datetime.strptime(v['Geçerlilik Bitiş Tarihi'], '%d.%m.%Y')).days)
    if (datetime.strptime(v['Geçerlilik Bitiş Tarihi'], '%d.%m.%Y') - datetime.now()).days >= 0:
        value = (datetime.strptime(v['Geçerlilik Bitiş Tarihi'], '%d.%m.%Y') - datetime.now()).days
    else:
        value = 0
    print(value)
    key = (clean(v['Sertifika İsmi'])).translate(tr2eng)
    packet = [ZabbixMetric(zabbix_host, key, value)]
    result = ZabbixSender(zabbix_server, int(zabbix_port), use_config=None).send(packet)
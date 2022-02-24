#!/usr/bin/python
import configparser
import logging
import sys
from pyzabbix import ZabbixAPI, ZabbixAPIException
import json
import re

config          = configparser.ConfigParser()
config.read('config.txt')
zabbix_server           = config.get('zabbix', 'server')
zabbix_port             = config.get('zabbix', 'port')
zabbix_username         = config.get('zabbix', 'user')
zabbix_password         = config.get('zabbix', 'pass')
zabbix_hostname         = config.get('zabbix', 'host')

zapi = ZabbixAPI(url=zabbix_server, user=zabbix_username, password=zabbix_password)

hosts = zapi.host.get(filter={"host": zabbix_hostname})

with open("output.json", "r", encoding='utf-8-sig') as read_file:
    data = json.load(read_file)


def clean(varStr): return re.sub('\W+|^(?=\d)','_', varStr)
tr2eng = str.maketrans('çÇğĞıİöÖşŞüÜ', 'cCgGiIoOsSuU')

if hosts:
    host_id = hosts[0]["hostid"]
    print("Found host id {0}".format(host_id))

    for k,v in data.items():
        try:
            item = zapi.item.create(
                hostid=host_id,
                name=(clean(v['Sertifika İsmi'])).translate(tr2eng),
                key_=(clean(v['Sertifika İsmi'])).translate(tr2eng),
                type=2,
                value_type=4,
                delay=10
            )
        except ZabbixAPIException as e:
            print(e)
            sys.exit()
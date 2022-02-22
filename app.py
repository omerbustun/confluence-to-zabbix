#!/usr/bin/python
import configparser
import logging
import sys
from pyzabbix import ZabbixAPI, ZabbixAPIException

config          = configparser.ConfigParser()
config.read('config.txt')
zabbix_server           = config.get('zabbix', 'server')
zabbix_port             = config.get('zabbix', 'port')
zabbix_username         = config.get('zabbix', 'user')
zabbix_password         = config.get('zabbix', 'pass')
zabbix_hostname         = config.get('zabbix', 'host')

zapi = ZabbixAPI(url=zabbix_server, user=zabbix_username, password=zabbix_password)

hosts = zapi.host.get(filter={"host": zabbix_hostname})
if hosts:
    host_id = hosts[0]["hostid"]
    print("Found host id {0}".format(host_id))

    try:
        item = zapi.item.create(
            hostid=host_id,
            name='test',
            key_='test',
            type=2,
            value_type=4,
            delay=10
        )
    except ZabbixAPIException as e:
        print(e)
        sys.exit()
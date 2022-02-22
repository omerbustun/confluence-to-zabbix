![GitHub last commit](https://img.shields.io/github/last-commit/omerbustun/confluence-to-zabbix?logo=Github)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/omerbustun/confluence-to-zabbix?logo=Github)
![GitHub Repo stars](https://img.shields.io/github/stars/omerbustun/confluence-to-zabbix?style=social)
# confluence-to-zabbix
Tool for parsing and piping e-mail alerts to Zabbix.

## Usage

Create a config.txt file in the main directory and populate it with the parameters below.

```
[zabbix]
server = <zabbix-server>
port = <port> #10051 by default
user = <zabbix-user>
pass = <password>
```
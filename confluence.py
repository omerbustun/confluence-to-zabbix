#!/usr/bin/python
from atlassian import Confluence
import pandas as pd
import configparser

config          = configparser.ConfigParser()
config.read('config.txt')
conf_server           = config.get('confluence', 'server')
conf_username         = config.get('confluence', 'user')
conf_password         = config.get('confluence', 'pass')


#!/usr/bin/python
from atlassian import Confluence
import pandas as pd
import configparser
import csv
import json

config = configparser.ConfigParser()
config.read('config.txt')

conf_server           = config.get('confluence', 'server')
conf_username         = config.get('confluence', 'user')
conf_password         = config.get('confluence', 'pass')
page_title            = config.get('confluence', 'page_title')
page_space            = config.get('confluence', 'page_space')
page_id               = config.get('confluence', 'page_id')

# connect to Confluence
conf = Confluence(url=conf_server, username=conf_username, password=conf_password)

# get current page content
page = conf.get_page_by_id(page_id, expand='body.view')
page_content = page['body']['view']['value']

#get table
table = pd.read_html(page_content)
table = table[0] #Only one table on the page

#convert table to HTML
json_export = table.to_csv('data.csv')

with open('data.json', 'w') as f:
    json.dump(json_export, f)
def make_json(csv_file, json_file):
    data = {}

    with open(csv_file, encoding='ISO-8859-9') as csvf:
        csv_reader = csv.DictReader(csvf)
        for rows in csv_reader:
            key = rows['']
            data[key] = rows
    
    with open(json_file, 'w', encoding='ISO-8859-9') as jsonf:
        jsonf.write(json.dumps(data, indent=4, ensure_ascii=False, sort_keys=False))


csv_file = 'data.csv'
json_file = 'output.json'

#def make_json(csv_file, json_file):
#    csvfile_ind = open(csv_file,'r', encoding='ISO-8859-9')
#    reader_ind = csv.DictReader(csvfile_ind)
#    json_file_ind = open(json_file, 'w', encoding='ISO-8859-9')
#    for row in reader_ind:
#        json_file_ind.write(json.dumps(row,sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False))


make_json(csv_file, json_file)
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson
data = readfromjson("results.json")
xml = json2xml.Json2xml(data).to_xml()
print(xml)

with open('results.xml', 'w') as xmlFile:
    xmlFile.write(xml)
    xmlFile.close()



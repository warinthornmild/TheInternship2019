import xml.etree.ElementTree as ET
import json

def xml_to_dict(root, data) :

    if root.text!=None and len(root.text.strip())!=0 : 
        data[root.tag] = root.text
        return data

    attr = {}
    for k,v in root.attrib.items() : 
        attr[k] = v
    data[root.tag] = attr

    if len(list(root.iter('*')))>1 : 
        for c in root :
            data[root.tag] = xml_to_dict(c, data[root.tag])
        return data

    return data
 
tree = ET.parse('weather.xml')
root = tree.getroot()
data = xml_to_dict(root, dict())[root.tag]

with open('weather.json', 'w') as f:
  json.dump(data, f, ensure_ascii=False)

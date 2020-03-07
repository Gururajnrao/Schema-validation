# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 13:47:17 2020

@author: Gururaj
"""
import jsonschema
import simplejson as json
import yaml
with open(r'spec.yaml') as file:
    hub_spec=yaml.load(file,Loader=yaml.FullLoader)   
"""
    for key, value in hub_spec.items():
        print(key,":",value)
"""
with open ('schema_validate.json', 'r') as f:
    schema_data=f.read()
schema=json.loads(schema_data)
try:
  jsonschema.validate(hub_spec, schema)
except:
   print ("Schema validation failed") 
import json
from pprint import pprint

data = {}
with open('inputjson.json') as f:
    data = json.load(f)

for key in data:
	print('%s:%s'%(key,data[key]))

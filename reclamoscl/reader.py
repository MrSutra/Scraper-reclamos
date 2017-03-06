import json
from pprint import pprint

with open('reclamos.json') as data_file:    
    data = json.load(data_file)

#pprint(data)
print(data[0]["complaint"])
archivo = open("asd.txt",'w')
archivo.write(data[0]["complaint"].encode('utf-8'))
archivo.close()
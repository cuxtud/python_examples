import requests
import json
from morpheuscypher import Cypher
import os
import sys
from pprint import pprint
c = Cypher(morpheus=morpheus)
acces_token=morpheus['morpheus']['apiAccessToken']
print(acces_token)


#get all tasks of type ansible and parse the id and then update the execute target

token = "43c4a82f-ee4d-4ac1-b88c-2492a7e6a3bc"
headers = {"Content-Type":"application/json","Accept":"application/json","Authorization": "BEARER " + (token)}
apiUrl = 'https://10.30.20.131/api/tasks?taskTypeCodes=ansibleTask'

response = requests.get(apiUrl, headers=headers, verify=False)
data = response.json()
tasks=data['tasks']

for i in tasks:
    for k,v in i.items():
        if k == 'id':
            jbody={"task": {"executeTarget": "resource"} }
            body=json.dumps(jbody)
            value=str(v)
            url=str('https://10.30.20.131/api/tasks/%s' % (value))
            r = requests.put(url, headers=headers, data=body, verify=False)
            print(r)
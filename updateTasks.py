import requests
import json
from morpheuscypher import Cypher
import os
import sys
from pprint import pprint
c = Cypher(morpheus=morpheus)
access_token=morpheus['morpheus']['apiAccessToken']
host=morpheus['morpheus']['applianceHost']
print(host)

#get all tasks of type ansible and parse the id and then update the execute target

headers = {"Content-Type":"application/json","Accept":"application/json","Authorization": "BEARER " + (access_token)}
apiUrl = str('https://%s/api/tasks?taskTypeCodes=ansibleTowerTask' % (host))
print(apiUrl)

response = requests.get(apiUrl, headers=headers, verify=False)
data = response.json()
tasks=data['tasks']
print(tasks)

for i in tasks:
    for k,v in i.items():
        if k == 'id':
            jbody={"task": {"executeTarget": "resource"} }
            body=json.dumps(jbody)
            value=str(v)
            url=str('https://%s/api/tasks/%s' % (host,value))
            r = requests.put(url, headers=headers, data=body, verify=False)
            print(r)
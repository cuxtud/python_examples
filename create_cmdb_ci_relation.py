#Need to install requests package for python
#easy_install requests
import requests
# Set the request parameters
instance_name=morpheus['instance']['name']
url = 'https://ven01434.service-now.com/api/now/cmdb/instance/cmdb_ci_vm_instance?sysparm_query=nameCONTAINS%s&sysparm_limit=1' % (instance_name)
# Eg. User name="admin", Password="admin" for this code sample.
user = 'admin'
pwd = 'Pa55w0rd'
# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}
# Do the HTTP request
response = requests.get(url, auth=(user, pwd), headers=headers )
# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()
# Decode the JSON response into a dictionary and use the data
data = response.json()
result = data['result']
jresult= json.dumps(result)

for i in result:
    for k,v in i.items():
        if k == 'sys_id':
            jbody={"inbound_relations": [{"type": "5f985e0ec0a8010e00a9714f2a172815", "target": "5f8af237c0a8010e01a932999468b83a", "sys_class_name": "cmdb_ci_apache_web_server"}], "source": "ServiceNow" }
            body=json.dumps(jbody)
            print(v)
            value=str(v)
            print(value)
            url = 'https://ven01434.service-now.com/api/now/cmdb/instance/cmdb_ci_vm_instance/%s/relation' % (value)
            # Eg. User name="admin", Password="admin" for this code sample.
            user = 'admin'
            pwd = 'Pa55w0rd'
            # Set proper headers
            headers = {"Content-Type":"application/json","Accept":"application/json"}
            # Do the HTTP request
            response = requests.get(url, auth=(user, pwd), headers=headers )
            # Check for HTTP codes other than 200
            if response.status_code != 200: 
                print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
                exit()
            # Decode the JSON response into a dictionary and use the data
            data = response.json()
            print(data)

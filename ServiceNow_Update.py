#Need to install requests package for python
#easy_install requests
import requests
import json

# Set the request parameters
url = 'https://dev69691.service-now.com/api/now/cmdb/instance/cmdb_ci_linux_server?sysparm_fields=name%2Cip_address%2Cram'

# Eg. User name="admin", Password="admin" for this code sample.
user = 'admin'
pwd = 'B5bRuAmFHnx0'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}
data = {"attributes": {"name":"instance-23", "ram": "3840", "ip_address": "34.68.85.149"}, "source": "ServiceNow"}
data1=json.dumps(data)
# Do the HTTP request
response = requests.post(url, auth=(user, pwd), headers=headers, data=data1)


# Check for HTTP codes other than 200
if response.status_code != 201:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)

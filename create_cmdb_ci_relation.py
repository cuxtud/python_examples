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
#sys_id = data['results']
print(data)


'''
def create_relation(sys_id):
    url = 'https://dev47749.service-now.com/api/now/cmdb/instance/cmdb_ci_linux_server/64ab8da09f030200fe2ab0aec32e701b/relation?sysparm_fields=sys_id%2Cname'
    # Eg. User name="admin", Password="admin" for this code sample.
    user = 'admin'
    pwd = 'admin'
    # Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}
    # Do the HTTP request

    response = requests.post(url, auth=(user, pwd), headers=headers ,data="{
        \"inbound_relations\": [
            {
                \"type\": \"5f985e0ec0a8010e00a9714f2a172815\",
                \"target\": \"45c60ced2f046c1026e0d6c6f699b620\",
                \"sys_class_name\": \"cmdb_ci_apache_webserver\"
            }
        ],
        \"source\": \"ServiceNow\"
    }")
    # Check for HTTP codes other than 200
    if response.status_code != 200: 
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()
    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    print(data)
'''
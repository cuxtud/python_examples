import requests
import json

headers="Content-Type: application/json"
ip=morpheus['container']['externalIp']
strip=str(ip)
print(ip)
url="https://%s" % (strip)
aurl=str(url)
nemailid=morpheus['customOptions']['fmoremailid']
emailid=str(nemailid)
firstname=morpheus['customOptions']['ffirstname']
smorpheusurl="https://%s/api/setup/init" % (strip)
nmorpheusurl=str(smorpheusurl)
def setup():
    morpheusurl=nmorpheusurl
    body={ "applianceName": "myenterprise-morpheus", "applianceUrl": aurl, "accountName": "Morpheus", "username": "admin", "password": "69f49632b13e", "email": "aabraham@morpheusdata.com", "firstName": firstname }
    b = json.dumps(body)
    response = requests.post(morpheusurl, headers=headers, data=b, verify=False)
    data = response.json()
    return data

setup()
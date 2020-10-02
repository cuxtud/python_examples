import requests
import json

headers="Content-Type: application/json"
ip=morpheus['container']['externalIp']
strip=str(ip)
print(ip)
url="https://%s" % (strip)
nemailid=morpheus['customOptions']['fmoremailid']
emailid=str(nemailid)
firstname=morpheus['customOptions']['ffirstname']
nmorpheusurl="https://%s/api/setup/init" % (strip)

def setup():
    morpheusurl=nmorpheusurl
    body={ "applianceName": "myenterprise-morpheus", "applianceUrl": url, "accountName": "Morpheus", "username": "admin", "password": "69f49632b13e", "email": emailid, "firstName": firstname }
    b = json.dumps(body)
    response = requests.post(morpheusurl, headers=headers, data=b)
    data = response.json()
    return data

setup()
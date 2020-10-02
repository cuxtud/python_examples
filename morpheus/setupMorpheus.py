import requests
import json

headers="Content-Type: application/json"
ip=morpheus['container']['externalIp']
strip=str(ip)
print(ip)
def setup(mip):
    emailid=morpheus['customOptions']['fmoremailid']
    firstname=morpheus['customOptions']['ffirstname']
    morpheusurl="https://%s/api/setup/init" % (mip)
    body={ "applianceName": "myenterprise-morpheus", "applianceUrl": "https://%s" % (mip), "accountName": "Morpheus", "username": "admin", "password": "69f49632b13e", "email": emailid, "firstName": firstname }
    b = json.dumps(body)
    response = requests.post(morpheusurl, headers=headers, data=b)
    data = response.json()
    return data

setup(strip)
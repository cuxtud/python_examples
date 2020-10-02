import requests
import json

headers="Content-Type: application/json"
ip=str(morpheus['container']['externalIp'])
url=str("https://%s" % (strip))
emailid=str(morpheus['customOptions']['fmoremailid'])
firstname=morpheus['customOptions']['ffirstname']
morpheusurl=str("https://%s/api/setup/init" % (strip))

def setup():
    morpheusurl=smorpheusurl
    body={ "applianceName": "myenterprise-morpheus", "applianceUrl": aurl, "accountName": "Morpheus", "username": "admin", "password": "69f49!632b13e", "email": "aabraham@morpheusdata.com", "firstName": firstname }
    b = json.dumps(body)
    response = requests.post(morpheusurl, headers=headers, data=b, verify=False)
    data = response.json()
    return data

setup()
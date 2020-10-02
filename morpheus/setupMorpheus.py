import requests
import json

headers={'Content-Type': 'application/json'}
ip=str(morpheus['container']['externalIp'])
url=str("https://%s" % (ip))
emailid=str(morpheus['customOptions']['fmoremailid'])
firstname=str(morpheus['customOptions']['ffirstname'])
morpheusurl=str("https://%s/api/setup/init" % (ip))

def setup():
    body={ "applianceName": "myenterprise-morpheus", "applianceUrl": url, "accountName": "Morpheus", "username": "admin", "password": "69F49!632b13e", "email": emailid, "firstName": firstname }
    b = json.dumps(body)
    response = requests.post(morpheusurl, headers=headers, data=b, verify=False)
    data = response.json()
    print(data)

setup()
print("This Lab is for %s with email: %s. Login with username: admin and password: 69F49!632b13e") % (firstname,emailid)
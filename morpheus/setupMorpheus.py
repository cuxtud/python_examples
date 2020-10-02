import requests
import json

headers="Content-Type: application/json"
ip=morpheus['container']['externalIp']
strip=str(ip)
print(ip)
url=str("https://%s" % (strip))
print(url)
#aurl=str(url)
nemailid=str(morpheus['customOptions']['fmoremailid'])
print(nemailid)
#emailid=str(nemailid)
firstname=morpheus['customOptions']['ffirstname']
smorpheusurl=str("https://%s/api/setup/init" % (strip))
print(smorpheusurl)
#nmorpheusurl=str(smorpheusurl)
'''
def setup():
    morpheusurl=smorpheusurl
    body={ "applianceName": "myenterprise-morpheus", "applianceUrl": aurl, "accountName": "Morpheus", "username": "admin", "password": "69f49!632b13e", "email": "aabraham@morpheusdata.com", "firstName": firstname }
    b = json.dumps(body)
    response = requests.post(morpheusurl, headers=headers, data=b, verify=False)
    data = response.json()
    return data

setup()
'''
import requests
import json
import time
from morpheuscypher import Cypher
import os
import sys

headers={'Content-Type': 'application/json',"Accept":"application/json"}
ip=str(morpheus['container']['externalIp'])
url=str("https://%s" % (ip))
emailid=str(morpheus['customOptions']['fmoremailid'])
firstname=str(morpheus['customOptions']['ffirstname'])
morpheusurl=str("https://%s/api/setup/init" % (ip))
licenseurl=str("https://%s/api/license" % (ip))


def setup():
    body={ "applianceName": "myenterprise-morpheus", "applianceUrl": url, "accountName": "Morpheus", "username": "admin", "password": "69F49!632b13e", "email": emailid, "firstName": firstname }
    b = json.dumps(body)
    response = requests.post(morpheusurl, headers=headers, data=b, verify=False)
    data = response.json()
    print(data)

#Sleep for 600secs before executing the setup
#time.sleep(1500)

#execute setup to run the initial setup of the appliance
#setup()
#print("This Lab is for %s with email: %s. Login with username: admin and password: 69F49!632b13e") % (firstname,emailid)

tokenurl=str("https://%s/oauth/token?grant_type=password&scope=write&client_id=morph-api"%(ip))
tokenheader={'Content-Type': 'application/x-www-form-urlencoded'}
#Get token of the appliance
def token():
    body = {'username': 'admin', 'password': '69F49!632b13e'}
    response = requests.post(tokenurl, headers=tokenheader, data=body, verify=False)
    data = response.json()
    access_token = data['access_token']
    return access_token


access_token=token()
print(access_token)

def license_key():
    c = Cypher(morpheus=morpheus)
    result = c.get("secret/labkey:license")
    pv=result.values()
    kv=(str(pv).strip('[]'))[2:-1]
    return kv

key=license_key()

#Add license to the appliance
license_headers={'Content-Type': 'application/json,"Accept":"application/json","Authorization": "BEARER " + (access_token)'}
def license(lkey):
    body={"license": lkey}
    b = json.dumps(body)
    response = requests.post(licenseurl, headers=license_headers, data=b, verify=False)
    data = response.json()
    print(data)

license(key)
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
key=str(morpheus['results']['getKey'])


def setup():
    body={ "applianceName": "myenterprise-morpheus", "applianceUrl": url, "accountName": "Morpheus", "username": "admin", "password": "69F49!632b13e", "email": emailid, "firstName": firstname }
    b = json.dumps(body)
    response = requests.post(morpheusurl, headers=headers, data=b, verify=False)
    data = response.json()
    print(data)

#Sleep for 900secs/15mins before executing the setup
time.sleep(900)

#execute setup to run the initial setup of the appliance
setup()
print("This Lab https://%s is for %s with email: %s. Login with username: admin and password: 69F49!632b13e") % (ip, firstname,emailid)

tokenurl=str("https://%s/oauth/token?grant_type=password&scope=write&client_id=morph-api"%(ip))
tokenheader={'Content-Type': 'application/x-www-form-urlencoded'}
#Get token of the appliance
def token():
    body = {'username': 'admin', 'password': '69F49!632b13e'}
    response = requests.post(tokenurl, headers=tokenheader, data=body, verify=False)
    data = response.json()
    access_token = data['access_token']
    return access_token


print("Get access token........")
access_token=token()
print(access_token)

def license_key():
    c = Cypher(morpheus=morpheus)
    result = c.get("secret/labkey:license")
    pv=result.values()
    print(pv)
    kv=(str(pv).strip('[]'))[2:-1]
    return kv

print("Get license key......")
#key=str(license_key())
print(key)

#Add license to the appliance
#license_headers={'Content-Type': 'application/json',"Authorization": "BEARER " + (access_token)}
license_headers={"Authorization": "BEARER " + (access_token)}

def license():
    body={"license": key}
    b = json.dumps(body)
    response = requests.post(licenseurl, headers=license_headers, data=b, verify=False)
    data = response.json()
    print(data)

print("Applying license key to appliance %s using token: %s and key %s") %(ip,access_token,key)
license()
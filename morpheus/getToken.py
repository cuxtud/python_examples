import requests

ip=str(morpheus['container']['externalIp'])
tokenurl=str("https://%s/oauth/token?grant_type=password&scope=write&client_id=morph-api"%(ip))
tokenheader={'Content-Type': 'application/x-www-form-urlencoded'}
#Get token of the appliance
def token():
    body = {'username': 'admin', 'password': '69F49!632b13e'}
    response = requests.post(tokenurl, headers=tokenheader, data=body, verify=False)
    data = response.json()
    access_token = data['access_token']
    return access_token


#print(token())
print(access_token)
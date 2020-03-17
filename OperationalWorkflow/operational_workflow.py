import requests
import json

#token = "token goes here"
#headers = {"Content-Type":"application/json","Accept":"application/json","Authorization": "Basic " + (token)}

def executeJenkinsWorkflow():
    #url = ""
    body = {"businessService": (morpheus['customOptions']['fvminstancename']),"location": (morphus['customOptions']['fvmlocation']), "usage": (morpheus['customOptions']['fvmusage']),"vmcpu": (morpheus['customOptions']['fvmcpu']),"vmmemory": (morpheus['customOptions']['fvmmemory']),"instancename": (['customOptions']['fvminstancename']),"centrifyZone": (morpheus['customOptions']['fvmcentrifyzone'])}
    b = json.dumps(body)
    print(b)
    #response = requests.post(generatereporturl, headers=headers, data=b)
    #data = response.json()
    #print(data)


executeJenkinsWorkflow()
    
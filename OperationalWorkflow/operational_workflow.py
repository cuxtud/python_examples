import requests
import json

#token = "token goes here"
#headers = {"Content-Type":"application/json","Accept":"application/json","Authorization": "Basic " + (token)}

def executeJenkinsWorkflow():
    #url = ""
    body = {"businessService": morpheus['customOptions']['fvminstancename']}
    #"<%=customOptions.fvmbusinessservice%>", "location": "<%=customOptions.fvmlocation%>", "usage": "<%=customOptions.fvmusage%>","vmcpu": "<%=customOptions.fvmcpu%>","vmmemory": "<%=customOptions.fvmmemory%>","instancename": "rkalv<%=customOptions.fvminstancename%>","centrifyZone": "<%=customOptions.fvmcentrifyzone%>"}
    b = json.dumps(body)
    print(b)
    #response = requests.post(generatereporturl, headers=headers, data=b)
    #data = response.json()
    #print(data)


executeJenkinsWorkflow()
    
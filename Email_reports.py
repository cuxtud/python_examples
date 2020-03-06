import requests
import json

token = "77937dc9-000c-4d70-b3db-0af0096c27b6"
headers = {"Content-Type":"application/json","Accept":"application/json","Authorization": "BEARER " + (token)}


# Generate Reports
def runreports(type):
    generatereporturl = 'https://sandbox.morpheusdata.com/api/reports/'
    body = { "report": {"type": type, "startDate": "2020-02-01", "endDate": "2020-02-10"}}
    b = json.dumps(body)
    response = requests.post(generatereporturl, headers=headers, data=b)
    data = response.json()
    #rid = data['reportResult'][0]['id']
    #print(str(rid))
    rid = data['reportResult']['id']
    return rid

sid = runreports('appCost')
print(sid)

# Fetch reports
def getreports(sid):
    fetchreporturl = 'https://sandbox.morpheusdata.com/api/reports/'+str(sid)
    response = requests.get(fetchreporturl, headers=headers)
    data = response.json()
    print(data)

getreports(sid)
#runreports('appCost')

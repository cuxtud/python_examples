import requests
import json

token = "77937dc9-000c-4d70-b3db-0af0096c27b6"
headers = {"Content-Type":"application/json","Accept":"application/json","Authorization": "BEARER " + (token)}

# Fetch reports
def getreports(id):
    fetchreporturl = 'https://sandbox.morpheusdata.com/api/reports/'+str(id)
    response = requests.get(fetchreporturl, headers=headers)
    data = response.json()
    print(data)

#reports('378')

# Generate Reports
def runreports(type):
    generatereporturl = 'https://sandbox.morpheusdata.com/api/reports/'
    body = { "report": {"type": type, "startDate": "2020-02-01", "endDate": "2020-02-10"}}
    b = json.dumps(body)
    response = requests.post(generatereporturl, headers=headers, data=b)
    data = response.json()
    print(data)

runreports('appCost')
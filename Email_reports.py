import requests
import json
import datetime

##Get the current date in format DD-MM-YYYY
x = datetime.datetime.now()
d = (x.strftime("%d")+"-"+x.strftime("%m")+"-"+x.strftime("%Y"))
currentdate=str(d)

##Get the start date in format DD-MM-YYYY, past 30 days
s = datetime.datetime.now() - datetime.timedelta(30)
sd = (s.strftime("%d")+"-"+s.strftime("%m")+"-"+s.strftime("%Y"))
startdate=str(sd)

token = "77937dc9-000c-4d70-b3db-0af0096c27b6"
headers = {"Content-Type":"application/json","Accept":"application/json","Authorization": "BEARER " + (token)}


# Generate Reports
def runreports(type):
    generatereporturl = 'https://sandbox.morpheusdata.com/api/reports/'
    body = { "report": {"type": type, "startDate": startdate, "endDate": currentdate}}
    b = json.dumps(body)
    response = requests.post(generatereporturl, headers=headers, data=b)
    data = response.json()
    #rid = data['reportResult'][0]['id']
    #print(str(rid))
    rid = data['reportResult']['id']
    return rid

#sid = runreports('appCost')
#print(sid)

# Fetch reports
def getreports(sid):
    fetchreporturl = 'https://sandbox.morpheusdata.com/api/reports/'+str(sid)
    response = requests.get(fetchreporturl, headers=headers)
    data = response.json()
    print(data)

#getreports(sid)

##Things to do
## Set the date range to 30 days
## Format the report data in csv and send it via email
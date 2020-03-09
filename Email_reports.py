import requests
import json
import datetime
import time
import csv

##Get the current date in format YYYY-MM-DD
x = datetime.datetime.now()
d = (x.strftime("%Y")+"-"+x.strftime("%m")+"-"+x.strftime("%d"))
currentdate=str(d)

##Get the start date in format YYYY-MM-DD, past 30 days
## The number in datetime.timedelta(30) can be set to whatever the last days report required.

s = datetime.datetime.now() - datetime.timedelta(30)
sd = (s.strftime("%Y")+"-"+s.strftime("%m")+"-"+s.strftime("%d"))
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

#sid = runreports('instanceCost')
#print(sid)

# Fetch reports
def getreports(sid):
    fetchreporturl = 'https://sandbox.morpheusdata.com/api/reports/'+str(sid)
    response = requests.get(fetchreporturl, headers=headers)
    data = response.json()
    #This is for app Cost
    #rows = data['reportResult']['rows'][2]
    #This is for instance Cost
    rows = data['reportResult']
    rtype = data['reportResult']['type']['name']
    filterTitle = data['reportResult']['filterTitle']
    print('\n'+rtype+'\n'+'\n'+filterTitle+'\n\nSummary\n')
    fname = "output.csv"
    with open(fname, "w") as file:
        csv_file = csv.writer(file)
        csv_file.writerow([rtype])
        csv_file.writerow([filterTitle])
        csv_file.writerow(["Summary"])
        csv_file.writerow(["Name","Cost","Price","Currency"])
        for i in data['reportResult']['rows']:
            for k,v in i.items():
                if k == 'data':
                    value = json.loads(v)
                    #print(value)
                    if "code" in value:
                        continue
                    else:
                        csv_file.writerow([value['name'],round(value['cost'],2),round(value['price'],2),value['currency']])


#time.sleep(20)
getreports(418)
#print(rdata)

##Things to do 
## Format the report data return in rows to print Summary of Report and then 
# loop the data to put them in colomns and write to CSV.

##Things completed
# The print rows in getreports now displays he content of the report what we see in UI
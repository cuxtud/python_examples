import requests
import json
import datetime
import time
import csv
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

##Get the current date in format YYYY-MM-DD
x = datetime.datetime.now()
d = (x.strftime("%Y")+"-"+x.strftime("%m")+"-"+x.strftime("%d"))
currentdate=str(d)

##Get the start date in format YYYY-MM-DD, past 30 days
## The number in datetime.timedelta(30) can be set to whatever the last days report required.

s = datetime.datetime.now() - datetime.timedelta(30)
sd = (s.strftime("%Y")+"-"+s.strftime("%m")+"-"+s.strftime("%d"))
startdate=str(sd)

# Update the token below
# If token can't be set here as plain text then store it in a file in the morpheus app server and then read from that file and pass it to the token variable.
token = "token goes here"
headers = {"Content-Type":"application/json","Accept":"application/json","Authorization": "BEARER " + (token)}


# Generate Reports
def runreports(type):
    generatereporturl = 'https://sandbox.morpheusdata.com/api/reports/'
    body = { "report": {"type": type, "startDate": startdate, "endDate": currentdate}}
    b = json.dumps(body)
    response = requests.post(generatereporturl, headers=headers, data=b)
    data = response.json()
    rid = data['reportResult']['id']
    return rid

# Fetch reports
def getreports(sid):
    fetchreporturl = 'https://sandbox.morpheusdata.com/api/reports/'+str(sid)
    response = requests.get(fetchreporturl, headers=headers)
    data = response.json()
    rows = data['reportResult']
    rtype = data['reportResult']['type']['name']
    filterTitle = data['reportResult']['filterTitle']
    fname = "/tmp/InstanceCostReport.csv"
    with open(fname, "w") as file:
        csv_file = csv.writer(file)
        csv_file.writerow([rtype])
        csv_file.writerow([filterTitle])
        csv_file.writerow(["Summary"])
        csv_file.writerow(["Name","Value"])
        for i in data['reportResult']['rows']:
            for k,v in i.items():
                if k == 'data':
                    value = json.loads(v)
                    if "code" in value:
                        csv_file.writerow([value['name'],round(value['value'],2)])
        csv_file.writerow(["Name","Cost","Price","Currency"])
        for i in data['reportResult']['rows']:
            for k,v in i.items():
                if k == 'data':
                    value = json.loads(v)
                    if "code" in value:
                        continue
                    else:
                        csv_file.writerow([value['name'],round(value['cost'],2),round(value['price'],2),value['currency']])

def send_mail():
    fromaddr = "info@morpheusdata.com"
    toaddr = "myemail@email.com"
    
    msg = MIMEMultipart()   
    msg['From'] = fromaddr 
    msg['To'] = toaddr  
    msg['Subject'] = "Monthly Instance Cost Report"
    body = "Hello, Attached is the monthly Instance Cost Report. Thanks MorpheusData"
    msg.attach(MIMEText(body, 'plain')) 
    filename = "InstanceCostReport.csv"
    attachment = open("/tmp/InstanceCostReport.csv", "rb") 
    p = MIMEBase('application', 'octet-stream') 
    p.set_payload((attachment).read()) 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    msg.attach(p) 
    s = smtplib.SMTP('127.0.0.1', 25) 
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text) 
    s.quit() 


# Send API to morpheus to run the report. The intanceCost below is the reporttype used.
sid = runreports('instanceCost')

##Sleeping for 20 seconds to let the report generate
time.sleep(20)

#Fetch the report which was generated and then parse the value to write to a CSV. This will write to a CSV on the morpheus app server in /tmp as InstanceCost.csv
getreports(sid)

#Send email with the InstanceCost.csv as an attachment
send_mail()

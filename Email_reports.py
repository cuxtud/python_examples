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
    #fname = "InstanceCostReport.csv"
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
                    #print(value)
                    if "code" in value:
                        csv_file.writerow([value['name'],round(value['value'],2)])
                        #print(value['name'],value['value'])
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

def send_mail():
    fromaddr = "aabraham@morpheusdata.com"
    toaddr = "aabraham@morpheusdata.com"
    
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    
    # storing the senders email address   
    msg['From'] = fromaddr 
    
    # storing the receivers email address  
    msg['To'] = toaddr 
    
    # storing the subject  
    msg['Subject'] = "Monthly Instance Cost Report"
    
    # string to store the body of the mail 
    body = "Hello, /n/t Attached is the monthly Instance Cost Report /nThanks,/nMorpheusData"
    
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    
    # open the file to be sent  
    filename = "InstanceCostReport.csv"
    attachment = open("/var/opt/morpheus/morpheus-ui/", "rb") 
    
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    
    # encode into base64 
    encoders.encode_base64(p) 
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    
    # creates SMTP session 
    s = smtplib.SMTP('info@gomorpheus.com', 587) 
    
    # start TLS for security 
    #s.starttls() 
    
    # Authentication 
    #s.login(fromaddr, "password") 
    
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
    
    # terminating the session 
    s.quit() 



getreports(419)
#send_mail()
#sid = runreports('instanceCost')
#time.sleep(20)
#getreports(sid)
##Things to do 
## Send email with the attachment
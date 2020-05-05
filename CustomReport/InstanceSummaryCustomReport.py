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
'''
def getSql():
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="morpheus",
        password="",
        database="morpheus"
    )
    mycursor = mydb.cursor()
    mycursor.execute("select name, date_created, cores_per_socket, status, plan_id, max_cores, provision_zone_id, max_memory, max_storage, created_by_id from instance")
    myresult = mycursor.fetchall()
    #for x in myresult:
    #    print(x)
    column_names = [i[0] for i in mycursor.description]
    fp = open('/tmp/report.csv', 'w')
    myFile = csv.writer(fp, lineterminator = '\n')
    myFile.writerow(column_names)   
    myFile.writerows(myresult)
    fp.close()

getSql()
'''
# Below is what we need to parse

'''
Datecreated=billingInfo(startDate)
Cloud= billingInfo(zones(0(zoneName))
servername=billingInfo(zones(0(instances(instances(0(name))))))
plan name=billingInfo(zones(0(instances(instances(0(containers(0(usages(0(servicePlanName))))))))))
cores= billingInfo(zones(0(instances(instances(0(containers(0(usages(0(applicablePrices(0(prices(1(quantity))))))))))))))
memory= billingInfo(zones(0(instances(instances(0(containers(0(usages(0(applicablePrices(0(prices(0(quantity))))))))))))))
storage= billingInfo(zones(0(instances(instances(0(containers(0(usages(0(applicablePrices(0(prices(3(quantity))))))))))))))
Create by username=billingInfo(zones(0(instances(instances(0(containers(0(usages(0(createdByUser))))))))))

metadataName=billingInfo(zones(0(instances(instances(0(containers(0(usages(0(metadata(0(name))))))))))))
metadataValue=billingInfo(zones(0(instances(instances(0(containers(0(usages(0(metadata(0(value)))))))))))
'''

# Update the token below
# If token can't be set here as plain text then store it in a file in the morpheus app server and then read from that file and pass it to the token variable.
token = ""
headers = {"Content-Type":"application/json","Accept":"application/json","Authorization": "BEARER " + (token)}

def report():
    apiUrl = 'https://10.30.20.164/api/billing/account/1'
    response = requests.get(apiUrl, headers=headers, verify=False)
    data = response.json()
    dc = data['billingInfo']['startDate']
    zones = data['billingInfo']['zones']
    #print(zones)
    cloudName = data['billingInfo']['zones'][0]['zoneName']
    serverName = data['billingInfo']['zones'][0]['instances']['instances'][0]['name']
    planName = data['billingInfo']['zones'][0]['instances']['instances'][0]['containers'][0]['usages'][0]['servicePlanName']
    coresCount = data['billingInfo']['zones'][0]['instances']['instances'][0]['containers'][0]['usages'][0]['applicablePrices'][0]['prices'][1]['quantity']
    memoryValue = data['billingInfo']['zones'][0]['instances']['instances'][0]['containers'][0]['usages'][0]['applicablePrices'][0]['prices'][0]['quantity']
    storageGB = data['billingInfo']['zones'][0]['instances']['instances'][0]['containers'][0]['usages'][0]['applicablePrices'][0]['prices'][3]['quantity']
    createdBy = data['billingInfo']['zones'][0]['instances']['instances'][0]['containers'][0]['usages'][0]['createdByUser']
    meta0Name = data['billingInfo']['zones'][0]['instances']['instances'][0]['containers'][0]['usages'][0]['metadata'][0]['name']
    meta0Value = data['billingInfo']['zones'][0]['instances']['instances'][0]['containers'][0]['usages'][0]['metadata'][0]['value']
    meta1Name = data['billingInfo']['zones'][0]['instances']['instances'][0]['containers'][0]['usages'][0]['metadata'][1]['name']
    meta1Value = data['billingInfo']['zones'][0]['instances']['instances'][0]['containers'][0]['usages'][0]['metadata'][1]['value']
    for i in data['billingInfo']:
        for k,v in i.items():
            if k == 'zones':
                value = json.loads(v)
                print(value)

    #fname = "C:/Anish/customInventorySummaryReport.csv"
    #with open(fname, "w") as file:
    #    csv_file = csv.writer(file)
    #    csv_file.writerow(["Summary"])
    #    csv_file.writerow(["Date Created","Cloud", "Server Name", "Plan Name", "Cores Count", "Memory (MB)", "Storage (GB)", "Created By", "Name", "Value"])


report()



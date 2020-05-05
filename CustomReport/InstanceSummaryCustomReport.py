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
        password="e920bc9fb0659a5257df814c",
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
token = "43c4a82f-ee4d-4ac1-b88c-2492a7e6a3bc"
headers = {"Content-Type":"application/json","Accept":"application/json","Authorization": "BEARER " + (token)}

#Datecreated
def testreport():
    apiUrl = 'https://10.30.20.164/api/billing/account/1'
    response = requests.get(apiUrl, headers=headers, verify=False)
    data = response.json()
    dc = data['billingInfo']['startDate']
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
    print("Date Created: " +dc)
    print("Cloud Name: " +cloudName)
    print("Server Name: " + serverName)
    print("Plan: " + planName)
    print("Total Cores: " + str(coresCount))
    print("Memory (MB): " + str(memoryValue))
    print("Total Stoage (GB): " + str(storageGB))
    print("Create by: " + createdBy)
    print("Tag Name: " + meta0Name)
    print("Tag Value: " + meta0Value)
    print("Tag Name: " + meta1Name)
    print("Tag Value: " + meta1Value)


#testreport()

def report():
    apiUrl = 'https://10.30.20.164/api/billing/account/1'
    response = requests.get(apiUrl, headers=headers, verify=False)
    data = response.json()
    dc = data['billingInfo']['startDate']
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
    fname = "C:/Anish/customInventorySummaryReport.csv"
    with open(fname, "w") as file:
        csv_file = csv.writer(file)
        csv_file.writerow(["Summary"])
        csv_file.writerow(["Date Created","Cloud", "Server Name", "Plan Name", "Cores Count", "Memory (MB)", "Storage (GB)", "Created By", "Name", "Value"])
        #for i in data['billingInfo']['zones']:
        for i in data['billingInfo']:
            print(i)
        #csv_file.writerow([dc])
        #csv_file.writerow([cloudName])
        #csv_file.writerow([serverName])
        #csv_file.writerow([planName])
        #csv_file.writerow([coresCount])
        #csv_file.writerow([memoryValue])
        #csv_file.writerow([storageGB])
        #csv_file.writerow([createdBy])
        #csv_file.writerow([meta0Name])
        #csv_file.writerow([meta0Value])
        #csv_file.writerow([meta1Name])
        #csv_file.writerow([meta1Value])

report()



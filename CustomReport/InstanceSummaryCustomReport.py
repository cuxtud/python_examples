import requests
import json
import datetime
import time
import csv
import smtplib 
import mysql.connector
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

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
    for x in myresult:
        print(x)

getSql()


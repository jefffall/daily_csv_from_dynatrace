#!/usr/bin/python3
from datetime import timedelta, datetime
import sys
import pytz
import os
import smtplib
from email.mime.text import MIMEText


now = datetime.now()
yesterday = now - timedelta(days=1)
timezone = pytz.timezone("America/Los_Angeles")
d_aware = timezone.localize(yesterday)

date_string = str(d_aware)

dateList = date_string.split("-")

trueDate =  dateList[1] + "." + dateList[2][:2] + "." + dateList[0]

args = "your_account_name_here Password_here 240 "+ trueDate  + "_00:00:00 " + trueDate + "_23:59:59 ALL"

os.system('/usr/bin/python3 /home/jfall/dynatrace/dtget.py ' + args)

fileNameList = os.listdir('/home/jfall/dynatrace/outboundmailfile')
fileName = fileNameList[-1]

fileNameClean = fileName.replace(":",".")

myPath = "/home/jfall/dynatrace/outboundmailfile/"

os.rename(myPath+fileName,myPath+fileNameClean)

fileName = fileNameClean

filePathAndName  = '/home/jfall/dynatrace/outboundmailfile/' + fileName

# mpack -s "testfile.csv" testfile.csv jeffreyefall@gmail.com

mpack_string  =  'mpack -s ' + '"' +  fileName + '" -d /home/jfall/dynatrace/joboutput.txt '  + filePathAndName + " " 

to = "your_email@gmail.com"
os.system(mpack_string + to)

os.remove(filePathAndName)

import datetime
import os
import requests
import json
from Fanc import Fanc
import mysql.connector
import pytz

# Set the time zone to Israel time
israel_timezone = pytz.timezone('Asia/Jerusalem')

Token = Fanc.get_Token ()
directory = os.getcwd()
f=open(directory + "/Last_Date_LP.txt", "r")
startOfIntervalFrom = f.read()
# Convert the string to a datetime object
date_object = datetime.datetime.strptime(startOfIntervalFrom, '%Y-%m-%dT%H:%M:%S')
# Import timedelta separately and add 1 day to the date
from datetime import timedelta
new_date = date_object + timedelta(days=1)
# Format the new_date as a string with the desired format
startOfIntervalTo = new_date.strftime('%Y-%m-%dT%H:%M:%S')
# Define the endpoint URL Test
# url = 'https://iecom--preprod.sandbox.my.salesforce.com/services/apexrest/MeterLP/'

# Define the endpoint URL Prod
# url = 'https://iecom.my.salesforce.com/services/apexrest/MeterLP/'
url = "https://iecom.my.salesforce.com/services/apexrest/MeterLP/"

# Define the headers
headers = {
    'Authorization': 'Bearer ' + Token,
    'X-PrettyPrint': '1',
    'Content-Type': 'application/json'
}


# Define the JSON body
data = {
    "meterNumber" : "",
    "accountName" : "S540321494", # Prod
    "startOfIntervalFrom" : startOfIntervalFrom, # Prod
    "startOfIntervalTo" : startOfIntervalTo, # Prod
    #"startOfIntervalFrom" : "2024-01-23T00:00:00", # Prod
    #"startOfIntervalTo" : "2024-01-24T00:00:00", # Prod
    "recExportTimeTo": None, # Prod
    "recExportTimeFrom": None, # Prod
}


# Convert the data to JSON format
json_data = json.dumps(data)

# Send the POST request
response = requests.post(url, headers=headers, data=json_data)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    response_data = response.json()
   
    # Process the response data as needed
    print("Response:", response_data)
else:
    # Print an error message if the request failed
    print("Error:", response.status_code, response.text)

# Connect to the database
connection = mysql.connector.connect(
    host="enova-prod-main.cc1atg19czgb.eu-central-1.rds.amazonaws.com",
    user="admin",
    password="JdAA78!fjGjkasdDF8",
    database="Electrical_Power",
    port = 3308  
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()
# electrical_power_SATEC_LP

# Loop through meterList and lpList to insert data into the table
for meter in response_data['meterList']:
    meterNumber = meter['meterNumber']
    for lp in meter['lpList']:
        transformer_U = lp['transformer_U']
        startOfInterval = datetime.datetime.strptime(lp['startOfInterval'], '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=pytz.utc).astimezone(israel_timezone)
        recExportTime = datetime.datetime.strptime(lp['recExportTime'], '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=pytz.utc).astimezone(israel_timezone)
        reactiveIKVARH = lp['reactiveIKVARH']
        reactiveEKVARH = lp['reactiveEKVARH']
        lastRecordStatus = lp['lastRecordStatus']
        endOfInternal = datetime.datetime.strptime(lp['endOfInternal'], '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=pytz.utc).astimezone(israel_timezone)
        activeIKWH = lp['activeIKWH']
        activeEKWH = lp['activeEKWH']

        # Insert data into the table
        query = "INSERT INTO Gefen_LP (meterNumber, transformer_U, startOfInterval, recExportTime, reactiveIKVARH, reactiveEKVARH, lastRecordStatus, endOfInternal, activeIKWH, activeEKWH) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (meterNumber, transformer_U, startOfInterval, recExportTime, reactiveIKVARH, reactiveEKVARH, lastRecordStatus, endOfInternal, activeIKWH, activeEKWH)
        cursor.execute(query, values)

# Commit changes and close connections
connection.commit()
cursor.close()
connection.close()

with open(directory + "/Last_Date_LP.txt", "w") as file:
    file.write(startOfIntervalTo)

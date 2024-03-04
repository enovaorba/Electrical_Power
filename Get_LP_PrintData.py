import datetime
import os
import requests
import json
from Fanc import Fanc
import mysql.connector

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
    "startOfIntervalFrom" : "2023-01-04T00:01:00", # Prod
    "startOfIntervalTo" : "2023-02-01T02:14:00", # Prod
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


#with open(directory + "/Last_Date_LP.txt", "w") as file:
#    file.write(startOfIntervalTo)

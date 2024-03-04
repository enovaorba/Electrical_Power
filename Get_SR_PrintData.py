import datetime
from errno import errorcode
import os
import requests
import json
from Fanc import Fanc
import mysql.connector
from datetime import datetime as dt

Token = Fanc.get_Token ()
directory = os.getcwd()
f=open(directory + "/Last_Date_SR.txt", "r")
startOfIntervalFrom = f.read()
# Convert the string to a datetime object
date_object = datetime.datetime.strptime(startOfIntervalFrom, '%Y-%m-%dT%H:%M:%S')
# Import timedelta separately and add 1 day to the date
from datetime import timedelta
new_date = date_object + timedelta(days=1)
# Format the new_date as a string with the desired format
startOfIntervalTo = new_date.strftime('%Y-%m-%dT%H:%M:%S')


# Define the endpoint URL
# url =   'https://iecom--preprod.sandbox.my.salesforce.com/services/apexrest/MeterSelfReading/'
url = "https://iecom.my.salesforce.com/services/apexrest/MeterSelfReading/"

# Define the headers
headers = {
     'Authorization': 'Bearer ' + Token,
    'X-PrettyPrint': '1',
    'Content-Type': 'application/json'
}

# Define the JSON body
data = {
# "meterNumber" : "", # Test
# "accountName" : "S123456789", # Test
# "srTimeFrom" : "2023-05-18T21:00:00", # Test
# "srTimeTo" : "2023-05-30T20:59:00", # Test
# "RecordsInPage": 2000,
"meterNumber" : "85306150909", # Prod
"accountName" : "540321494", # Prod
"srTimeFrom" : "2023-08-01T00:00:00", # Prod
"srTimeTo" : "2023-09-29T00:00:00", # Prod
"recExTimeFrom" : None, # Prod
"recExTimeTo" : None,
"SrNumberFrom" :None
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



#with open(directory + "/Last_Date_SR.txt", "w") as file:
#    file.write(startOfIntervalTo)

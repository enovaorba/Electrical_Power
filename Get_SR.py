import datetime
from errno import errorcode
import os
import requests
import json
from Fanc import Fanc
import mysql.connector
from datetime import datetime as dt
import pytz

# Set the time zone to Israel time
israel_timezone = pytz.timezone('Asia/Jerusalem')

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
"srTimeFrom" : "2023-12-01T00:00:00", # Prod
"srTimeTo" : "2023-12-29T00:00:00", # Prod
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


def insert_data(cursor, data):
    insert_query = """
    INSERT INTO Gefen_SR (
        meter_number, self_reading_time, rec_export_time,
        reactive_i_totalc, reactive_i_md1c, reactive_i_accu_md1c,
        reactive_i_3c, reactive_i_2c, reactive_i_1c,
        reactive_e_totalc, reactive_e_3c, reactive_e_2c, reactive_e_1c,
        active_i_total, active_i_md3c, active_i_md2c, active_i_md1c,
        active_i_accu_md3c, active_i_accu_md2c, active_i_accu_md1c,
        active_i_3c, active_i_2c, active_i_1c,
        active_e_total, active_e_3c, active_e_2c, active_e_1c
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    
    for meter_data in response_data['meterList']:
        meter_number = meter_data['meterNumber']
        for sr_data in meter_data['srList']:
            self_reading_time = dt.strptime(sr_data['selfReadingTime'], '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=pytz.utc).astimezone(israel_timezone)
            rec_export_time = dt.strptime(sr_data['recExportTime'], '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=pytz.utc).astimezone(israel_timezone)

            values = (
                meter_number,
                self_reading_time,
                rec_export_time,
                sr_data['reactiveITotalc'],
                sr_data['reactiveIMD1c'],
                sr_data['reactiveIAccuMD1c'],
                sr_data['reactiveI3c'],
                sr_data['reactiveI2c'],
                sr_data['reactiveI1c'],
                sr_data['reactiveETotalc'],
                sr_data['reactiveE3c'],
                sr_data['reactiveE2c'],
                sr_data['reactiveE1c'],
                sr_data['activeITotal'],
                sr_data['activeIMD3c'],
                sr_data['activeIMD2c'],
                sr_data['activeIMD1c'],
                sr_data['activeIAccuMD3c'],
                sr_data['activeIAccuMD2c'],
                sr_data['activeIAccuMD1c'],
                sr_data['activeI3c'],
                sr_data['activeI2c'],
                sr_data['activeI1c'],
                sr_data['activeETotalc'],
                sr_data['activeE3c'],
                sr_data['activeE2c'],
                sr_data['activeE1c'],
            )
            
            cursor.execute(insert_query, values)

def main():
    try:
        
        insert_data(cursor, json_data)

        connection.commit()
        print("Data inserted successfully.")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access denied. Check your credentials.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist.")
        else:
            print(err)

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    main()


with open(directory + "/Last_Date_SR.txt", "w") as file:
    file.write(startOfIntervalTo)

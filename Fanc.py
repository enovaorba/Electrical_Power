import requests
import json
import datetime
import os
import mysql.connector
import pytz
from datetime import datetime, timedelta


class Fanc:
    
    def PrintFile(line, NameFile):
        # Define Israel timezone
        israel_timezone = pytz.timezone('Asia/Jerusalem')
        line = datetime.now(israel_timezone).strftime('%Y-%m-%dT%H:%M:%S') + " " + line
        directory = os.getcwd()
        NameFile = directory + NameFile
        file_object = open(NameFile, 'a')
        file_object.write(line + "\n")
        file_object.close()
        #ShrinkFile
        file = open(NameFile, "r")
        s_file = file.read()
        MinL = len(s_file)
        MaxL = 10000000;
        if MinL > MaxL:
            file_object = open(NameFile, 'w')
            file_object.write(s_file[0:(MinL - (MaxL / 2))] + "\n")
            file_object.close()


    def get_Token():
        # Define the URL you want to send the POST request to
        # url = 'https://iecom--preprod.sandbox.my.salesforce.com/services/oauth2/token?grant_type=password&client_id=3MVG9sh10GGnD4Dt2L_VxUozN4EtszPZrcSdjr8HoWVSacnjkoLHj.slC6iNSTWPpyzQJMF43SKXn95f3zWCC&client_secret=7CE1E5212E755654ABDC82B22E42AC215AF0ECD71D4F24A774A67B3EB5DB657D&username=Test.Z@gmail.com.gefenapi&password=Aa123456qbEk6aZDSo46iFdBl1NatStg'
        url = "https://iecom.my.salesforce.com/services/oauth2/token?grant_type=password&client_id=3MVG9sh10GGnD4Dt2L_VxUozN4EtszPZrcSdjr8HoWVSacnjkoLHj.slC6iNSTWPpyzQJMF43SKXn95f3zWCC&client_secret=7CE1E5212E755654ABDC82B22E42AC215AF0ECD71D4F24A774A67B3EB5DB657D&username=yaelh@satec-global.com.gefenapi&password=Yh@25062022cUsZwvXhmHXN7h2iG2qnc8RxS"
        # Define the data you want to send in the request body
        data = {
            'param1': 'value1',
            'param2': 'value2'
        }

        # Send the POST request with JSON data in the request body
        response = requests.post(url, json=data)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            response_data = response.json()

            # Extract the value of the access_token field
            access_token = response_data.get('access_token')

            if access_token:
                print(f'Access Token: {access_token}')
            else:
                print('Access Token not found in the response.')
        else:
            # Print an error message if the request failed
            print(f'Error: {response.status_code}')
            print(response.text)
            return response.text
        return access_token


    def Get_LP(accountName,startOfIntervalFrom2,startOfIntervalTo2):
        
        # Set the time zone to Israel time
        israel_timezone = pytz.timezone('Asia/Jerusalem')

        Token = Fanc.get_Token ()
        directory = os.getcwd()
        f=open(directory + "/Last_Date_LP.txt", "r")
        startOfIntervalFrom = f.read()
        # Convert the string to a datetime object
        date_object = datetime.strptime(startOfIntervalFrom, '%Y-%m-%dT%H:%M:%S')
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
            "accountName" : accountName, # Prod
            "startOfIntervalFrom" : startOfIntervalFrom2, # Prod
            "startOfIntervalTo" : startOfIntervalTo2, # Prod
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
            host= "enova-prod-main.cc1atg19czgb.eu-central-1.rds.amazonaws.com",
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
                startOfInterval = datetime.strptime(lp['startOfInterval'], '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=pytz.utc).astimezone(israel_timezone)
                recExportTime = datetime.strptime(lp['recExportTime'], '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=pytz.utc).astimezone(israel_timezone)
                reactiveIKVARH = lp['reactiveIKVARH']
                reactiveEKVARH = lp['reactiveEKVARH']
                lastRecordStatus = lp['lastRecordStatus']
                endOfInternal = datetime.strptime(lp['endOfInternal'], '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=pytz.utc).astimezone(israel_timezone)
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

    def Get_SR(accountName,startOfIntervalFrom,startOfIntervalTo):
            Token = Fanc.get_Token ()
            # Define the endpoint URL
            url = 'https://iecom--preprod.sandbox.my.salesforce.com/services/apexrest/MeterLP/'
            headers = {
                'Authorization': 'Bearer ' + Token,
                'X-PrettyPrint': '1',
                'Content-Type': 'application/json'
            }
 
            # Define the JSON body
            data = {
                {
                    "meterNumber" : "",
                    "accountName" : accountName,
                    "srTimeFrom" : startOfIntervalFrom,
                    "srTimeTo" : startOfIntervalTo,
                    "recExTimeFrom" : "",
                    "recExTimeTo" : "",
                    "SrNumberFrom" :""
                }  

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
                return response_data
            else:
                # Print an error message if the request failed
                print("Error:", response.status_code, response.text)
                return response.status_code, response.text

    

    
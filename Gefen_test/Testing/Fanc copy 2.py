import requests
import json


class Fanc:
    
    def PrintFile(line, NameFile):
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
        url = 'https://iecom--preprod.sandbox.my.salesforce.com/services/oauth2/token?grant_type=password&client_id=3MVG9sh10GGnD4Dt2L_VxUozN4EtszPZrcSdjr8HoWVSacnjkoLHj.slC6iNSTWPpyzQJMF43SKXn95f3zWCC&client_secret=7CE1E5212E755654ABDC82B22E42AC215AF0ECD71D4F24A774A67B3EB5DB657D&username=Test.Z@gmail.com.gefenapi&password=Aa123456qbEk6aZDSo46iFdBl1NatStg'
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


    def Get_LP(accountName,startOfIntervalFrom,startOfIntervalTo):
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
            "meterNumber" : "",
            "accountName" : accountName,
            "startOfIntervalFrom" : startOfIntervalFrom,
            "startOfIntervalTo" : startOfIntervalTo,
            "RecordsInPage": 2000
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
    

    
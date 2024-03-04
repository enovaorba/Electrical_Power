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


    def get_Token(url):
        # Define the URL you want to send the POST request to

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

            
from Fanc import Fanc
import requests
import json

Token = Fanc.get_Token ()

# Define the endpoint URL
url = 'https://iecom--preprod.sandbox.my.salesforce.com/services/oauth2/token?grant_type=password&client_id=3MVG9sh10GGnD4Dt2L_VxUozN4EtszPZrcSdjr8HoWVSacnjkoLHj.slC6iNSTWPpyzQJMF43SKXn95f3zWCC&client_secret=7CE1E5212E755654ABDC82B22E42AC215AF0ECD71D4F24A774A67B3EB5DB657D&username=Test.Z@gmail.com.gefenapi&password=Aa123456qbEk6aZDSo46iFdBl1NatStg'

# Define the headers
headers = {
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
    'X-PrettyPrint': '1',
    'Content-Type': 'application/json'
}

# Define the JSON body
data = {
    
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

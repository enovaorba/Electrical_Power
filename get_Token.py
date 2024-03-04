import requests
import json

# Define the URL you want to send the POST request to Test
# url = 'https://iecom--preprod.sandbox.my.salesforce.com/services/oauth2/token?grant_type=password&client_id=3MVG9sh10GGnD4Dt2L_VxUozN4EtszPZrcSdjr8HoWVSacnjkoLHj.slC6iNSTWPpyzQJMF43SKXn95f3zWCC&client_secret=7CE1E5212E755654ABDC82B22E42AC215AF0ECD71D4F24A774A67B3EB5DB657D&username=Test.Z@gmail.com.gefenapi&password=Aa123456qbEk6aZDSo46iFdBl1NatStg'

# Define the URL you want to send the POST request to Prod
##url = 'https://iecom--preprod.sandbox.my.salesforce.com/services/oauth2/token?grant_type=password&client_id=3MVG9sh10GGnD4Dt2L_VxUozN4EtszPZrcSdjr8HoWVSacnjkoLHj.slC6iNSTWPpyzQJMF43SKXn95f3zWCC&client_secret=7CE1E5212E755654ABDC82B22E42AC215AF0ECD71D4F24A774A67B3EB5DB657D&username=yaelh@satec-global.com.gefenapi&password=Yh@25062022cUsZwvXhmHXN7h2iG2qnc8RxS'
# url = "https://iecom.my.salesforce.com/services/oauth2/token?grant_type=password&client_id=3MVG9sh10GGnD4Dt2L_VxUozN4EtszPZrcSdjr8HoWVSacnjkoLHj.slC6iNSTWPpyzQJMF43SKXn95f3zWCC&client_secret=7CE1E5212E755654ABDC82B22E42AC215AF0ECD71D4F24A774A67B3EB5DB657D&username=yaelh@satec-global.com.gefenapi&password=Yh@25062022cUsZwvXhmHXN7h2iG2qnc8RxS"
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
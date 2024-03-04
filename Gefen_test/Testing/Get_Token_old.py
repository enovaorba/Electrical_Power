import requests

# Define the Salesforce OAuth2 token endpoint URL
token_url = 'https://iecom--preprod.sandbox.my.salesforce.com/services/oauth2/token?grant_type=password&client_id=3MVG9sh10GGnD4Dt2L_VxUozN4EtszPZrcSdjr8HoWVSacnjkoLHj.slC6iNSTWPpyzQJMF43SKXn95f3zWCC&client_secret=7CE1E5212E755654ABDC82B22E42AC215AF0ECD71D4F24A774A67B3EB5DB657D&username=Test.Z@gmail.com.gefenapi&password=Aa123456qbEk6aZDSo46iFdBl1NatStg'

# Define the request parameters
params = {
    'grant_type': 'password',
    'client_id': 'YOUR_CONSUMER_KEY',
    'client_secret': 'YOUR_CONSUMER_SECRET',
    'username': 'user@domain.co.il',
    'password': 'intUser369*363636784BXQvxxx764Lap'
}

# Send the POST request
response = requests.post(token_url, data=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    token_data = response.json()
    
    # Print the access token and other relevant information
    print("Access Token:", token_data['access_token'])
    print("Instance URL:", token_data['instance_url'])
    print("Token Type:", token_data['token_type'])
else:
    # Print an error message if the request failed
    print("Error:", response.status_code, response.text)

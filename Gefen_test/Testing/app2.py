from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define a function to get a value from an external API
def get_value(input_value):
    # Replace 'external_api_url' with the actual URL of the external API
    external_api_url = f'http://164.92.139.174:5000?param={input_value}'  # Include input_value in the API URL

    # Make a GET request to the external API
    response = requests.get(external_api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to fetch data from the external API'}

# Create a route to handle GET requests and accept an input value from the URL
@app.route('/get-value/<input_value>', methods=['GET'])
def get_value_route(input_value):
    value = get_value(input_value)
    return jsonify(value)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

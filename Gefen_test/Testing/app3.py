def get_value(input_value):
    external_api_url = f'https://example.com/api?param={input_value}'  # Replace with the actual API URL
    try:
        response = requests.get(external_api_url)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the external API: {str(e)}")
        return {'error': 'Failed to fetch data from the external API'}


from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define a function to get a value from an external API
def get_value(input_value):
    external_api_url = f'http://164.92.139.174:5000?param={input_value}'  # Replace with the actual API URL
    try:
        response = requests.get(external_api_url)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the external API: {str(e)}")
        return {'error': 'Failed to fetch data from the external API'}

# Create a route to handle GET requests and accept an input value from the URL
@app.route('/get-value/<input_value>', methods=['GET'])
def get_value_route(input_value):
    value = get_value(input_value)
    return jsonify(value)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

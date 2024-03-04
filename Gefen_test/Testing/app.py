from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a sample function to get a value
def get_value():
    input_value='123456'
    return "Hello, World!" + input_value
def F_Get_LP():
    return "Hello, World!"

# Create a route to handle GET requests and return a value
@app.route('/get-value/<input_value>', methods=['GET'])
def get_value_route(input_value):
    value = get_value(input_value)
    return jsonify(value)


if __name__ == '__main__':
    app.run(host='164.92.139.174', port=5000)
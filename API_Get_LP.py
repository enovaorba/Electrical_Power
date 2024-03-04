from flask import Flask, request, jsonify
from Fanc import Fanc
#http://164.92.139.174:5000/accountName/S123456789/startOfIntervalFrom/2023-05-18T21:00:00/startOfIntervalTo/2023-05-30T20:59:00

app = Flask(__name__)

@app.route('/accountName/<param_a>/startOfIntervalFrom/<param_b>/startOfIntervalTo/<param_c>', methods=['GET'])
def add_parameters(param_a, param_b,param_c):
    
    try:
        result_a = f"{param_a}"
        result_b = f"{param_b}"
        param_c = f"{param_c}"
        Get_Data = Fanc.Get_LP(param_a,param_b,param_c)
        return jsonify({"result": Get_Data})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

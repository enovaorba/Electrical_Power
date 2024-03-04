from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add_aaa/<parameter>', methods=['GET'])
def add_aaa(parameter):
    try:
        result = f"{parameter}AAA"
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

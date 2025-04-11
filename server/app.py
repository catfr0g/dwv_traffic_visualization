from flask import Flask, request, jsonify
from flask_cors import CORS  # Allows cross-origin requests from the frontend

app = Flask(__name__)
CORS(app)  # Enable CORS if your frontend runs on another port

# In-memory store for packages
packages = []

@app.route('/traffic', methods=['GET'])
def receive_traffic():
    # Get JSON data from the request
    package = request.get_json()
    if package:
        packages.append(package)
        print(f"Received package: {package}")
        return jsonify({"status": "received"}), 200
    else:
        return jsonify({"error": "No JSON data received"}), 400

@app.route('/data', methods=['GET'])
def get_data():
    # Return all received package data to frontend
    return jsonify(packages), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
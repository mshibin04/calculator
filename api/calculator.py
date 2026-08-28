from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

def perform_calculation(number1, number2, operation):
    """Backend calculation logic"""
    try:
        num1 = float(number1)
        num2 = float(number2)
        
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            if num2 == 0:
                return {"error": "Cannot divide by zero"}
            return num1 / num2
        else:
            return {"error": "Invalid operation"}
    except ValueError:
        return {"error": "Invalid numbers"}

@app.route('/', methods=['GET'])
def home():
    """Serve the main HTML file"""
    return send_file('public/index.html')

@app.route('/api/calculate', methods=['POST'])
def calculate():
    """API endpoint for calculations"""
    data = request.json
    
    try:
        number1 = data.get('number1')
        number2 = data.get('number2')
        operation = data.get('operation')
        
        if number1 is None or number2 is None or not operation:
            return jsonify({"error": "Missing parameters"}), 400
        
        result = perform_calculation(number1, number2, operation)
        
        if isinstance(result, dict) and "error" in result:
            return jsonify(result), 400
        
        return jsonify({"result": result}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

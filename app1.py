from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the GET endpoint
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

# Define the POST endpoint
@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        # Parse JSON data from the request
        data = request.get_json()
        
        # Basic input validation
        if not data or 'data' not in data:
            return jsonify({"is_success": False, "message": "Invalid input"}), 400
        
        # Extract numbers and alphabets from the input array
        input_data = data['data']
        numbers = [item for item in input_data if item.isdigit()]
        alphabets = [item for item in input_data if item.isalpha()]

        # Find the highest lowercase alphabet
        lowercase_alphabets = [char for char in alphabets if char.islower()]
        highest_lowercase_alphabet = [max(lowercase_alphabets)] if lowercase_alphabets else []

        # Construct the response
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",  # Replace with actual user_id logic if needed
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

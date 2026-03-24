from flask import Flask, request, jsonify
import math

app = Flask(__name__)


@app.route('/api/test')
def hello():
    return {'message': 'Hello World!'}


# Addition operation
@app.route('/api/add', methods=['POST'])
def add():
    data_request = request.get_json()
    if (not data_request or 'number_1' not in data_request or
            'number_2' not in data_request):
        return jsonify({'error': 'Invalid input'}), 400

    number_1 = float(data_request['number_1'])
    number_2 = float(data_request['number_2'])
    result = number_1 + number_2
    return jsonify({'result': result})


# Optional: Completing the following TODOs is optional for more practice

# TODO: Implement the 'multiplication operation'
@app.route('/api/multiply', methods=['POST'])
def multiply():
    data_request = request.get_json()
    # Check if the input is valid
    if (not data_request or 'number_1' not in data_request or
            'number_2' not in data_request):
        return jsonify({'error': 'Invalid input'}), 400

    number_1 = float(data_request['number_1'])
    number_2 = float(data_request['number_2'])
    result = number_1 * number_2
    return jsonify({'result': result})


# TODO: Implement the 'subtraction operation'
@app.route('/api/subtract', methods=['POST'])
def subtract():
    data_request = request.get_json()
    # Check if the input is valid
    if (not data_request or 'number_1' not in data_request or
            'number_2' not in data_request):
        return jsonify({'error': 'Invalid input'}), 400

    number_1 = float(data_request['number_1'])
    number_2 = float(data_request['number_2'])
    result = number_1 - number_2
    return jsonify({'result': result})

# TODO: Implement the 'division operation'
@app.route('/api/divide', methods=['POST'])
def divide():
    # Check if the input is valid
    data_request = request.get_json()
    if (not data_request or 'number_1' not in data_request or
            'number_2' not in data_request):
        return jsonify({'error': 'Invalid input'}), 400
    number_1 = float(data_request['number_1'])
    number_2 = float(data_request['number_2'])
    if number_2 == 0:
        return jsonify({'error': 'Division by zero is not allowed'}), 400
    result = number_1 / number_2
    return jsonify({'result': result})

# TODO: Add more routes and operations! Create your own calculator!
# For example:
# - Square root
# - Exponentiation
# - Trigonometric functions (sin, cos, tan)
# - Logarithms

@app.route('/api/square_root', methods=['POST'])
def square_root():
    data_request = request.get_json()
    if (not data_request or 'number' not in data_request):
        return jsonify({'error': 'Invalid input'}), 400

    number = float(data_request['number'])
    if number < 0:
        return jsonify({'error': 'Square root of negative number is not allowed'}), 400
    result = number ** 0.5
    return jsonify({'result': result})


@app.route('/api/exponentiation', methods=['POST'])
def exponentiation():
    data_request = request.get_json()
    if (not data_request or 'base' not in data_request or
            'exponent' not in data_request):
        return jsonify({'error': 'Invalid input'}), 400

    base = float(data_request['base'])
    exponent = float(data_request['exponent'])
    result = base ** exponent
    return jsonify({'result': result})

@app.route('/api/sin', methods=['POST'])
def sin():
    data_request = request.get_json()
    if (not data_request or 'angle' not in data_request):
        return jsonify({'error': 'Invalid input'}), 400

    angle = float(data_request['angle'])
    result = math.sin(math.radians(angle))
    return jsonify({'result': result})

@app.route('/api/cos', methods=['POST'])
def cos():
    data_request = request.get_json()
    if (not data_request or 'angle' not in data_request):
        return jsonify({'error': 'Invalid input'}), 400

    angle = float(data_request['angle'])
    result = math.cos(math.radians(angle))
    return jsonify({'result': result})

@app.route('/api/tan', methods=['POST'])
def tan():
    data_request = request.get_json()
    if (not data_request or 'angle' not in data_request):
        return jsonify({'error': 'Invalid input'}), 400

    angle = float(data_request['angle'])
    result = math.tan(math.radians(angle))
    return jsonify({'result': result})

@app.route('/api/logarithm', methods=['POST'])
def logarithm():
    data_request = request.get_json()
    if (not data_request or 'number' not in data_request or
            'base' not in data_request):
        return jsonify({'error': 'Invalid input'}), 400

    number = float(data_request['number'])
    base = float(data_request['base'])
    if number <= 0 or base <= 1:
        return jsonify({'error': 'Logarithm is not defined for the given input'}), 400
    result = math.log(number, base)
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
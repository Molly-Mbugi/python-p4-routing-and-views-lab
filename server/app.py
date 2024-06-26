from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print to console (for debugging purposes)
    return parameter  # Return as response

@app.route('/count/<int:parameter>')
def count(parameter):
    return "\n".join(str(i) for i in range(parameter))

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
        operation_str = '+'
    elif operation == '-':
        result = num1 - num2
        operation_str = '-'
    elif operation == '*':
        result = num1 * num2
        operation_str = '*'
    elif operation == 'div':
        result = num1 / num2
        operation_str = 'div'
    elif operation == '%':
        result = num1 % num2
        operation_str = '%'
    else:
        return "Invalid operation!"

    return f"The result of {num1} {operation_str} {num2} is {result}"

if __name__ == '__main__':
    app.run(port=5555)




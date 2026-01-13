from flask import Flask

app = Flask(__name__)

# -------------------------------
# Index View
# -------------------------------
@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# -------------------------------
# Print String View
# -------------------------------
@app.route("/print/<string:param>")
def print_string(param):
    print(param)  # prints to console
    return param  # return plain text, no HTML


# -------------------------------
# Count View
# -------------------------------
from flask import Response

@app.route("/count/<int:param>")
def count(param):
    # join numbers with newline and add final newline at the end
    numbers = "\n".join(str(i) for i in range(param)) + "\n"
    return Response(numbers, mimetype="text/plain")

# -------------------------------
# Math View
# -------------------------------
@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    try:
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "div":
            result = num1 / num2   # returns float
        elif operation == "%":
            result = num1 % num2
        else:
            return "Invalid operation. Use +, -, *, div, or %", 400

        return str(result)  # return plain text
    except Exception as e:
        return f"Error: {e}", 500

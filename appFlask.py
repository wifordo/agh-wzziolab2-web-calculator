from flask import Flask, request, jsonify
from calculator import Calculator  # import z pliku calculator.py

app = Flask(__name__)

@app.route('/calculate')
def calculate():
    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)

    if op is None or arg1 is None or arg2 is None:
        return jsonify({"error": "Missing or invalid parameters. Use ?op=&arg1=&arg2="}), 400

    calc = Calculator(arg1, arg2)

    op = op.lower()
    try:
        if op == 'sum':
            result = calc.sum()
        elif op == 'subtract':
            result = calc.subtract()
        elif op == 'multiply':
            result = calc.multiply()
        elif op == 'divide':
            result = calc.divide()
        else:
            return jsonify({"error": f"Unknown operation '{op}'"}), 400
    except ZeroDivisionError:
        return jsonify({"error": "Division by zero"}), 400

    return jsonify({"op": op, "arg1": arg1, "arg2": arg2, "result": result})

if __name__ == '__main__':
    app.run(debug=True)

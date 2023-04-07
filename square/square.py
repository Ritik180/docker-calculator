from flask import Flask, request

app = Flask(__name__)

@app.route('/square')
def square():
    number = request.args.get('number', type=int)
    return str(number ** 2)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

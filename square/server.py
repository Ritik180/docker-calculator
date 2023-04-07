from flask import Flask

app = Flask(__name__)

@app.route('/square/<int:num>')
def square(num):
    return f'The square of {num} is {num**2}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

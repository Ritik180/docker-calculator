from flask import Flask

app = Flask(__name__)

@app.route('/cube/<int:num>')
def cube(num):
    return f'The cube of {num} is {num**3}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

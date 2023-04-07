from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/square', methods=['POST'])
def square():
    number = int(request.form['number'])
    result = number ** 2
    return render_template('result.html', operation='Square', number=number, result=result)

@app.route('/cube', methods=['POST'])
def cube():
    number = int(request.form['number'])
    result = number ** 3
    return render_template('result.html', operation='Cube', number=number, result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0

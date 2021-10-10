from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template("index.html", number1=9, number2=99)

@app.route('/multiply')
def multiply():
    n1, n2=7,77
    n3=n1*n2
    return render_template("body.html", value1=n1, value2=n2, value3=n3)

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=80)


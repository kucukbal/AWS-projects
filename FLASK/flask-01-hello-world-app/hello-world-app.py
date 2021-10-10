from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello ():
    return "hello world from kucukbal"

@app.route('/second')
def second ():
    return "this is the second page"


@app.route('/third/subthird')
def third ():
    return "this is the sub page of third page"


@app.route('/fourth/<string:id>')
def fourth (id):
    return f"id of this page is {id}"
    


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=80)

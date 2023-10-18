from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! I am blue'

@app.route('/about')
def about():
    return 'This is blue Environment.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

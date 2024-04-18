from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to my basic web application 1234!'

@app.route('/about')
def about():
    return 'This is a simple web application created with Flask.'

if __name__ == '__main__':
    # Start the Flask development server
    app.run(host='0.0.0.0', port=5000, debug=True)

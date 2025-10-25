from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from my Docker Container! 🐳"

if __name__ == '__main__':
    #0.0.0.0 so server is available outside the container
    app.run(host='0.0.0.0', port=5000)
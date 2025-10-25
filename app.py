from flask import Flask
from redis import Redis

app = Flask(__name__)

db = Redis(host='db', port=6379, decode_responses=True)

@app.route('/')
def hello():
    count = db.incr('hits')
    return f"Hello from Docker! 🐳 This page has been visited {count} times."

if __name__ == '__main__':
    #0.0.0.0 so server is available outside the container
    app.run(host='0.0.0.0', port=5000)
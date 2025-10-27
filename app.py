# app.py
from flask import Flask
from redis import Redis

app = Flask(__name__)
db = Redis(host='db', port=6379, decode_responses=True)

@app.route('/')
def hello():
    count = db.incr('hits')
    # --- THIS IS THE LINE TO CHANGE ---
    return f"Hello from v2.0! 🚀 This page has been visited {count} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
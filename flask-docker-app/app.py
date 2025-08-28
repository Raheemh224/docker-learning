import os
from flask import Flask
import redis

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST')
redis_port = int(os.getenv('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port)

@app.route("/")
def home():
    return "My First Dockerised Flask App"

@app.route("/count")
def count():
    r.incr("visit_count")

    count = r.get("visit_count")
    return f"Page visited {count} times"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
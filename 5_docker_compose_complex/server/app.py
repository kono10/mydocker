from flask import Flask
import redis
import os

app = Flask(__name__)

# service name in docker-compose.yml
r = redis.Redis(host=os.environ["REDIS_HOST"])


@app.route("/")
def hello_world():
    if r.exists("visits"):
        visits = int(r.get("visits")) + 1
    else:
        visits = int(1)
    r.set("visits", visits)

    return f"<h1>Hello, World! Number of Visits!!! {int(r.get('visits'))}</h1>"


if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")

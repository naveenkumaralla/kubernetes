from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello from v1.1! Served by container: {socket.gethostname()}\n"

app.run(host="0.0.0.0", port=5000)

# app/app.py
from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def hello():
    return "Selam dünya v2."

@app.route("/health")
def health():
    # livenessProbe => 200 OK
    return Response("healthy\n", mimetype="text/plain")

@app.route("/ready")
def ready():
    # readinessProbe => 200 OK
    return Response("ready\n", mimetype="text/plain")

if __name__ == "__main__":
    # K8s servis/prob'ları 8080'e bakıyor
    app.run(host="0.0.0.0", port=8080)

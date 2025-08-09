# Devolver JSON en Flask
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/data")
def data():
    return jsonify({"mensaje": "Hola API"})

if __name__ == "__main__":
    app.run(debug=True)

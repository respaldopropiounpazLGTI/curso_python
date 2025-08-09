# Rutas y métodos en Flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola, Flask!"

@app.route("/usuarios", methods=["GET"]) # methods especifica el tipo de solicitud aceptada.
def obtener_usuarios():
    return [{"id": 1, "nombre": "Ana"}]


if __name__ == "__main__":
    app.run(debug=True)

# cd ruta-del-proyecto
# code app.py
# flask --app app run
from flask import Flask, jsonify, request
import csv
import os

app = Flask(__name__)

DATA_FILE = "data.csv"

# Función auxiliar: cargar datos desde CSV
def cargar_datos():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, mode="r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        datos = [dict(row) for row in lector]
        # Convertir id y precio a numérico
        for d in datos:
            d["id"] = int(d["id"])
            d["precio"] = float(d["precio"])
        return datos

# Función auxiliar: guardar datos en CSV
def guardar_datos(datos):
    with open(DATA_FILE, mode="w", newline="", encoding="utf-8") as f:
        campos = ["id", "nombre", "precio"]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for d in datos:
            escritor.writerow(d)

# Endpoint inicial
@app.route("/api/data", methods=["GET"])
def data():
    return jsonify({"mensaje": "Hola API con CSV"})

# GET - Listar todos
@app.route("/api/items", methods=["GET"])
def listar_items():
    datos = cargar_datos()
    return jsonify(datos)

# GET - Obtener uno
@app.route("/api/items/<int:item_id>", methods=["GET"])
def obtener_item(item_id):
    datos = cargar_datos()
    for item in datos:
        if item["id"] == item_id:
            return jsonify(item)
    return jsonify({"error": "Item no encontrado"}), 404

# POST - Crear
@app.route("/api/items", methods=["POST"])
def agregar_item():
    datos = cargar_datos()
    nuevo_item = request.get_json()

    if not nuevo_item.get("nombre") or "precio" not in nuevo_item:
        return jsonify({"error": "Campos 'nombre' y 'precio' son obligatorios"}), 400

    nuevo_item["id"] = datos[-1]["id"] + 1 if datos else 1
    nuevo_item["precio"] = float(nuevo_item["precio"])
    datos.append(nuevo_item)
    guardar_datos(datos)
    return jsonify(nuevo_item), 201

# PUT - Actualizar
@app.route("/api/items/<int:item_id>", methods=["PUT"])
def actualizar_item(item_id):
    datos = cargar_datos()
    item_data = request.get_json()

    for item in datos:
        if item["id"] == item_id:
            item.update({
                "nombre": item_data.get("nombre", item["nombre"]),
                "precio": float(item_data.get("precio", item["precio"]))
            })
            guardar_datos(datos)
            return jsonify(item)
    return jsonify({"error": "Item no encontrado"}), 404

# DELETE - Eliminar
@app.route("/api/items/<int:item_id>", methods=["DELETE"])
def eliminar_item(item_id):
    datos = cargar_datos()
    nuevos_datos = [item for item in datos if item["id"] != item_id]

    if len(nuevos_datos) == len(datos):
        return jsonify({"error": "Item no encontrado"}), 404

    guardar_datos(nuevos_datos)
    return jsonify({"mensaje": f"Item {item_id} eliminado correctamente"})

if __name__ == "__main__":
    # Crear archivo CSV si no existe
    if not os.path.exists(DATA_FILE):
        guardar_datos([])
    app.run(debug=True)

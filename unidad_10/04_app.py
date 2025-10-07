# cd ruta-del-proyecto
# code app.py
# flask --app app run
from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"

# Función auxiliar: cargar datos
def cargar_datos():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# Función auxiliar: guardar datos
def guardar_datos(datos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

# Endpoint inicial
@app.route("/", methods=["GET"])
def data():
    return jsonify({"mensaje": "Hola API"})

# GET - Listar todos los elementos
@app.route("/api/items", methods=["GET"])
def listar_items():
    datos = cargar_datos()
    # print(" -----datos[0] ------")
    # print(datos[0])
    return jsonify(datos)

# GET - Obtener un ítem por ID
@app.route("/api/items/<int:item_id>", methods=["GET"])
def obtener_item(item_id):
    # print("item_id ----")
    # print(item_id)
    datos = cargar_datos()
    for item in datos:
        if item["id"] == item_id:
            return jsonify(item)
    return jsonify({"error": "Item no encontrado"}), 404

# POST - Agregar un nuevo ítem
@app.route("/api/items", methods=["POST"])
def agregar_item():
    datos = cargar_datos()
    nuevo_item = request.get_json()

    if not nuevo_item.get("nombre"):
        return jsonify({"error": "El campo 'nombre' es obligatorio"}), 400

    # if datos:
    #     nuevo_item["id"] = datos[-1]["id"] + 1
    # else:
    #     nuevo_item["id"] = 1

    nuevo_item["id"] = datos[-1]["id"] + 1 if datos else 1
    datos.append(nuevo_item)
    guardar_datos(datos)
    return jsonify(nuevo_item), 201

# curl -X POST http://localhost:5000/api/items \
#   -H "Content-Type: application/json" \
#   -d '{"nombre": "Item nuevo", "precio": 15.0}'


# PUT - Actualizar un ítem por ID
@app.route("/api/items/<int:item_id>", methods=["PUT"])
def actualizar_item(item_id):
    datos = cargar_datos()
    item_data = request.get_json()

    for item in datos:
        if item["id"] == item_id:
            item.update(item_data)
            guardar_datos(datos)
            return jsonify(item)
    return jsonify({"error": "Item no encontrado"}), 404

# curl -X PUT http://localhost:5000/api/items/1 \
#   -H "Content-Type: application/json" \
#   -d '{"nombre": "Item actualizado", "precio": 12.0}'


# DELETE - Eliminar un ítem por ID
@app.route("/api/items/<int:item_id>", methods=["DELETE"])
def eliminar_item(item_id):
    datos = cargar_datos()
    datos_filtrados = [item for item in datos if item["id"] != item_id] # listas por comprensión 

    if len(datos) == len(datos_filtrados):
        return jsonify({"error": "Item no encontrado"}), 404

    guardar_datos(datos_filtrados)
    return jsonify({"mensaje": f"Item {item_id} eliminado correctamente"})

# curl -X DELETE http://localhost:5000/api/items/2

if __name__ == "__main__":
    # Si no existe el archivo, crear uno vacío
    if not os.path.exists(DATA_FILE):
        guardar_datos([])
    app.run(debug=True)

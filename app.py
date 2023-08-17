import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

frutas = [
    {"id": 1, "nombre": "Manzana", "precio": 1.0},
    {"id": 2, "nombre": "Plátano", "precio": 0.5},
]

verduras = [
    {"id": 1, "nombre": "Zanahoria", "precio": 0.3},
    {"id": 2, "nombre": "Tomate", "precio": 0.10},
    
]

# Obtener lista de frutas o agregar una nueva fruta
@app.route('/api/frutas', methods=['GET', 'POST'])
def lista_frutas():
    if request.method == 'GET':
        response = json.dumps(frutas, ensure_ascii=False)  # ensure_ascii=False para preservar caracteres especiales
        return response
    elif request.method == 'POST':
        nueva_fruta = {
            "id": len(frutas) + 1,
            "nombre": request.json.get("nombre"),
            "precio": request.json.get("precio")
        }
        frutas.append(nueva_fruta)
        return jsonify(nueva_fruta), 201

# Obtener detalles de una fruta, actualizar o eliminar
@app.route('/api/frutas/<int:fruta_id>', methods=['GET', 'PUT', 'DELETE'])
def detalle_fruta(fruta_id):
    fruta = next((fruta for fruta in frutas if fruta["id"] == fruta_id), None)
    if not fruta:
        return jsonify({"error": "Fruta no encontrada"}), 404

    if request.method == 'GET':
        return jsonify(fruta)
    elif request.method == 'PUT':
        fruta["nombre"] = request.json.get("nombre", fruta["nombre"])
        fruta["precio"] = request.json.get("precio", fruta["precio"])
        return jsonify(fruta)
    elif request.method == 'DELETE':
        frutas.remove(fruta)
        return jsonify({"mensaje": "Fruta eliminada"}), 204

# Obtener lista de verduras o agregar una nueva verdura
@app.route('/api/verduras', methods=['GET', 'POST'])
def lista_verduras():
    if request.method == 'GET':
        response = json.dumps(verduras, ensure_ascii=False)  # ensure_ascii=False para preservar caracteres especiales
        return response
    elif request.method == 'POST':
        nueva_verdura = {
            "id": len(verduras) + 1,
            "nombre": request.json.get("nombre"),
            "precio": request.json.get("precio")
        }
        verduras.append(nueva_verdura)
        return jsonify(nueva_verdura), 201

# Obtener detalles de una verdura, actualizar o eliminar
@app.route('/api/verduras/<int:verdura_id>', methods=['GET', 'PUT', 'DELETE'])
def detalle_verdura(verdura_id):
    verdura = next((verdura for verdura in verduras if verdura["id"] == verdura_id), None)
    if not verdura:
        return jsonify({"error": "Verdura no encontrada"}), 404

    if request.method == 'GET':
        return jsonify(verdura)
    elif request.method == 'PUT':
        verdura["nombre"] = request.json.get("nombre", verdura["nombre"])
        verdura["precio"] = request.json.get("precio", verdura["precio"])
        return jsonify(verdura)
    elif request.method == 'DELETE':
        verduras.remove(verdura)
        return jsonify({"mensaje": "Verdura eliminada"}), 204

if __name__ == '__main__':
    app.run(debug=True)

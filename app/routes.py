from flask import Blueprint, jsonify, request

bp = Blueprint('main', __name__)

tasks = []

@bp.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@bp.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "Título é obrigatório"}), 400
    task = {"id": len(tasks) + 1, "title": data["title"], "done": False}
    tasks.append(task)
    return jsonify(task), 201

@bp.route('/tasks/<int:task_id>', methods=['PUT'])
def mark_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return jsonify(task)
    return jsonify({"error": f"Tarefa com id {task_id} não encontrada"}), 404

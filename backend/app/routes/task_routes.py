from flask import Blueprint, request, jsonify
from app.services import task_service

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify(task_service.get_tasks())

@task_bp.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.json
    return jsonify(task_service.create_task(data["title"]))

@task_bp.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    return jsonify(task_service.delete_task(task_id))

@task_bp.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.json
    return jsonify(task_service.update_task(task_id, data["done"]))

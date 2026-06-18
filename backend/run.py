from flask import Flask
from app.routes.task_routes import task_bp
from app.db.db import db
from app.models.task import Task

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://admin:password@db:5432/taskdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql+psycopg2://admin:secret@db:5432/taskdb"
)

db.init_app(app)

app.register_blueprint(task_bp)

@app.route("/api/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

with app.app_context():
    db.create_all()
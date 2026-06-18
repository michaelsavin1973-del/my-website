from flask import Flask
from app.routes.task_routes import task_bp
from app.db.db import db
from app.models.task import Task

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

import os
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@db:5432/"
    f"{os.getenv('POSTGRES_DB')}"
)

db.init_app(app)

app.register_blueprint(task_bp)

@app.route("/api/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(host="0.0.0.0", port=5000)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name="default"):
    app = Flask(__name__)
    if config_name == "testing":
        app.config.from_object("config.TestConfig")
    else:
        app.config.from_object("config.Config")
    db.init_app(app)

    with app.app_context():
        from app import models

        db.create_all()

        from app.routes import task_bp

        app.register_blueprint(task_bp)

    return app

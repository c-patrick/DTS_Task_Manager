import pytest
from app import create_app, db
from app.models import User


@pytest.fixture
def app():
    app = create_app("testing")  # assumes you have a testing config
    app.config.update(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
            "WTF_CSRF_ENABLED": False,  # disable CSRF for form testing
        }
    )

    with app.app_context():
        db.create_all()
        # Add test user
        user = User(username="TestUser")
        db.session.add(user)
        db.session.commit()

    yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

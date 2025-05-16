from app import db
from app.models import User


def test_user_creation_success(client, app):
    response = client.post("/users", data={"name": "Alice"}, follow_redirects=True)

    assert response.status_code == 200
    assert b"User created successfully" in response.data

    with app.app_context():
        user = User.query.filter_by(username="Alice").first()
        assert user is not None
        assert user.username == "Alice"


def test_user_creation_duplicate(client, app):
    with app.app_context():
        user = User(username="Bob")
        db.session.add(user)
        db.session.commit()

    response = client.post("/users", data={"name": "Bob"}, follow_redirects=True)

    assert response.status_code == 200
    assert b"User already exists." in response.data


def test_user_creation_empty_name(client):
    response = client.post("/users", data={"username": ""}, follow_redirects=True)

    assert response.status_code == 200
    assert b"This field is required." in response.data


def test_user_list_display(client, app):
    with app.app_context():
        db.session.add_all([User(username="Charlie"), User(username="Dana")])
        db.session.commit()

    response = client.get("/users")
    assert response.status_code == 200
    assert b"Charlie" in response.data
    assert b"Dana" in response.data


def test_user_deletion(client, app):
    with app.app_context():
        user = User(username="Eve")
        db.session.add(user)
        db.session.commit()
        user_id = user.id

    response = client.post(f"/users/delete/{user_id}", follow_redirects=True)

    assert response.status_code == 200
    assert b"User deleted" in response.data

    with app.app_context():
        user = User.query.get(user_id)
        assert user is None

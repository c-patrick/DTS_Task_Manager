from app.models import Task


def test_create_task_success(client, app):
    response = client.post(
        "/",
        data={
            "title": "New Task",
            "description": "A task description",
            "priority": "High",
            "due_date": "2025-12-31",
            "user_id": 1,
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Task created successfully" in response.data

    with app.app_context():
        task = Task.query.filter_by(title="New Task").first()
        assert task is not None
        assert task.user_id == 1


def test_create_task_missing_user(client):
    response = client.post(
        "/",
        data={
            "title": "Invalid Task",
            "description": "Missing user",
            "priority": "Medium",
            "due_date": "2025-12-31",
            "user_id": -1,
        },
        follow_redirects=True,
    )

    assert b"Please select a valid user." in response.data


def test_create_task_missing_title(client):
    response = client.post(
        "/",
        data={
            "title": "",
            "description": "No title",
            "priority": "Low",
            "due_date": "2025-12-31",
            "user_id": 1,
        },
        follow_redirects=True,
    )

    assert b"This field is required." in response.data


def test_get_task_by_id(client, app):
    with app.app_context():
        from app.models import User, Task, db

        user = User(username="testuser")
        db.session.add(user)
        db.session.commit()

        task = Task(
            title="Test Task",
            description="This is a test task.",
            user_id=user.id,
            due_date=None,
            priority=None,
        )
        db.session.add(task)
        db.session.commit()

        task_id = task.id

    response = client.get(f"/task/{task_id}")

    assert response.status_code == 200
    # Check that the response contains the task title and username
    assert b"Test Task" in response.data
    assert b"testuser" in response.data


def test_get_task_not_found(client):
    # Request a task id that does not exist
    response = client.get("/task/99999")
    assert response.status_code == 404

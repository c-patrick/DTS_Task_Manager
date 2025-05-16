# HMCTS Developer Challenge – Task Management App

A simple task management system built using **Flask**, **SQLAlchemy**, and **Bootstrap** as part of the [HMCTS Developer Challenge](https://github.com/hmcts/dts-developer-challenge).


## Features

- User management (add and list users)
- Task creation with validation (via Flask-WTF)
- Task editing with flash feedback
- User filtering on task list
- Task filtering by ID
- Bootstrap-based responsive frontend
- Collapsible task creation form with toggling button label
- Auto-dismiss flash messages with progress bar timer
- Basic unit tests using `pytest`


## Tech Stack

- Python 3.9+
- Flask
- SQLAlchemy
- Flask-WTF
- Bootstrap 5
- SQLite


## Setup Instructions

### 1) Clone the Repository

```bash
git clone https://github.com/yourusername/hmcts-task-app.git
cd hmcts-task-app
```

### 2) Set Up a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3) Install Dependencies
```bash
pip install -r requirements.txt
```
### 4) Set Up the Database
```bash
python
>>> from app import db
>>> db.create_all()
>>> exit()
```

### 5) Run the Application
```bash
flask run
```


## Running Tests
```bash
pytest
```
Tests cover user creation, duplicate prevention, and form validation.


## Project Structure
```
.
├── app
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   └── templates
│       ├── base.html
│       ├── edit.html
│       ├── index.html
│       ├── task_detail.html
│       └── users.html
├── config.py
├── instance
│   └── tasks.db
├── README.md
├── requirements.txt
├── run.py
└── tests
    ├── __init__.py
    ├── conftest.py
    ├── test_tasks.py
    └── test_users.py
```

## API Documentation
API documentation can be found in `Endpoints.md`.
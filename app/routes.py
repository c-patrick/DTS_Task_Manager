from flask import Blueprint, request, render_template, redirect, url_for, flash, jsonify
from app.forms import TaskForm, UserForm
from app.models import Task, User
from app import db
from datetime import datetime

task_bp = Blueprint("task_bp", __name__)


@task_bp.route("/", methods=["GET", "POST"])
def index():
    form = TaskForm()
    users = User.query.all()
    form.user_id.choices = [(-1, "Select a user...")] + [
        (user.id, user.username) for user in users
    ]

    # Get filter values from query params
    filter_user_id = request.args.get("user_id", type=int, default=-1)
    filter_task_id = request.args.get("task_id", type=int)

    # Apply filtering logic
    query = Task.query

    if filter_task_id:
        query = query.filter(Task.id == filter_task_id)
    else:
        if filter_user_id != -1:
            query = query.filter(Task.user_id == filter_user_id)

    tasks = query.order_by(Task.due_date.asc().nulls_last()).all()

    if form.validate_on_submit():
        if form.user_id.data == -1:
            flash("Please select a valid user.", "danger")
        else:
            new_task = Task(
                title=form.title.data,
                description=form.description.data,
                due_date=form.due_date.data,
                priority=form.priority.data or None,
                user_id=form.user_id.data,
            )
            db.session.add(new_task)
            db.session.commit()
            flash("Task created successfully!", "success")
            return redirect(url_for("task_bp.index"))

    users = User.query.all()
    return render_template(
        "index.html",
        tasks=tasks,
        form=form,
        users=users,
        filter_user_id=filter_user_id,
        filter_task_id=filter_task_id,
    )


@task_bp.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    form = TaskForm(obj=task)  # populate form with existing data
    users = User.query.all()
    form.user_id.choices = [(user.id, user.username) for user in users]

    if form.validate_on_submit():
        task.title = form.title.data
        task.user_id = form.user_id.data
        task.description = form.description.data
        task.due_date = form.due_date.data
        task.priority = form.priority.data or None

        db.session.commit()
        flash("Task updated successfully!", "success")
        return redirect(url_for("task_bp.index"))

    return render_template("edit.html", form=form, task=task)


@task_bp.route("/task/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return render_template("task_detail.html", task=task)


@task_bp.route("/api/task/<int:task_id>", methods=["GET"])
def get_task_json(task_id):
    task = Task.query.get_or_404(task_id)
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "due_date": task.due_date.isoformat() if task.due_date else None,
        "priority": task.priority,
        "user_id": task.user_id,
        "username": task.user.username,
    }


@task_bp.route("/users", methods=["GET", "POST"])
def manage_users():
    form = UserForm()
    users = User.query.order_by(User.id.asc()).all()

    if form.validate_on_submit():  # Create a new users
        new_user = User(username=form.name.data)
        db.session.add(new_user)
        db.session.commit()
        flash("User created successfully", "success")
        return redirect(url_for("task_bp.manage_users"))

    return render_template("users.html", users=users, form=form)


@task_bp.route("/users/delete/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("User deleted", "warning")
    return redirect(url_for("task_bp.manage_users"))


@task_bp.route("/complete/<int:task_id>")
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.completed == True:
        task.completed = False
    else:
        task.completed = True
    db.session.commit()
    return redirect(url_for("task_bp.index"))


@task_bp.route("/delete/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("task_bp.index"))


@task_bp.errorhandler(404)
def handle_404_error(e):
    # Check if request path starts with /api/
    if request.path.startswith("/api/"):
        return jsonify({"message": str(e)}), 404
    else:
        # Default HTML 404 page
        return e

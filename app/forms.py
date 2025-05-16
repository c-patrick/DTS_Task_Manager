from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, ValidationError
from flask import flash
from app.models import User


class TaskForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=100)])
    user_id = SelectField("Assigned To", coerce=int, validators=[DataRequired()])
    description = TextAreaField("Description", validators=[Optional(), Length(max=500)])
    due_date = DateField("Due Date", format="%Y-%m-%d", validators=[Optional()])
    priority = SelectField(
        "Priority",
        choices=[("", "None"), ("Low", "Low"), ("Medium", "Medium"), ("High", "High")],
        validators=[Optional()],
    )
    submit = SubmitField("Submit")


class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Add User")

    def validate_name(self, field):
        if User.query.filter_by(username=field.data).first():
            # flash("User already exists.", "danger")
            raise ValidationError("User already exists.")

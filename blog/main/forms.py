from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email


def strip_filter(x):
    return x.strip() if x else None


class MemberForm(Form):
    firstname = StringField(
        "First Name",
        validators=[DataRequired(), Length(min=2, max=30)],
        filters=[strip_filter]
    )
    lastname = StringField(
        "Last Name",
        validators=[DataRequired(), Length(min=1, max=30)],
        filters=[strip_filter]
    )
    email = StringField(
        "Email", validators=[DataRequired(), Email()], filters=[strip_filter]
    )
    phone = StringField(
        "Phone",
        validators=[
            DataRequired(),
            Length(min=10, max=13, message="Enter your valid mobile number"),
        ],
        filters=[strip_filter],
        render_kw={
            "type": "number",
            "autocomplete": "off",
            "onfocus": "this.removeAttribute('readonly');",
        }
    )
    usn = StringField(
        "USN",
        validators=[DataRequired(), Length(min=2, max=30)],
        filters=[strip_filter]
    )
    branch = SelectField(
        "Branch",
        choices=[
            ("ECE", "Electronics & Communication Engineering"),
            ("CSE", "Computer Science Engineering"),
            ("EEE", "Electrical & Electronics Engineering"),
            ("ISE", "Information Science Engineering"),
            ("MECH", "Mechanical Engineering"),
            ("Civil", "Civil Engineering"),
            ("IPE", "Industrial and Production Engineering")
        ]
    )
    semester = SelectField(
        "semester",
        choices=[
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5", "5"),
            ("6", "6"),
            ("7", "7"),
            ("8", "8")
        ]
    )
    submit = SubmitField("Become a member")


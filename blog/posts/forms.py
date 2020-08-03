from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


def strip_filter(x): return x.rstrip() if x else None


class PostForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[
                            DataRequired()], filters=[strip_filter])
    submit = SubmitField('Post')

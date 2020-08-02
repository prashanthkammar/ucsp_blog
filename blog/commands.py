import click
from flask.cli import with_appcontext

from blog.extensions import db
from blog.models import User


@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()

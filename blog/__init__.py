from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import MigrateCommand
from blog.config import Config
from blog.commands import create_tables
from blog.extensions import db, login_manager, mail, admin, migrate, manager

login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    admin.init_app(app)
    migrate.init_app(app, db)
    manager(app)

    from blog.users.routes import users
    from blog.posts.routes import posts
    from blog.main.routes import main
    from blog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    app.cli.add_command(create_tables)
    manager.add_command('db', MigrateCommand)

    return app

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = "mysecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'user.login'

from innercircleproj.core.views import core_blueprint
from innercircleproj.error_pages.handlers import error_bp
from innercircleproj.users.views import user_bp
from innercircleproj.blogposts.views import post_bp

app.register_blueprint(core_blueprint)
app.register_blueprint(error_bp)
app.register_blueprint(user_bp)
app.register_blueprint(post_bp)

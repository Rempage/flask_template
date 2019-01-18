from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from flask_uploads import UploadSet, configure_uploads, ALL
from config import config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'wap.login'
login_manager.login_message = "账号登录失效"
csrf = CSRFProtect()

fileUpload = UploadSet('files', ALL)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    configure_uploads(app, fileUpload)

    from .wap import wap as wap_blueprint
    app.register_blueprint(wap_blueprint)

    from .www import www as www_blueprint
    app.register_blueprint(www_blueprint, url_prefix='/www')

    return app
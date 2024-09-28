from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config


# Renombrar db a database
database = SQLAlchemy()

# Inicializar LoginManager
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar la base de datos y el sistema de login
<<<<<<< HEAD
    database.init_app(app)
=======
    database.init_app(app)  # Cambiado a 'database'
>>>>>>> bea17413e07e1b0f4a193a8a83213fef4bdd08ac

    login_manager.init_app(app)
    login_manager.login_view = 'users.login'
    login_manager.login_message = None

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Registrar Blueprints
    from .routes_users import users_blueprint
    from .routes_links import links_blueprint
    from .routes_listas import listas_blueprint
<<<<<<< HEAD
    from .routes_api import api_blueprint
=======
>>>>>>> bea17413e07e1b0f4a193a8a83213fef4bdd08ac

    app.register_blueprint(users_blueprint, url_prefix='/')
    app.register_blueprint(links_blueprint, url_prefix='/')
    app.register_blueprint(listas_blueprint, url_prefix='/')
<<<<<<< HEAD
    app.register_blueprint(api_blueprint, url_prefix='/api')
=======
>>>>>>> bea17413e07e1b0f4a193a8a83213fef4bdd08ac

    return app

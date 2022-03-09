from flask import Flask
from flask_migrate import Migrate

from .config import app_config
from .models import db
from .views.CategoryVIew import category_api as category_blueprint


def create_app(env_name):
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    migrate = Migrate(app=app, db=db)
    db.init_app(app)
    app.register_blueprint(category_blueprint, url_prefix='/categories')
    @app.route('/', methods=['GET'])
    def index():
        return 'It works!'

    return app
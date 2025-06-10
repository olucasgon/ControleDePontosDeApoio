from flask import Flask
from flask_restful import Api
from src.routes.Endpoints import initialize_endpoints
from src.entities.Base import db

def create_app() -> Flask:

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:54321@localhost:3306/controlepontoapoio'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    api = Api(app, prefix="/api")
    initialize_endpoints(api)

    return app
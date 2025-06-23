from flask import Flask
from flask_restful import Api
from src.routes.Endpoints import initialize_endpoints
from src.entities.Base import db

def create_app() -> Flask:

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:54321@localhost:5432/controlepontoapoio'

    db.init_app(app)

    api = Api(app, prefix="/api")
    initialize_endpoints(api)

    return app
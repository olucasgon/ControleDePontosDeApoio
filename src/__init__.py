from flask import Flask
from flask_restful import Api


def create_app() -> Flask:

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:54321@localhost:3306/controlepontoapoio'

    #db.init_app(app)

    api = Api(app, prefix="/api")
    #initialize_endpoints(api)

    return app
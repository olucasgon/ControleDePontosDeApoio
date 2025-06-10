import re
from flask_restful import Resource, abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.services.PontoApoioService import getPontosApoio, getPontoApoio, addPontoApoio, updatePontoApoio, deletePontoApoio

class PontoApoioResponseSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
    latitude = fields.Float()
    longitude = fields.Float()

class PontoApoioRequestSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
    latitude = fields.Float()
    longitude = fields.Float()

    @validates("nome")
    def validate_name(self, value):
        if not re.match(pattern=r"^[a-zA-Z0-9_\s]+$", string=value):
            raise ValidationError(
                "Value must contain only alphanumeric and underscore characters."
            )
        
    @validates('latitude')
    def validate_latitude(self, value):
        if not (-90 <= value <= 90):
            raise ValidationError("Latitude must be between -90 and 90 degrees.")
    
    @validates('longitude')
    def validate_longitude(self, value):
        if not (-180 <= value <= 180):
            raise ValidationError("Longitude must be between -180 and 180 degrees.")
        
class PontoApoioItem(MethodResource, Resource):
    @marshal_with(PontoApoioResponseSchema)
    def get(self, ponto_apoio_id):
        try:
            ponto_apoio = getPontoApoio(ponto_apoio_id)
            if ponto_apoio is None:
                abort(404, message="Ponto de Apoio not found")
            return ponto_apoio, 200
        except OperationalError:
            abort(500, message="Database connection error")

    def delete(self, ponto_apoio_id):
        try:
            deletePontoApoio(ponto_apoio_id)
            return "Ponto de Apoio deleted successfully", 204
        except UnmappedInstanceError:
            abort(404, message="Ponto de Apoio not found")
        except (OperationalError, IntegrityError):
            abort(500, message="Database error")

    @use_kwargs(PontoApoioRequestSchema, location={"form"})
    @marshal_with(PontoApoioResponseSchema)
    def put(self, ponto_apoio_id, **kwargs):
        try:
            ponto_apoio = updatePontoApoio(ponto_apoio_id, **kwargs)
            return ponto_apoio, 200
        except(OperationalError, IntegrityError):
            abort(500, message="Database error")
class PontoApoioList(MethodResource, Resource):
    @marshal_with(PontoApoioResponseSchema(many=True))
    def get(self):
        try:
            ponto_apoios = getPontosApoio()
            return ponto_apoios, 200
        except OperationalError:
            abort(500, message="Database connection error")
    
    @use_kwargs(PontoApoioRequestSchema, location={"form"})
    @marshal_with(PontoApoioResponseSchema)
    def post(self, **kwargs):
        try:
            ponto_apoio = addPontoApoio(**kwargs)
            return ponto_apoio, 201
        except IntegrityError:
            abort(400, message="Ponto de Apoio already exists")
        except OperationalError:
            abort(500, message="Database error")
        except ValidationError as e:
            abort(400, message=str(e))

    
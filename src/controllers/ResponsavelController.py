import re
from flask_restful import Resource, abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.services.ResponsavelService import getResponsaveis, getResponsavel, addResponsavel, updateResponsavel, deleteResponsavel
class ResponsavelResponseSchema(Schema):
    id = fields.Int()
    codigo = fields.Str()
    pessoa_id = fields.Int()
    pontoapoio_id = fields.Int()

class ResponsavelRequestSchema(Schema):
    id = fields.Int()
    codigo = fields.Str()
    pessoa_id = fields.Int()
    pontoapoio_id = fields.Int()

    @validates("pessoa_id")
    def validate_pessoa_id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValidationError("Pessoa ID must be a positive integer.")
    
    @validates("pontoapoio_id")
    def validate_pontoapoio_id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValidationError("Ponto Apoio ID must be a positive integer.")

class ResponsavelItem(MethodResource, Resource):
    @marshal_with(ResponsavelResponseSchema)
    def get(self, responsavel_id):
        try:
            responsavel = getResponsavel(responsavel_id)
            if responsavel is None:
                abort(404, message="Responsável not found")
            return responsavel, 200
        except OperationalError:
            abort(500, message="Database connection error")

    def delete(self, responsavel_id):
        try:
            deleteResponsavel(responsavel_id)
            return "Responsável deleted successfully", 204
        except UnmappedInstanceError:
            abort(404, message="Responsável not found")
        except (OperationalError, IntegrityError):
            abort(500, message="Database error")

    @use_kwargs(ResponsavelRequestSchema, location="json")
    @marshal_with(ResponsavelResponseSchema)
    def put(self, responsavel_id, **kwargs):
        try:
            updated_responsavel = updateResponsavel(responsavel_id, **kwargs)
            return updated_responsavel, 200
        except ValidationError as e:
            abort(400, message=str(e))
        except (OperationalError, IntegrityError):
            abort(500, message="Database error")

class ResponsavelList(MethodResource, Resource):
    @marshal_with(ResponsavelResponseSchema(many=True))
    def get(self):
        try:
            responsaveis = getResponsaveis()
            return responsaveis, 200
        except OperationalError:
            abort(500, message="Database connection error")

    @use_kwargs(ResponsavelRequestSchema, location="json")
    @marshal_with(ResponsavelResponseSchema)
    def post(self, **kwargs):
        try:
            responsavel = addResponsavel(**kwargs)
            return responsavel, 201
        except IntegrityError:
            abort(400, message="Responsável already exists")
        except OperationalError:
            abort(500, message="Database error")
        except ValidationError as e:
            abort(400, message=str(e))
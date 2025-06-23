import re
from flask_restful import Resource, abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.services.RecursoService import getRecursos, getRecurso, addRecurso, updateRecurso, deleteRecurso


class RecursoResponseSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
    quantidade = fields.Int()
    pontoapoio_id = fields.Int()
    

class RecursoRequestSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
    quantidade = fields.Int()
    pontoapoio_id = fields.Int()

    @validates("nome")
    def validate_nome(self, value):
        if not re.match(pattern=r"^[a-zA-Z0-9_\s]+$", string=value):
            raise ValidationError(
                "Value must contain only alphanumeric and underscore characters."
            )
    
    @validates('quantidade')
    def validate_quantidade(self, value):
        if value < 0:
            raise ValidationError("Quantidade must be a non-negative integer.")
        
    @validates('pontoapoio_id')
    def validate_pontoapoio_id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValidationError("Ponto Apoio ID must be a positive integer.")
        
class RecursoItem(MethodResource, Resource):
    @marshal_with(RecursoResponseSchema)
    def get(self, recurso_id):
        try:
            recurso = getRecurso(recurso_id)
            if recurso is None:
                abort(404, message="Recurso not found")
            return recurso, 200
        except OperationalError:
            abort(500, message="Database connection error")

    def delete(self, recurso_id):
        try:
            deleteRecurso(recurso_id)
            return 'Recurso Deletado com Sucesso', 204
        except UnmappedInstanceError:
            abort(404, message="Recurso not found")
        except (OperationalError, IntegrityError):
            abort(500, message="Database connection error")

    @use_kwargs(RecursoRequestSchema, location="json")
    @marshal_with(RecursoResponseSchema)
    def put(self, recurso_id, **kwargs):
        try:
            updated_recurso = updateRecurso(recurso_id, **kwargs)
            if updated_recurso is None:
                abort(404, message="Recurso not found")
            return updated_recurso, 200
        except ValidationError as e:
            abort(400, message=str(e))
        except (OperationalError, IntegrityError):
            abort(500, message="Database connection error")
    
class RecursoList(MethodResource, Resource):
    @marshal_with(RecursoResponseSchema(many=True))
    def get(self):
        try:
            recursos = getRecursos()
            return recursos, 200
        except OperationalError:
            abort(500, message="Database connection error")

    @use_kwargs(RecursoRequestSchema, location="json")
    @marshal_with(RecursoResponseSchema)
    def post(self, **kwargs):
        try:
            recurso = addRecurso(**kwargs)
            return recurso, 201
        except ValidationError as e:
            abort(400, message=str(e))
        except (OperationalError, IntegrityError):
            abort(500, message="Database connection error")
            

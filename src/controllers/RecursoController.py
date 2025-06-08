from flask_restful import Resource, abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.services.RecursoService import getRecursos,getRecurso,addRecurso,updateRecurso,deleteRecurso

class RecursoSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    quantidade = fields.Int(required=True)
    pontoapoio_id = fields.Int(required=True)

    @validates('nome')
    def validate_nome(self, value):
        if not value.strip():
            raise ValidationError("Nome não pode estar vazio.")
        
    @validates('quantidade')
    def validate_quantidade(self, value):
        if value < 0:
            raise ValidationError("Quantidade não pode ser negativa.")


class RecursoItem(MethodResource, Resource):
    @marshal_with(RecursoSchema)
    def get(self, recurso_id):
        try:
            recurso = getRecurso(recurso_id)
            if not recurso:
                abort(404, message="Recurso não encontrado.")
            return recurso, 200
        except OperationalError:
            abort(500, message="Erro interno no servidor.")

    def delete(self, recurso_id):
        try:
            deleteRecurso(recurso_id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Recurso não encontrado.")
        except (OperationalError, IntegrityError):
            abort(500, message="Erro interno no servidor.")

    @use_kwargs(RecursoSchema, location="form")
    @marshal_with(RecursoSchema)
    def put(self, recurso_id, **kwargs):
        try:
            recurso = updateRecurso(id=recurso_id, **kwargs)
            return recurso, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Erro interno no servidor.")


class RecursoList(MethodResource, Resource):
    @marshal_with(RecursoSchema(many=True))
    def get(self):
        try:
            return getRecursos(), 200
        except OperationalError:
            abort(500, message="Erro interno no servidor.")

    @use_kwargs(RecursoSchema, location="form")
    @marshal_with(RecursoSchema)
    def post(self, **kwargs):
        try:
            recurso = addRecurso(**kwargs)
            return recurso, 201
        except IntegrityError as err:
            abort(400, message=f"Erro de integridade: {str(err.orig)}")
        except OperationalError:
            abort(500, message="Erro interno no servidor.")

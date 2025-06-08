from flask_restful import Resource, abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields, validates, ValidationError
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.services.RegistroEntradaService import get_registros_entrada, get_registro_entrada, add_registro_entrada, update_registro_entrada,delete_registro_entrada

class RegistroEntradaSchema(Schema):
    id = fields.Int(dump_only=True)
    pessoa_id = fields.Int(required=True)
    pontoapoio_id = fields.Int(required=True)
    entrada = fields.DateTime(required=True, format='%Y-%m-%d %H:%M:%S')
    saida = fields.DateTime(allow_none=True, format='%Y-%m-%d %H:%M:%S')

    @validates('entrada')
    def validate_entrada(self, value):
        if value is None:
            raise ValidationError("A data de entrada é obrigatória.")


class RegistroEntradaItem(MethodResource, Resource):
    @marshal_with(RegistroEntradaSchema)
    def get(self, registro_id):
        try:
            registro = get_registro_entrada(registro_id)
            if not registro:
                abort(404, message="Registro não encontrado.")
            return registro, 200
        except OperationalError:
            abort(500, message="Erro interno no servidor.")

    def delete(self, registro_id):
        try:
            delete_registro_entrada(registro_id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Registro não encontrado.")
        except (OperationalError, IntegrityError):
            abort(500, message="Erro interno no servidor.")

    @use_kwargs(RegistroEntradaSchema, location="form")
    @marshal_with(RegistroEntradaSchema)
    def put(self, registro_entrada_id, **kwargs):
        try:
            registro = update_registro_entrada(id=registro_entrada_id, **kwargs)
            return registro, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Erro interno no servidor.")


class RegistroEntradaList(MethodResource, Resource):
    @marshal_with(RegistroEntradaSchema(many=True))
    def get(self):
        try:
            return get_registros_entrada(), 200
        except OperationalError:
            abort(500, message="Erro interno no servidor.")

    @use_kwargs(RegistroEntradaSchema, location="form")
    @marshal_with(RegistroEntradaSchema)
    def post(self, **kwargs):
        try:
            registro = add_registro_entrada(**kwargs)
            return registro, 201
        except IntegrityError as err:
            abort(400, message=f"Erro de integridade: {str(err.orig)}")
        except OperationalError:
            abort(500, message="Erro interno no servidor.")


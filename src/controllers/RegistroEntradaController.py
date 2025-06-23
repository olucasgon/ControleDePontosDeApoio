
import re
from flask_restful import Resource, abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates, validates_schema
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.services.RegistroEntradaService import getRegistrosEntrada, getRegistroEntrada, addRegistroEntrada, updateRegistroEntrada, deleteRegistroEntrada


class RegistroEntradaResponseSchema(Schema):
    id = fields.Int()
    pessoa_id = fields.Int()
    pontoapoio_id = fields.Int()
    entrada = fields.DateTime()
    saida = fields.DateTime(allow_none=True)


class RegistroEntradaRequestSchema(Schema):
    id = fields.Int()
    pessoa_id = fields.Int(required=True)
    pontoapoio_id = fields.Int(required=True)
    entrada = fields.DateTime(required=True)
    saida = fields.DateTime(allow_none=True)

    @validates("pessoa_id")
    def validate_pessoa_id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValidationError("Pessoa ID must be a positive integer.")

    @validates("pontoapoio_id")
    def validate_pontoapoio_id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValidationError("Ponto Apoio ID must be a positive integer.")

    @validates_schema
    def validate_dates(self, data, **kwargs):
        entrada = data.get("entrada")
        saida = data.get("saida")
        if saida and entrada and saida < entrada:
            raise ValidationError("Saída must be after Entrada.", field_name="saida")


class RegistroEntradaItem(MethodResource, Resource):
    @marshal_with(RegistroEntradaResponseSchema)
    def get(self, registro_id):
        try:
            registro = getRegistroEntrada(registro_id)
            if registro is None:
                abort(404, message="Registro de Entrada not found")
            return registro, 200
        except OperationalError:
            abort(500, message="Database connection error")

    def delete(self, registro_id):
        try:
            deleteRegistroEntrada(registro_id)
            return "Registro de Entrada deleted successfully", 204
        except UnmappedInstanceError:
            abort(404, message="Registro de Entrada not found")
        except (OperationalError, IntegrityError):
            abort(500, message="Database error")

    @use_kwargs(RegistroEntradaRequestSchema, location="json")
    @marshal_with(RegistroEntradaResponseSchema)
    def put(self, registro_id, **kwargs):
        try:
            updated_registro = updateRegistroEntrada(registro_id, **kwargs)
            return updated_registro, 200
        except ValidationError as e:
            abort(400, message=str(e))
        except (OperationalError, IntegrityError):
            abort(500, message="Database error")


class RegistroEntradaList(MethodResource, Resource):
    @marshal_with(RegistroEntradaResponseSchema(many=True))
    def get(self):
        try:
            registros = getRegistrosEntrada()
            return registros, 200
        except OperationalError:
            abort(500, message="Database connection error")

    @use_kwargs(RegistroEntradaRequestSchema, location="json")
    @marshal_with(RegistroEntradaResponseSchema)
    def post(self, **kwargs):
        try:
            new_registro = addRegistroEntrada(**kwargs)
            return new_registro, 201
        except ValidationError as e:
            abort(400, message=str(e))
        except (OperationalError, IntegrityError):
            abort(500, message="Database error")
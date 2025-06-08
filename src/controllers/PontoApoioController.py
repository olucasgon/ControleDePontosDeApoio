from flask_restful import Resource, abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.services.PontoApoioService import getPontosApoio,getPontoApoio, addPontoApoio, updatePontoApoio, deletePontoApoio

import re

class PontoApoioSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    latitude = fields.Float(required=True)
    longitude = fields.Float(required=True)
    capacidade = fields.Int(required=True)

    @validates('nome')
    def validate_nome(self, value):
        if not value.strip():
            raise ValidationError("Nome não pode estar vazio.")
        if not re.match(r"^[a-zA-Z0-9\s]+$", value):
            raise ValidationError("Nome deve conter apenas caracteres alfanuméricos e espaços.")

    @validates('capacidade')
    def validate_capacidade(self, value):
        if value <= 0:
            raise ValidationError("Capacidade deve ser maior que zero.")

    @validates('latitude')
    def validate_latitude(self, value):
        if not (-90 <= value <= 90):
            raise ValidationError("Latitude deve estar entre -90 e 90.")

    @validates('longitude')
    def validate_longitude(self, value):
        if not (-180 <= value <= 180):
            raise ValidationError("Longitude deve estar entre -180 e 180.")


class PontoApoioItem(MethodResource, Resource):
    @marshal_with(PontoApoioSchema)
    def get(self, pontoapoio_id):
        try:
            pontoapoio = getPontoApoio(pontoapoio_id)
            if not pontoapoio:
                abort(404, message="Ponto de apoio não encontrado.")
            return pontoapoio, 200
        except OperationalError:
            abort(500, message="Erro interno no servidor.")

    def delete(self, pontoapoio_id):
        try:
            deletePontoApoio(pontoapoio_id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Ponto de apoio não encontrado.")
        except (OperationalError, IntegrityError):
            abort(500, message="Erro interno no servidor.")

    @use_kwargs(PontoApoioSchema, location="form")
    @marshal_with(PontoApoioSchema)
    def put(self, pontoapoio_id, **kwargs):
        try:
            pontoapoio = updatePontoApoio(id=pontoapoio_id, **kwargs)
            return pontoapoio, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Erro interno no servidor.")


class PontoApoioList(MethodResource, Resource):
    @marshal_with(PontoApoioSchema(many=True))
    def get(self):
        try:
            return getPontosApoio(), 200
        except OperationalError:
            abort(500, message="Erro interno no servidor.")

    @use_kwargs(PontoApoioSchema, location="form")
    @marshal_with(PontoApoioSchema)
    def post(self, **kwargs):
        try:
            pontoapoio = addPontoApoio(**kwargs)
            return pontoapoio, 201
        except IntegrityError as err:
            abort(400, message=f"Erro de integridade: {str(err.orig)}")
        except OperationalError as err:
            abort(500, message="Erro interno no servidor.")

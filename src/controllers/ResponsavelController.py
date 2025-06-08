from flask_restful import Resource, abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields, validates, ValidationError
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.services.ResponsavelService import get_responsaveis,get_responsavel,add_responsavel,update_responsavel,delete_responsavel

class ResponsavelSchema(Schema):
    id = fields.Int(dump_only=True)
    codigo = fields.Str(required=True)
    pessoa_id = fields.Int(required=True)
    pontoapoio_id = fields.Int(required=True)

    @validates("codigo")
    def validate_codigo(self, value):
        if not value.isalnum():
            raise ValidationError("O código deve conter apenas letras e números.")


class ResponsavelItem(MethodResource, Resource):
    @marshal_with(ResponsavelSchema)
    def get(self, responsavel_id):
        try:
            responsavel = get_responsavel(responsavel_id)
            if not responsavel:
                abort(404, message="Responsável não encontrado.")
            return responsavel, 200
        except OperationalError:
            abort(500, message="Erro interno no servidor.")

    def delete(self, responsavel_id):
        try:
            delete_responsavel(responsavel_id)
            return "", 204
        except UnmappedInstanceError:
            abort(404, message="Responsável não encontrado.")
        except (OperationalError, IntegrityError):
            abort(500, message="Erro interno no servidor.")

    @use_kwargs(ResponsavelRequestSchema, location="form")
    @marshal_with(ResponsavelSchema)
    def put(self, responsavel_id, **kwargs):
        try:
            responsavel = update_responsavel(
                responsavel_id=responsavel_id,
                codigo=kwargs["codigo"],
                pessoa_id=kwargs["pessoa_id"],
                pontoapoio_id=kwargs["pontoapoio_id"]
            )
        return responsavel, 200
    except (OperationalError, IntegrityError):
        abort(500, message="Erro ao atualizar responsável")


class ResponsavelList(MethodResource, Resource):
    @marshal_with(ResponsavelSchema(many=True))
    def get(self):
        try:
            return get_responsaveis(), 200
        except OperationalError:
            abort(500, message="Erro interno no servidor.")

    @use_kwargs(ResponsavelSchema, location="form")
    @marshal_with(ResponsavelSchema)
    def post(self, **kwargs):
        try:
            responsavel = add_responsavel(**kwargs)
            return responsavel, 201
        except IntegrityError as err:
            abort(400, message=f"Erro de integridade: {str(err.orig)}")
        except OperationalError:
            abort(500, message="Erro interno no servidor.")

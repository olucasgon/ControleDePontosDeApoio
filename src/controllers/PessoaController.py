from flask_restful import Resource, abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.services.PessoaService import getPessoa,getPessoas,addPessoa,updatePessoa,deletePessoa
import re


class PessoaSchema(Schema):
    id = fields.Int()
    nome = fields.Str(required=True)
    cpf = fields.Str(required=True)
    telefone = fields.Str()
    pontoapoio_id = fields.Int()

    @validates("cpf")
    def validate_cpf(self, value):
        if not re.match(r"^\d{11}$", value):
            raise ValidationError("CPF deve conter exatamente 11 dígitos numéricos.")

class PessoaItem(MethodResource, Resource):
    @marshal_with(PessoaSchema)
    def get(self, pessoa_id):
        try:
            pessoa = getPessoa(pessoa_id)
            if not pessoa:
                abort(404, message="Pessoa não encontrada.")
            return pessoa, 200
        except OperationalError:
            abort(500, message="Erro interno do servidor.")

    def delete(self, pessoa_id):
        try:
            deletePessoa(pessoa_id)
            return "Pessoa Deletada com Sucesso", 204
        except UnmappedInstanceError:
            abort(404, message="Pessoa não encontrada.")
        except (OperationalError, IntegrityError):
            abort(500, message="Erro ao deletar a pessoa.")

    @use_kwargs(PessoaSchema, location="form")
    @marshal_with(PessoaSchema)
    def put(self, pessoa_id, **kwargs):
        try:
            pessoa = updatePessoa(**kwargs, id=pessoa_id)
            return pessoa, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Erro ao atualizar a pessoa.")

class PessoaList(MethodResource, Resource):
    @marshal_with(PessoaSchema(many=True))
    def get(self):
        try:
            return getPessoas(), 200
        except OperationalError:
            abort(500, message="Erro ao buscar lista de pessoas.")

    @use_kwargs(PessoaSchema, location="form")
    @marshal_with(PessoaSchema)
    def post(self, **kwargs):
        try:
            pessoa = addPessoa(**kwargs)
            return pessoa, 201
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError as err:
            abort(500, message=str(err.__context__))

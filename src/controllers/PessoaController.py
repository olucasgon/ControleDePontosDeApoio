import re
from flask_restful import Resource, abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.services.PessoaService import getPessoas, getPessoa, addPessoa, updatePessoa, deletePessoa
class PessoaResponseSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
    cpf = fields.Str()
    telefone = fields.Str()
    pontoapoio_id = fields.Int()


class PessoaRequestSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
    cpf = fields.Str()
    telefone = fields.Str()
    pontoapoio_id = fields.Int()


 
    @validates("nome")
    def validate_name(self, value):
        if not re.match(pattern=r"^[a-zA-Z0-9_\s]+$", string=value):
            raise ValidationError(
                "Value must contain only alphanumeric and underscore characters."
            )
        
    @validates('cpf')
    def validate_cpf(self, value):
        if not re.match(r'^\d{11}$', value):
            raise ValidationError("CPF must be a string of 11 digits.")

    @validates('telefone')
    def validate_telefone(self, value):
        if not re.match(r'^\d{10,11}$', value):
            raise ValidationError("Telefone must be a string of 10 or 11 digits.")
        
    @validates('pontoapoio_id')
    def validate_pontoapoio_id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValidationError("Ponto Apoio ID must be a positive integer.")
        

class PessoaItem(MethodResource, Resource):
    @marshal_with(PessoaResponseSchema)
    def get(self, pessoa_id):
        try:
            pessoa = getPessoa(pessoa_id)
            if not pessoa:
                abort(404, message="Pessoa not found")
            return pessoa, 200
        except OperationalError:
            abort(500, message="Database connection error")

    def delete(self, pessoa_id):
        try:
            deletePessoa(pessoa_id)
            return "Pessoa deleted successfully", 204
        except UnmappedInstanceError:
            abort(404, message="Pessoa not found")
        except (OperationalError, IntegrityError):
            abort(500, message="Database error")

    @use_kwargs(PessoaRequestSchema, location="json")
    @marshal_with(PessoaResponseSchema)
    def put(self, pessoa_id, **kwargs):
        try:
            pessoa = updatePessoa(pessoa_id, **kwargs)
            return pessoa, 200
        except (OperationalError, IntegrityError):
            abort(500, message="Database error")

class PessoaList(MethodResource, Resource):
    @marshal_with(PessoaResponseSchema(many=True))
    def get(self):
        try:
            pessoas = getPessoas()
            return pessoas, 200
        except OperationalError:
            abort(500, message="Database connection error")
        
    @use_kwargs(PessoaRequestSchema, location="json")
    @marshal_with(PessoaResponseSchema)
    def post(self, **kwargs):
        try:
            pessoa = addPessoa(**kwargs)
            return pessoa, 201
        except IntegrityError as err:
            abort(500, message=str(err.orig))
        except OperationalError as err:
            abort(500, message=str(err.orig))
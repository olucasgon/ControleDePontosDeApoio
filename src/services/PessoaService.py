from src.repositories.PessoaRepository import get_pessoas, get_pessoa, add_pessoa, update_pessoa, delete_pessoa
from src.entities.Pessoa import Pessoa

def getPessoas():
    return get_pessoas()


def getPessoa(pessoa_id: int):
    return get_pessoa(pessoa_id)

def addPessoa(id: int, nome: str, cpf: str, telefone: str, pontoapoio_id: int):
    pessoa = Pessoa()
    pessoa.id = id
    pessoa.nome = nome
    pessoa.cpf = cpf
    pessoa.telefone = telefone
    pessoa.pontoapoio_id = pontoapoio_id
    return add_pessoa(pessoa)

def updatePessoa(id: int, nome: str, cpf: str, telefone: str, pontoapoio_id: int):
    return update_pessoa(id, nome, cpf, telefone, pontoapoio_id)


def deletePessoa(pessoa_id: int):
    return delete_pessoa(pessoa_id)
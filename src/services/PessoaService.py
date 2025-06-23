from src.repositories.PessoaRepository import get_pessoas, get_pessoa, add_pessoa, update_pessoa, delete_pessoa
from src.entities.Pessoa import Pessoa

def getPessoas():
    return get_pessoas()


def getPessoa(pessoa_id: int):
    pessoa = get_pessoa(pessoa_id)
    if not pessoa:
        raise ValueError(f"Pessoa com ID {pessoa_id} não encontrada.")
    return get_pessoa(pessoa_id)

def addPessoa(nome: str, cpf: str, telefone: str, pontoapoio_id: int):
    pessoas = get_pessoas()
    for p in pessoas:
        if p.cpf == cpf and p.pontoapoio_id == pontoapoio_id:
            raise ValueError("Pessoa já cadastrada neste ponto de apoio.")

    pessoa = Pessoa()
    pessoa.nome = nome
    pessoa.cpf = cpf
    pessoa.telefone = telefone
    pessoa.pontoapoio_id = pontoapoio_id

    return add_pessoa(pessoa)

def updatePessoa(id: int, nome: str, cpf: str, telefone: str, pontoapoio_id: int):
    pessoas = get_pessoas()
    for p in pessoas:
        if p.id != id and p.cpf == cpf and p.pontoapoio_id == pontoapoio_id:
            raise ValueError("Outra pessoa com esse CPF já está cadastrada neste ponto de apoio.")

    return update_pessoa(id, nome, cpf, telefone, pontoapoio_id)


def deletePessoa(pessoa_id: int):
    pessoa = get_pessoa(pessoa_id)
    if not pessoa:
        raise ValueError("Pessoa não encontrada.")
    return delete_pessoa(pessoa_id)
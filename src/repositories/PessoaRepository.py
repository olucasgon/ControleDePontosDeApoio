from src.entities.Pessoa import Pessoa
from src.entities.Base import db

def get_pessoas() -> list[Pessoa]:

    pessoas = db.session.query(Pessoa).all()
    return pessoas

def get_pessoa(pessoa_id: int) -> Pessoa:

    pessoa = db.session.query(Pessoa).get(pessoa_id)
    return pessoa

def add_pessoa(pessoa: Pessoa) -> Pessoa:

    db.session.add(pessoa)
    db.session.commit()
    return pessoa

def update_pessoa(pessoa_id: int, nome: str, cpf: str, telefone: str, pontoapoio_id: int) -> Pessoa:

    pessoa = db.session.query(Pessoa).get(pessoa_id)
    if pessoa:
        pessoa.nome = nome
        pessoa.cpf = cpf
        pessoa.telefone = telefone
        pessoa.pontoapoio_id = pontoapoio_id
        db.session.commit()
    return pessoa

def delete_pessoa(pessoa_id: int) -> Pessoa:

    pessoa = db.session.query(Pessoa).get(pessoa_id)
    if pessoa:
        db.session.delete(pessoa)
        db.session.commit()
    return pessoa

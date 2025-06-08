from src.entities.Responsavel import Responsavel
from src.entities.Base import db

def get_responsaveis() -> list[Responsavel]:

    responsaveis = db.session.query(Responsavel).all()
    return responsaveis

def get_responsavel(responsavel_id: int) -> Responsavel:
    
    responsavel = db.session.query(Responsavel).get(responsavel_id)
    return responsavel

def add_responsavel(responsavel: Responsavel) -> Responsavel:

    db.session.add(responsavel)
    db.session.commit()
    return responsavel

def update_responsavel(responsavel_id: int, codigo: str, pessoa_id: int, pontoapoio_id: int) -> Responsavel:
    responsavel = db.session.query(Responsavel).get(responsavel_id)
    if responsavel:
        responsavel.codigo = codigo
        responsavel.pessoa_id = pessoa_id
        responsavel.pontoapoio_id = pontoapoio_id
        db.session.commit()
    return responsavel

def delete_responsavel(responsavel_id: int) -> Responsavel:

    responsavel = db.session.query(Responsavel).get(responsavel_id)
    if responsavel:
        db.session.delete(responsavel)
        db.session.commit()
    return responsavel

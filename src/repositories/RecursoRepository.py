from src.entities.Recurso import Recurso
from src.entities.Base import db

def get_recursos() -> list[Recurso]:
    
    recursos = db.session.query(Recurso).all()
    return recursos

def get_recurso(recurso_id: int) -> Recurso:
    
    recurso = db.session.query(Recurso).get(recurso_id)
    return recurso

def add_recurso(recurso: Recurso) -> Recurso:
   
    db.session.add(recurso)
    db.session.commit()
    return recurso

def update_recurso(recurso_id: int, nome: str, quantidade: int, pontoapoio_id: int) -> Recurso:
    
    recurso = db.session.query(Recurso).get(recurso_id)
    if recurso:
        recurso.nome = nome
        recurso.quantidade = quantidade
        recurso.pontoapoio_id = pontoapoio_id
        db.session.commit()
    return recurso

def delete_recurso(recurso_id: int) -> Recurso:
   
    recurso = db.session.query(Recurso).get(recurso_id)
    if recurso:
        db.session.delete(recurso)
        db.session.commit()
    return recurso
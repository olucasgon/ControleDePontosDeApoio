from src.repositories.RecursoRepository import get_recursos, get_recurso, add_recurso, update_recurso, delete_recurso
from src.entities.Recurso import Recurso

def getRecursos():
    return get_recursos()

def getRecurso(recurso_id: int):
    return get_recurso(recurso_id)

def addRecurso(id: int, nome: str, quantidade: int, ponto_apoio_id: int):
    recurso = Recurso()
    recurso.id = id
    recurso.nome = nome
    recurso.quantidade = quantidade
    recurso.ponto_apoio_id = ponto_apoio_id

    return add_recurso(recurso)

def updateRecurso(id: int, nome: str, quantidade: int, ponto_apoio_id: int):
    return update_recurso(id, nome, quantidade, ponto_apoio_id)

def deleteRecurso(recurso_id: int):
    return delete_recurso(recurso_id)


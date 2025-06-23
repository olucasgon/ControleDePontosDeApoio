from src.repositories.RecursoRepository import get_recursos, get_recurso, add_recurso, update_recurso, delete_recurso
from src.entities.Recurso import Recurso

def getRecursos():
    return get_recursos()

def getRecurso(recurso_id: int):
    recurso = get_recurso(recurso_id)
    if not recurso:
        raise ValueError(f"Recurso com ID {recurso_id} não encontrado.")
    return get_recurso(recurso_id)

def addRecurso(nome: str, quantidade: int, pontoapoio_id: int):
    if quantidade < 0:
        raise ValueError("Quantidade não pode ser negativa.")

    recurso = Recurso()
    recurso.nome = nome
    recurso.quantidade = quantidade
    recurso.pontoapoio_id = pontoapoio_id

    return add_recurso(recurso)

def updateRecurso(id: int, nome: str, quantidade: int, pontoapoio_id: int):
    if quantidade < 0:
        raise ValueError("Quantidade não pode ser negativa.")
    recurso = get_recurso(id)
    if not recurso:
        raise ValueError("Recurso não encontrado.")
    return update_recurso(id, nome, quantidade, pontoapoio_id)

def deleteRecurso(recurso_id: int):
    recurso = get_recurso(recurso_id)
    if not recurso:
        raise ValueError("Recurso não encontrado.")
    return delete_recurso(recurso_id)

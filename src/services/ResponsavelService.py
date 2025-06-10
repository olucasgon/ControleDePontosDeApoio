from src.repositories.ResponsavelRepository import get_responsaveis, get_responsavel, add_responsavel, update_responsavel, delete_responsavel
from src.entities.Responsavel import Responsavel

def getResponsaveis():
    return get_responsaveis()

def getResponsavel(responsavel_id: int):
    return get_responsavel(responsavel_id)

def addResponsavel(id: int, codigo: str, pessoa_id: int, ponto_apoio_id: int):
    responsavel = Responsavel()
    responsavel.id = id
    responsavel.codigo = codigo
    responsavel.pessoa_id = pessoa_id
    responsavel.ponto_apoio_id = ponto_apoio_id

    return add_responsavel(responsavel)

def updateResponsavel(id: int, codigo: str, pessoa_id: int, ponto_apoio_id: int):
    return update_responsavel(id, codigo, pessoa_id, ponto_apoio_id)

def deleteResponsavel(responsavel_id: int):
    return delete_responsavel(responsavel_id)
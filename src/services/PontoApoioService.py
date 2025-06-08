from src.repositories.PontoApoioRepository import get_pontos_apoio, get_ponto_apoio, add_ponto_apoio, update_ponto_apoio, delete_ponto_apoio
from src.entities.PontoApoio import PontoApoio

def getPontosApoio():
    return get_pontos_apoio()

def getPontoApoio(ponto_apoio_id: int):
    return get_ponto_apoio(ponto_apoio_id)

def addPontoApoio(id: int, nome: str, latitude: float, longitude: float, capacidade: int = 0):
    ponto_apoio = PontoApoio()
    ponto_apoio.id = id
    ponto_apoio.nome = nome
    ponto_apoio.latitude = latitude
    ponto_apoio.longitude = longitude
    ponto_apoio.capacidade = 0 

    return add_ponto_apoio(ponto_apoio)

def updatePontoApoio(id: int, nome: str, latitude: float, longitude: float, capacidade: int):
    return update_ponto_apoio(id, nome, latitude, longitude, capacidade)

def deletePontoApoio(ponto_apoio_id: int):
    return delete_ponto_apoio(ponto_apoio_id)
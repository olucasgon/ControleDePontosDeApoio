from src.repositories.RegistroEntradaRepository import get_registros_entrada, get_registro_entrada, add_registro_entrada, update_registro_entrada, delete_registro_entrada
from src.entities.RegistroEntrada import RegistroEntrada
from datetime import datetime

def getRegistrosEntrada():
    return get_registros_entrada()

def getRegistroEntrada(registro_entrada_id: int):
    return get_registro_entrada(registro_entrada_id)

def addRegistroEntrada(id: int, pessoa_id: int, ponto_apoio_id: int, entrada: datetime, saida: datetime = None):
    registro_entrada = RegistroEntrada()
    registro_entrada.id = id
    registro_entrada.pessoa_id = pessoa_id
    registro_entrada.ponto_apoio_id = ponto_apoio_id
    registro_entrada.entrada = entrada
    registro_entrada.saida = saida

    return add_registro_entrada(registro_entrada)

def updateRegistroEntrada(id: int, pessoa_id: int, ponto_apoio_id: int, entrada: datetime, saida: datetime = None):
    return update_registro_entrada(id, pessoa_id, ponto_apoio_id, entrada, saida)

def deleteRegistroEntrada(registro_entrada_id: int):
    return delete_registro_entrada(registro_entrada_id)

from src.repositories.RegistroEntradaRepository import (
    get_registros_entrada,
    get_registro_entrada,
    add_registro_entrada,
    update_registro_entrada,
    delete_registro_entrada
)
from src.repositories.PontoApoioRepository import get_ponto_apoio
from src.entities.RegistroEntrada import RegistroEntrada
from datetime import datetime


def getRegistrosEntrada():
    return get_registros_entrada()


def getRegistroEntrada(registro_entrada_id: int):
    registro = get_registro_entrada(registro_entrada_id)
    if not registro:
        raise ValueError(f"Registro com ID {registro_entrada_id} não encontrado.")
    return registro


def addRegistroEntrada(pessoa_id: int, pontoapoio_id: int, entrada: datetime, saida: datetime = None):
    if saida and entrada > saida:
        raise ValueError("A data de entrada não pode ser posterior à data de saída.")

    registros = get_registros_entrada()
    for r in registros:
        if r.pessoa_id == pessoa_id and r.saida is None:
            raise ValueError("Esta pessoa já está registrada como abrigada em um ponto de apoio.")

    pontoapoio = get_ponto_apoio(pontoapoio_id)
    if not pontoapoio:
        raise ValueError("Ponto de apoio não encontrado.")

    ocupacao_atual = len([
        r for r in registros
        if r.pontoapoio_id == pontoapoio_id and r.saida is None
    ])
    if ocupacao_atual >= pontoapoio.capacidade:
        raise ValueError("Capacidade do ponto de apoio já atingida.")

    registro_entrada = RegistroEntrada()
    registro_entrada.pessoa_id = pessoa_id
    registro_entrada.pontoapoio_id = pontoapoio_id
    registro_entrada.entrada = entrada
    registro_entrada.saida = saida

    return add_registro_entrada(registro_entrada)


def updateRegistroEntrada(id: int, pessoa_id: int, pontoapoio_id: int, entrada: datetime, saida: datetime = None):
    if saida and entrada > saida:
        raise ValueError("A data de entrada não pode ser posterior à data de saída.")
    return update_registro_entrada(id, pessoa_id, pontoapoio_id, entrada, saida)


def deleteRegistroEntrada(registro_entrada_id: int):
    registro = get_registro_entrada(registro_entrada_id)
    if not registro:
        raise ValueError(f"Registro com ID {registro_entrada_id} não encontrado.")
    return delete_registro_entrada(registro_entrada_id)
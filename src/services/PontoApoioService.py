from src.repositories.PontoApoioRepository import get_pontos_apoio, get_ponto_apoio, add_ponto_apoio, update_ponto_apoio, delete_ponto_apoio
from src.repositories.PessoaRepository import get_pessoas
from src.entities.PontoApoio import PontoApoio

def getPontosApoio():
    return get_pontos_apoio()

def getPontoApoio(ponto_apoio_id: int):
    ponto = get_ponto_apoio(ponto_apoio_id)
    if not ponto:
        raise ValueError("Ponto de apoio não encontrado.")
    return ponto

def addPontoApoio(nome: str, latitude: float, longitude: float, capacidade: int):
    if not nome.strip():
        raise ValueError("Nome do ponto de apoio não pode ser vazio.")
    pontos = get_pontos_apoio()
    for p in pontos:
        if p.nome.lower() == nome.strip().lower():
            raise ValueError("Nome do ponto de apoio já existe.")
    if capacidade <= 0:
        raise ValueError("Capacidade deve ser maior que zero.")

    ponto_apoio = PontoApoio()
    ponto_apoio.nome = nome.strip()
    ponto_apoio.latitude = latitude
    ponto_apoio.longitude = longitude
    ponto_apoio.capacidade = capacidade

    return add_ponto_apoio(ponto_apoio)

def updatePontoApoio(id: int, nome: str, latitude: float, longitude: float, capacidade: int):
    ponto = get_ponto_apoio(id)
    if not ponto:
        raise ValueError("Ponto de apoio não encontrado.")
    if not nome.strip():
        raise ValueError("Nome do ponto de apoio não pode ser vazio.")
    pontos = get_pontos_apoio()
    for p in pontos:
        if p.id != id and p.nome.lower() == nome.strip().lower():
            raise ValueError("Nome do ponto de apoio já existe.")
    if capacidade <= 0:
        raise ValueError("Capacidade deve ser maior que zero.")

    return update_ponto_apoio(id, nome.strip(), latitude, longitude, capacidade)

def deletePontoApoio(ponto_apoio_id: int):
    ponto = get_ponto_apoio(ponto_apoio_id)
    if not ponto:
        raise ValueError("Ponto de apoio não encontrado.")
    pessoas = get_pessoas()
    abrigadas = [p for p in pessoas if p.pontoapoio_id == ponto_apoio_id]
    if abrigadas:
        raise ValueError("Não é possível remover ponto de apoio com pessoas abrigadas.")
    return delete_ponto_apoio(ponto_apoio_id)
from src.entities.PontoApoio import PontoApoio
from src.entities.Base import db

def get_pontos_apoio() -> list[PontoApoio]:
    pontos_apoio = db.session.query(PontoApoio).all()
    return pontos_apoio

def get_ponto_apoio(ponto_apoio_id: int) -> PontoApoio:
    ponto_apoio = db.session.query(PontoApoio).get(ponto_apoio_id)
    return ponto_apoio

def add_ponto_apoio(ponto_apoio: PontoApoio) -> PontoApoio:
    db.session.add(ponto_apoio)
    db.session.commit()
    return ponto_apoio

def update_ponto_apoio(ponto_apoio_id: int, nome: str, latitude: float, longitude: float, capacidade: int) -> PontoApoio:
    ponto_apoio = db.session.query(PontoApoio).get(ponto_apoio_id)
    if ponto_apoio:
        ponto_apoio.nome = nome
        ponto_apoio.latitude = latitude
        ponto_apoio.longitude = longitude
        ponto_apoio.capacidade = capacidade
        db.session.commit()
    return ponto_apoio

def delete_ponto_apoio(ponto_apoio_id: int) -> PontoApoio:
    ponto_apoio = db.session.query(PontoApoio).get(ponto_apoio_id)
    if ponto_apoio:
        db.session.delete(ponto_apoio)
        db.session.commit()
    return ponto_apoio
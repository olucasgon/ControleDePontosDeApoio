from datetime import datetime
from src.entities.RegistroEntrada import RegistroEntrada
from src.entities.Base import db

def get_registros_entrada() -> list[RegistroEntrada]:

    registros_entrada = db.session.query(RegistroEntrada).all()
    return registros_entrada

def get_registro_entrada(registro_entrada_id: int) -> RegistroEntrada:
    
    registro_entrada = db.session.query(RegistroEntrada).get(registro_entrada_id)
    return registro_entrada

def add_registro_entrada(registro_entrada: RegistroEntrada) -> RegistroEntrada:

    db.session.add(registro_entrada)
    db.session.commit()
    return registro_entrada

def update_registro_entrada(registro_entrada_id: int, pessoa_id: int, ponto_apoio_id: int, entrada: datetime , saida: datetime) -> RegistroEntrada:
    
    registro_entrada = db.session.query(RegistroEntrada).get(registro_entrada_id)
    if registro_entrada:
        registro_entrada.pessoa_id = pessoa_id
        registro_entrada.ponto_apoio_id = ponto_apoio_id
        registro_entrada.entrada = entrada
        registro_entrada.saida = saida
        db.session.commit()
    return registro_entrada

def delete_registro_entrada(registro_entrada_id: int) -> RegistroEntrada:
    
    registro_entrada = db.session.query(RegistroEntrada).get(registro_entrada_id)
    if registro_entrada:
        db.session.delete(registro_entrada)
        db.session.commit()
    return registro_entrada
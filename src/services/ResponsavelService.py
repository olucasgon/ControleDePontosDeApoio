from src.repositories.ResponsavelRepository import get_responsaveis, get_responsavel, add_responsavel, update_responsavel, delete_responsavel
from src.repositories.PontoApoioRepository import get_ponto_apoio
from src.repositories.PessoaRepository import get_pessoa
from src.entities.Responsavel import Responsavel

def getResponsaveis():
    return get_responsaveis()

def getResponsavel(responsavel_id: int):
    responsavel = get_responsavel(responsavel_id)
    if not responsavel:
        raise ValueError(f"Responsável com ID {responsavel_id} não encontrado.")
    return responsavel

def addResponsavel(codigo: str, pessoa_id: int, pontoapoio_id: int):
    if not codigo.strip():
        raise ValueError("O código do responsável não pode ser vazio.")

    responsaveis = get_responsaveis()
    for r in responsaveis:
        if r.pessoa_id == pessoa_id and r.pontoapoio_id == pontoapoio_id:
            raise ValueError("Pessoa já é responsável por este ponto de apoio.")

    ponto = get_ponto_apoio(pontoapoio_id)
    if not ponto:
        raise ValueError("Ponto de apoio não encontrado.")

    pessoa = get_pessoa(pessoa_id)
    if not pessoa:
        raise ValueError("Pessoa não encontrada.")

    responsavel = Responsavel()
    responsavel.codigo = codigo
    responsavel.pessoa_id = pessoa_id
    responsavel.pontoapoio_id = pontoapoio_id

    return add_responsavel(responsavel)

def updateResponsavel(id: int, codigo: str, pessoa_id: int, pontoapoio_id: int):

    if not codigo.strip():
        raise ValueError("O código do responsável não pode ser vazio.")

    ponto = get_ponto_apoio(pontoapoio_id)
    if not ponto:
        raise ValueError("Ponto de apoio não encontrado.")

    pessoa = get_pessoa(pessoa_id)
    if not pessoa:
        raise ValueError("Pessoa não encontrada.")

    responsaveis = get_responsaveis()
    for r in responsaveis:
        if r.id != id and r.pessoa_id == pessoa_id and r.pontoapoio_id == pontoapoio_id:
            raise ValueError("Outra entrada com essa pessoa e ponto de apoio já existe.")

    return update_responsavel(id, codigo, pessoa_id, pontoapoio_id)

def deleteResponsavel(responsavel_id: int):
    responsavel = get_responsavel(responsavel_id)
    if not responsavel:
        raise ValueError("Responsável não encontrado.")

    return delete_responsavel(responsavel_id)
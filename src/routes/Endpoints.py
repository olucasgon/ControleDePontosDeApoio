from src.controllers.PessoaController import  PessoaItem, PessoaList
from src.controllers.PontoApoioController import PontoApoioItem, PontoApoioList

def initialize_endpoints(api):

    api.add_resource(PessoaItem, '/pessoa/<int:pessoa_id>', endpoint='pessoa_item')
    api.add_resource(PessoaList, '/pessoa', endpoint='pessoa_list')

    api.add_resource(PontoApoioItem, '/ponto_apoio/<int:ponto_apoio_id>', endpoint='ponto_apoio_item')
    api.add_resource(PontoApoioList, '/ponto_apoio', endpoint='ponto_apoio_list')
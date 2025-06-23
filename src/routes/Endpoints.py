from src.controllers.PessoaController import PessoaItem, PessoaList
from src.controllers.PontoApoioController import PontoApoioItem, PontoApoioList
from src.controllers.RecursoController import RecursoItem, RecursoList
from src.controllers.RegistroEntradaController import RegistroEntradaItem, RegistroEntradaList
from src.controllers.ResponsavelController import ResponsavelItem, ResponsavelList

def initialize_endpoints(api):

    # Pessoas
    api.add_resource(PessoaItem, '/pessoa/<int:pessoa_id>', endpoint='pessoa_item')
    api.add_resource(PessoaList, '/pessoa', endpoint='pessoa_list')

    # Pontos de Apoio
    api.add_resource(PontoApoioItem, '/ponto_apoio/<int:ponto_apoio_id>', endpoint='ponto_apoio_item')
    api.add_resource(PontoApoioList, '/ponto_apoio', endpoint='ponto_apoio_list')

    # Recursos
    api.add_resource(RecursoItem, '/recurso/<int:recurso_id>', endpoint='recurso_item')
    api.add_resource(RecursoList, '/recurso', endpoint='recurso_list')

    # Registros de Entrada
    api.add_resource(RegistroEntradaItem, '/registro_entrada/<int:registro_id>', endpoint='registro_entrada_item')
    api.add_resource(RegistroEntradaList, '/registro_entrada', endpoint='registro_entrada_list')

    # Responsáveis
    api.add_resource(ResponsavelItem, '/responsavel/<int:responsavel_id>', endpoint='responsavel_item')
    api.add_resource(ResponsavelList, '/responsavel', endpoint='responsavel_list')
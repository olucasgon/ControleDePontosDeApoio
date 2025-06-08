from src.controllers.PessoaController import PessoaList, PessoaItem
from src.controllers.PontoApoioController import PontoApoioList, PontoApoioItem
from src.controllers.RecursoController import RecursoList, RecursoItem
from src.controllers.RegistroEntradaController import RegistroEntradaList, RegistroEntradaItem
from src.controllers.ResponsavelController import ResponsavelList, ResponsavelItem

def initialize_endpoints(api):
    # Rotas para Pessoa
    api.add_resource(PessoaList, "/pessoas")
    api.add_resource(PessoaItem, "/pessoas/<int:pessoa_id>")

    # Rotas para Ponto de Apoio
    api.add_resource(PontoApoioList, "/pontosapoio")
    api.add_resource(PontoApoioItem, "/pontosapoio/<int:pontoapoio_id>")

    # Rotas para Recurso
    api.add_resource(RecursoList, "/recursos")
    api.add_resource(RecursoItem, "/recursos/<int:recurso_id>")

    # Rotas para Registro de Entrada
    api.add_resource(RegistroEntradaList, "/registrosentrada")
    api.add_resource(RegistroEntradaItem, "/registrosentrada/<int:registroentrada_id>")

    # Rotas para Responsável
    api.add_resource(ResponsavelList, "/responsaveis")
    api.add_resource(ResponsavelItem, "/responsaveis/<int:responsavel_id>")

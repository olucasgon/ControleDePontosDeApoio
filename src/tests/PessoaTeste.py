import requests
URL = "http://127.0.0.1:5000/api/pessoa"

pessoa = {
    "cpf": "123.456.789-00",
    "id": 1,
    "nome": "João Silva",
    "pontoapoio_id": 1,
    "telefone": "21999990000"
}

response = requests.post(
    url = URL,
    json = pessoa
)
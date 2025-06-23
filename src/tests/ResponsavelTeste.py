import requests
URL = "http://127.0.0.1:5000/api/responsavel"

Responsavel = {
    "codigo": "R001",
    "id": 1,
    "pessoa_id": 1,
    "pontoapoio_id": 1
}

response = requests.post(
    url = URL,
    json = Responsavel
)
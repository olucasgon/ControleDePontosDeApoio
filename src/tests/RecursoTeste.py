import requests 
URL = "http://127.0.0.1:5000/api/recurso"

recurso = {
    "id": 1,
    "nome": "Gerador",
    "pontoapoio_id": 1,
    "quantidade": 3
}

response = requests.post(
    url = URL,
    json = recurso
)
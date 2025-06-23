import requests 
URL = "http://127.0.0.1:5000/api/registro_entrada"

registro_entrada = {
    "entrada": "2025-06-01T08:00:00",
    "id": 1,
    "pessoa_id": 1,
    "pontoapoio_id": 1,
    "saida": "2025-06-01T17:00:00"
}

response = requests.post(
    url = URL,
    json = registro_entrada
)
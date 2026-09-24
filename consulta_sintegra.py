import requests

TOKEN = "COLOQUE_SEU_TOKEN_AQUI"

URL = "https://api.arquivo-nfe.com/prod/consulta_cadastro"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}"
}

PARAMETROS = {
    "uf": "SP",
    "cnpj": "COLOQUE_UM_CNPJ_AQUI"
}

print("Consultando SINTEGRA...")
print()

resposta = requests.get(
    URL,
    headers=HEADERS,
    params=PARAMETROS,
    timeout=60
)

print("HTTP Status:", resposta.status_code)
print("Resposta:")
print(resposta.text)

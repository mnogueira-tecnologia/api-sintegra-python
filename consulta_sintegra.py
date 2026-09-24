import requests

TOKEN = input("Digite seu token de acesso: ")

URL = "https://api.arquivo-nfe.com/prod/consulta_cadastro"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}"
}

PARAMETROS = {
    "uf": input("Digite a UF: ").strip().upper(),
    "cnpj": input("Digite o CNPJ: ").strip()
}

print("Consultando SINTEGRA...")
print()

resposta = requests.post(
    URL,
    headers=HEADERS,
    params=PARAMETROS,
    timeout=60
)

print("HTTP Status:", resposta.status_code)
print("Resposta:")
print(resposta.text)

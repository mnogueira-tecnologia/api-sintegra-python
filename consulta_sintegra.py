import requests

# Token de acesso à API
TOKEN = "COLOQUE_SEU_TOKEN_AQUI"

# URL da API SINTEGRA
URL = "https://api.arquivo-nfe.com/prod/sintegra"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}"
}

# Exemplos de consultas
# Informe apenas UM dos campos: cnpj, cpf ou ie
consultas = [
    {
        "uf": "SP",
        "cnpj": "COLOQUE_CNPJ_AQUI",
        "cpf": None,
        "ie": None,
        "request_id": None
    },
    {
        "uf": "SP",
        "cnpj": None,
        "cpf": None,
        "ie": "COLOQUE_IE_AQUI",
        "request_id": None
    },
    {
        "uf": "RJ",
        "cnpj": None,
        "cpf": "COLOQUE_CPF_AQUI",
        "ie": None,
        "request_id": None
    }
]


def criar_parametros(consulta):
    parametros = {
        "uf": consulta["uf"]
    }

    identificadores = [
        ("cnpj", consulta.get("cnpj")),
        ("cpf", consulta.get("cpf")),
        ("ie", consulta.get("ie"))
    ]

    informados = [
        nome
        for nome, valor in identificadores
        if valor is not None and valor != ""
    ]

    if len(informados) != 1:
        raise ValueError(
            "Informe exatamente um dos parâmetros: cnpj, cpf ou ie."
        )

    nome = informados[0]
    parametros[nome] = consulta[nome]

    return parametros


print("Integração com a API SINTEGRA")
print("-" * 50)

for consulta in consultas:

    parametros = criar_parametros(consulta)

    resposta = requests.get(
        URL,
        headers=HEADERS,
        params=parametros,
        timeout=60
    )

    dados = resposta.json()

    print("\nConsulta:")
    print(dados)

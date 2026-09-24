# Integração da API SINTEGRA em Python – Consulta de Inscrição Estadual em tempo real

Exemplo de integração em **Python** com a API SINTEGRA da **ArquivoNFe**, para consulta de dados cadastrais por UF.

A API permite realizar consultas utilizando **CNPJ, CPF ou Inscrição Estadual (IE)**, conforme a disponibilidade da consulta para cada UF.

## 🔎 Palavras-chave

* API SINTEGRA
* Consulta SINTEGRA
* SINTEGRA CCC
* Consulta Inscrição Estadual
* API Fiscal Brasil
* Consulta CNPJ
* Consulta CPF
* Consulta Inscrição Estadual por API

## Benefícios

✔ Consulta por CNPJ, CPF ou IE
✔ Dados cadastrais retornados pela API
✔ Integração simples via API REST
✔ Processamento assíncrono utilizando `request_id`
✔ Exemplo prático de integração em Python

## Casos de uso

✔ Validação cadastral antes da emissão de NF
✔ Conferência cadastral automática
✔ Verificação de informações de empresas e contribuintes
✔ Integração com sistemas ERP e aplicações próprias
✔ Processos de KYC (Know Your Customer)

## Diferenciais

✔ Consulta dos dados cadastrais disponibilizados pela SEFAZ da UF consultada.
✔ Comunicação segura por HTTPS.
✔ Infraestrutura hospedada na Oracle Cloud no Brasil.
✔ Painel web para configurações, consultas manuais e acompanhamento das integrações via API.
✔ API REST com suporte a consultas por CNPJ, CPF ou Inscrição Estadual.

---

## 🚀 Requisitos

* Windows ou Linux
* Python 3.x
* Biblioteca `requests`

---

## ⚙️ Como utilizar

### 1️⃣ Cadastre-se gratuitamente

Acesse o portal:

https://portal.arquivo-nfe.com

Crie sua conta para obter acesso à API.

---

### 2️⃣ Copie seu Token

Após o login no portal:

1. Acesse o menu **Meu Token**.
2. Copie seu token de acesso.

> ⚠️ **Nunca publique seu token de acesso no GitHub.**

No arquivo `consulta_sintegra.py`, informe seu token apenas localmente:

```python
TOKEN = 'SEU_TOKEN_AQUI'
```

Antes de publicar o código, certifique-se de que o token não esteja preenchido.

---

### 3️⃣ Instalação do Python

O exemplo utiliza **Python 3**.

#### Windows

Baixe o Python pelo site oficial:

https://www.python.org/downloads/windows/

Durante a instalação, marque a opção:

**Add python.exe to PATH**

Depois de concluir a instalação, abra o **Prompt de Comando (CMD)** e execute:

```bash
python --version
```

O comando deverá apresentar a versão instalada, por exemplo:

```text
Python 3.13.x
```

#### Linux

Verifique se o Python 3 está instalado:

```bash
python3 --version
```

Caso não esteja instalado, utilize o gerenciador de pacotes da sua distribuição.

Por exemplo, no Ubuntu/Debian:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

Depois confirme:

```bash
python3 --version
```

---

### 4️⃣ Instalação das dependências

O exemplo utiliza a biblioteca `requests` para realizar as chamadas HTTP à API.

No Windows, abra o **Prompt de Comando (CMD)** e acesse a pasta onde está o projeto.

Execute:

```bash
pip install -r requirements.txt
```

Depois da instalação, você pode verificar se a biblioteca `requests` está disponível:

```bash
pip show requests
```

No Linux, utilize:

```bash
pip3 install -r requirements.txt
```

---

### 5️⃣ Script Python

O exemplo completo de integração está disponível no arquivo [`consulta_sintegra.py`](consulta_sintegra.py).

O script demonstra:

* configuração do token de acesso;
* envio de consultas por CNPJ, CPF ou Inscrição Estadual;
* armazenamento do `request_id` (protocolo da consulta);
* consulta dos resultados de forma assíncrona;
* novas tentativas quando a consulta ainda está em processamento;
* tratamento das respostas da API;
* exibição dos resultados em formato JSON.

Depois de instalar as dependências e configurar o token, execute:

#### Windows

```bash
python consulta_sintegra.py
```

#### Linux

```bash
python3 consulta_sintegra.py
```

O código-fonte completo está disponível em:

[`consulta_sintegra.py`](consulta_sintegra.py)

---

## 📄 Exemplo de retorno da API

O exemplo abaixo apresenta um retorno da API após a conclusão da consulta:

![Retorno JSON](exemplo_ccc_retorno_json.png)

---

## 🔗 Documentação da API

Consulte a documentação completa da API SINTEGRA:

https://www.arquivo-nfe.com/api-sintegra-ccc

---

## ⭐ Apoie o projeto

Se este projeto foi útil para você:

⭐ **Deixe uma estrela no repositório.**

Isso ajuda outras pessoas a encontrarem este exemplo de integração.

---

Made with ❤️ by **ArquivoNfe**

https://www.arquivo-nfe.com

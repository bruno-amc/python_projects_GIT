#arquivo usado para testes apenas.
"""

import urllib.request
import json

# URL da API que você deseja consultar
url = "http://economia.awesomeapi.com.br/json/last/BRL-CAD"

try:
    # Fazendo a solicitação GET para a API
    with urllib.request.urlopen(url) as response:
        # Lendo os dados da resposta
        data = response.read().decode("utf-8")

        # Convertendo os dados JSON para um dicionário Python
        dados = json.loads(data)

        # Faça algo com os dados aqui
        print("Dados da API:")
        print(dados)

except urllib.error.URLError as e:
    # Se houver um erro ao fazer a solicitação, imprima o erro
    print("Erro ao acessar a API:", e)


"""
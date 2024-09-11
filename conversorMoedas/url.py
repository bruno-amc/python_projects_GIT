import json
import urllib.request

def obterCotacoesCambio(moeda_de_origem, moeda_de_destino):
    """
    A API gera um retorno no seguinte formato:
    {'BRLUSD': {'code': 'BRL', 'codein': 'USD', 'name': 'Real Brasileiro/Dólar Americano', 
    'high': '0.2019', 'low': '0.2018', 'varBid': '0', 'pctChange': '0', 'bid': '0.2018', 
    'ask': '0.2019', 'timestamp': '1707853537', 'create_date': '2024-02-13 16:45:37'}}

    No qual a primeira chave indica a comnbinação de moedas usadas na conversão e a cotação retornada com 
    a chave 'ask' é a cotação desejada. Por isso a variável valor_desejado foi montada usando f-strings, de forma
    que a chave a ser acessada pudesse sofrer alteraçãoes conforme a moeda escolhida.

    Args:
        moeda_de_origem (str): A moeda de origem para a conversão (ex: "BRL" para Real Brasileiro).
        moeda_de_destino (str): A moeda de destino para a conversão (ex: "USD" para Dólar Americano).

    Returns:
        float: O valor da cotação da moeda de origem para a moeda de destino.
    """

    url = f"http://economia.awesomeapi.com.br/json/last/{moeda_de_origem}-{moeda_de_destino}"
    
    try:
        # Fazendo a solicitação GET para a API
        with urllib.request.urlopen(url) as response:
            # Lendo os dados da resposta
            data = response.read().decode("utf-8")
    
            # Convertendo os dados JSON para um dicionário Python
            dados = json.loads(data)
            print(dados)
            
            valor_desejado = dados[f'{moeda_de_origem}{moeda_de_destino}']['ask']
            print(valor_desejado,"*"*20)
            momento_da_consulta = dados[f'{moeda_de_origem}{moeda_de_destino}']['create_date']
            print(momento_da_consulta)
            return valor_desejado , momento_da_consulta
    
    except urllib.error.URLError as e:
        # Se houver um erro ao fazer a solicitação, imprima o erro
        print("Erro ao acessar a API:", e)
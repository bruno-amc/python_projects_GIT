from url import obterCotacoesCambio
import datetime

def calculoConversao(moeda_de_origem1, moeda_de_destino1, 
                     valor_para_conversao, resultado, result_data_consulta, result_ultima_atualizacao_cambio):

    try:
        valor_desejado_cambio, momento_da_consulta_do_cambio = obterCotacoesCambio(moeda_de_origem1, moeda_de_destino1) 
        valor_final = float(valor_para_conversao) * float(valor_desejado_cambio)
        resultado.config(text=f'Resultado: {valor_final}')
        result_data_consulta.config(text=f'Data da pesquisa: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
        result_ultima_atualizacao_cambio.config(text=f'Data da última cotação: {momento_da_consulta_do_cambio}')
        return valor_final
    except:
        resultado.config(text='Resultado:NÃO PODE SER CALCULADO')
        print(Exception)



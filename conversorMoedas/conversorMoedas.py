import tkinter as tk
from tkinter import Toplevel, Label, Entry, Button, StringVar, Text, ttk
from tkinter.ttk import Combobox
from calculo import calculoConversao

#função para limpar os campos
def limpar_campos():
    lista_moedas_destino.set('')
    lista_moedas_origem.set('')
    entrada_valor_a_ser_convertido.delete(0, 'end')
    resultado.config(text='')
    resultado_data_consulta.config(text='')
    resultado_ultima_atualizacao_cambio.config(text='')

janela_principal = tk.Tk()
janela_principal.title('Conversor de Moedas - Taxa de câmbio')

icone = 'icone_moedas.ico' # arquivo na extensão .ico que está no mesmo diretório do programav
janela_principal.iconbitmap(icone)

# Variável de controle para o da lista de moedas
moedas_var = tk.StringVar()
moedas_var2 = tk.StringVar()

#widgets
rotulo_moeda_origem = tk.Label(janela_principal, text="Selecione a moeda de origem: ")
opcoes_moedas = ["BRL", "USD", "GBP", "CAD", "EUR", "AUD", "XAU"]
lista_moedas_origem = Combobox(janela_principal, textvariable=moedas_var, values=opcoes_moedas, state="readonly")
rotulo_moeda_destino = tk.Label(janela_principal, text="Selecione a moeda de destino: ")
lista_moedas_destino = Combobox(janela_principal, textvariable=moedas_var2, values=opcoes_moedas, state="readonly")
espaco_vazio = Label(janela_principal, text="", width=10, height=2)
resultado = tk.Label(janela_principal,text='Resultado:')
resultado_data_consulta = tk.Label(janela_principal,text='')
resultado_ultima_atualizacao_cambio = tk.Label(janela_principal,text='')

botao_realizar_conversao = Button(janela_principal, text='Converter', command= lambda: calculoConversao(lista_moedas_origem.get(),
                                                                                                         lista_moedas_destino.get(),
                                                                                                         entrada_valor_a_ser_convertido.get(),
                                                                                                         resultado,
                                                                                                         resultado_data_consulta,
                                                                                                         resultado_ultima_atualizacao_cambio ),
                                                                                                           )

rotulo_valor_a_ser_convertido = tk.Label(janela_principal, text="Informe o valor: ")
entrada_valor_a_ser_convertido = tk.Entry(janela_principal)
botao_limpar_campo = Button(janela_principal, text='Limpar todos os campos', command= limpar_campos)
botao_fechar_aplicacao = Button(janela_principal, text='Fechar aplicação', command= janela_principal.destroy)

#layout
rotulo_moeda_origem.pack()
lista_moedas_origem.pack()
rotulo_moeda_destino.pack()
lista_moedas_destino.pack()
rotulo_valor_a_ser_convertido.pack()
entrada_valor_a_ser_convertido.pack()
botao_realizar_conversao.pack()
resultado.pack()
espaco_vazio.pack()
resultado_data_consulta.pack()
resultado_ultima_atualizacao_cambio.pack()
botao_limpar_campo.pack()
botao_fechar_aplicacao.pack()

janela_principal.mainloop()



"""
Observações:
A documentação da API disponibilizou o nome e as iniciais de todas as moedas em:https://economia.awesomeapi.com.br/xml/available/uniq

Elas foram colocadas em um excel, separadas do texto usando as funções =DIREITA / =ESQUERDA e depois
=UNIRTEXTO( ", ";VERDADEIRO;C1:C157) para montar uma só string contendo todas as moedas e separadas por vírgulas.

Obtendo a seguinte string:
AED,AFN,ALL,AMD,ANG,AOA,ARS,AUD,AZN,BAM,BBD,BDT,BGN,BHD,BIF,BND,BOB,BRL,BRLT,BSD,BTC,BWP,BYN,BZD,CAD,CHF,CHFRTS,CLP,CNH,CNY,COP,CRC,CUP,CVE,CZK,DJF,DKK,OGE,DOP,DZD,EGP,ETB,ETH,EUR,FJD,GBP,GEL,GHS,GMD,GNF,GTQ,HKD,HNL,HRK,HTG,HUF,IDR,ILS,INR,IQD,IRR,ISK,JMD,JOD,JPY,RTS,KES,KGS,KHR,KMF,KRW,KWD,KYD,KZT,LAK,LBP,LKR,LSL,LTC,LYD,MAD,MDL,MGA,MKD,MMK,MNT,MOP,MRO,MUR,MVR,MWK,MXN,MYR,MZN,NAD,NGN,GNI,LEL,NIO,NOK,NPR,NZD,OMR,PAB,PEN,PGK,PHP,PKR,PLN,PYG,QAR,RON,RSD,RUB,RUBTOD,RUBTOM,RWF,SAR,SCR,SDG,SDR,SEK,SGD,SOS,STD,SVC,SYP,SZL,THB,TJS,TMT,TND,TRY,TTD,TWD,TZS,UAH,UGX,USD,USDT,UYU,UZS,VEF,VND,VUV,XAF,XAGG,XBR,XCD,XOF,XPF,XRP,YER,ZAR,ZMK,ZWL,XAU



E o mesmo para o nome das moedas com os países:
Dirham dos Emirados,Afghani do Afeganistão,Lek Albanês,Dram Armênio,Guilder das Antilhas,Kwanza Angolano,Peso Argentino,Dólar Australiano,Manat Azeri,Marco Conversível,Dólar de Barbados,Taka de Bangladesh,Lev Búlgaro,Dinar do Bahrein,Franco Burundinense,Dólar de Brunei,Boliviano,Real Brasileiro,Real Brasileiro Turismo,Dólar das Bahamas,Bitcoin,Pula de Botswana,Rublo Bielorrusso,Dólar de Belize,Dólar Canadense,Franco Suíço,TS Franco Suíço,Peso Chileno,Yuan chinês offshore,Yuan Chinês,Peso Colombiano,Colón Costarriquenho,Peso Cubano,Escudo cabo-verdiano,Coroa Checa,Franco do Djubouti,Coroa Dinamarquesa,Dogecoin,Peso Dominicano,Dinar Argelino,Libra Egípcia,Birr Etíope,Ethereum,Euro,Dólar de Fiji,Libra Esterlina,Lari Georgiano,Cedi Ganês,Dalasi da Gâmbia,Franco de Guiné,Quetzal Guatemalteco,Dólar de Hong Kong,Lempira Hondurenha,Kuna Croata,Gourde Haitiano,Florim Húngaro,Rupia Indonésia,Novo Shekel Israelense,Rúpia Indiana,Dinar Iraquiano,Rial Iraniano,Coroa Islandesa,Dólar Jamaicano,Dinar Jordaniano,Iene Japonês,TS Iene Japonês,Shilling Queniano,Som Quirguistanês,Riel Cambojano,Franco Comorense,Won Sul-Coreano,Dinar Kuwaitiano,Dólar das Ilhas Cayman,Tengue Cazaquistanês,Kip Laosiano,Libra Libanesa,Rúpia de Sri Lanka,Loti do Lesoto,Litecoin,Dinar Líbio,Dirham Marroquino,Leu Moldavo,Ariary Madagascarense,Denar Macedônio,Kyat de Mianmar,Mongolian Tugrik,Pataca de Macau,Ouguiya Mauritana,Rúpia Mauriciana,Rufiyaa Maldiva,Kwacha Malauiana,Peso Mexicano,Ringgit Malaio,Metical de Moçambique,Dólar Namíbio,Naira Nigeriana,Naira Nigeriana,PARALLEL Naira Nigeriana,Córdoba Nicaraguense,Coroa Norueguesa,Rúpia Nepalesa,Dólar Neozelandês,Rial Omanense,Balboa Panamenho,Sol do Peru,Kina Papua-Nova Guiné,Peso Filipino,Rúpia Paquistanesa,Zlóti Polonês,Guarani Paraguaio,Rial Catarense,Leu Romeno,Dinar Sérvio,Rublo Russo,OD Rublo Russo,OM Rublo Russo,Franco Ruandês,Riyal Saudita,Rúpias de Seicheles,Libra Sudanesa,DSE,Coroa Sueca,Dólar de Cingapura,Shilling Somaliano,Dobra São Tomé/Príncipe,Colon de El Salvador,Libra Síria,Lilangeni Suazilandês,Baht Tailandês,Somoni do Tajiquistão,TMT,Dinar Tunisiano,Nova Lira Turca,Dólar de Trinidad,Dólar Taiuanês,Shilling Tanzaniano,Hryvinia Ucraniana,Shilling Ugandês,Dólar Americano,Dólar Americano,Peso Uruguaio,Som Uzbequistanês,Bolívar Venezuelano,Dong Vietnamita,Vatu de Vanuatu,Franco CFA Central,Prata,Brent Spot,Dólar do Caribe Oriental,Franco CFA Ocidental,Franco CFP,XRP,Riyal Iemenita,Rand Sul-Africano,Kwacha Zambiana,Dólar Zimbabuense,Ouro

"""
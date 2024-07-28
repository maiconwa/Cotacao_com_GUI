import requests
from tkinter import *


def exchange_rates():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dollar: {cotacao_dolar}
    Euro: {cotacao_euro}
    Bitcoin: {cotacao_btc}'''
    
    texto_cotacoes['text'] = texto


janela = Tk()
janela.title('Current exchange rates')
janela.geometry('280x200')

texto_orientacao = Label(janela, text='Click the button to view the exchange rates')
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text='Search Dollar/Euro/Bitcoin', command=exchange_rates)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_cotacoes = Label(janela, text='')
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()

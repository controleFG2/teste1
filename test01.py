from tkinter import *

janela = Tk()

janela.title('cotação atual')
janela.geometry('400x200')

texto_orientacao = Label(janela, text= 'clique no botão para ver as cotações das moedas')
texto_orientacao.pack(padx= 10, pady= 10)

botao = Button(janela, text= 'buscar coteções')
botao.pack(padx= 150, pady= 10)

texto_cotacoes = Label(janela, text= '')
texto_cotacoes.pack(padx= 10, pady= 10)

janela.mainloop()
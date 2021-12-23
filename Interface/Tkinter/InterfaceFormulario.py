from tkinter import *
from typing import Collection

janela = Tk()
janela.title('Formulário')
janela.geometry('450x120')

# FUNCAO DE RECEPÇÂO DA INFORMAÇÂO
def obter():
    nome = entry_nome.get()
    idade = entry_idade.get()
    pais = entry_pais.get()

    label_nome_out['text'] = nome
    label_idade_out['text'] = idade
    label_pais_out['text'] = pais

    # apaga o texto do Entry
    entry_nome.delete(0,END)
    entry_idade.delete(0,END)
    entry_pais.delete(0,END)

# INPUT
    # NOME
label_nome = Label(janela, width=10, text='Nome: ', font=('Arial 10'))
label_nome.grid(row=0, column=0)

entry_nome = Entry(janela, width=30, font=('Arial 10'))
entry_nome.grid(row=0, column=1, padx=10, pady=5)

    # IDADE
label_idade = Label(janela, width=10, text='Idade: ', font=('Arial 10'))
label_idade.grid(row=1, column=0)

entry_idade = Entry(janela, width=30, font=('Arial 10'))
entry_idade.grid(row=1, column=1, padx=10, pady=5)

    # PAIS
label_pais = Label(janela, width=10, text='País: ', font=('Arial 10'))
label_pais.grid(row=2, column=0)

entry_pais = Entry(janela, width=30, font=('Arial 10'))
entry_pais.grid(row=2, column=1, padx=10, pady=5)

# OUTPUT
label_nome_out = Label(janela, width=10, text='NOME', font=('Arial 10'))
label_nome_out.grid(row=0, column=2)

label_idade_out = Label(janela, width=10, text='IDADE', font=('Arial 10'))
label_idade_out.grid(row=1, column=2)

label_pais_out = Label(janela, width=10, text='PAIS', font=('Arial 10'))
label_pais_out.grid(row=2, column=2)

botao = Button(janela, command=obter, width=10, text='ENVIAR', relief=RAISED, bg='blue', fg='white')
botao.grid(row=3, column=1)

janela.mainloop()
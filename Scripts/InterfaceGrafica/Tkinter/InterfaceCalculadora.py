from tkinter import *
from tkinter import ttk

# colors
cor_01 = '#000'
cor_02 = '#fff'
cor_03 = '#'
cor_04 = '#ECEFF1'
cor_05 = '#FFAB40'

# janela
janela = Tk()
janela.title('Calculadora') # title => titulo da janela
janela.geometry('235x310') # geometry => argumentos de altura-largura da janela
janela.config(bg=cor_01)

# display de input
frame_tela = Frame(janela, width=235, height=50, bg=cor_01) # particiona a jananela
frame_tela.grid(row=0, column=0) # adiciona um grid

# display dos botoes
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#####
valores = ''
valor_texto = StringVar()
# funcoes de calculo
    # receber valores
def calcular(event):
    global valores # global => mantem os valores em metodo acessavel
    valores = valores + str(event) # soma os event's, mantendo os dados temporários
    valor_texto.set(valores) # acessa o StringVar para printar no app_label

    #calcular 
def calcular_result():
    global valores
    resultado = eval(valores)
    valor_texto.set(str(resultado))

    # limpar tela
def limpar_tela():
    global valores
    valores = ''
    valor_texto.set('')

# label
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cor_01, fg=cor_02)
app_label.place(x=0, y=0)

# botoes
    # linha 1
btn_01 = Button(frame_corpo, command=limpar_tela, text='C', width=11, height=2, bg=cor_04, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_01.place(x=0, y=0)
btn_02 = Button(frame_corpo, command=lambda:calcular('%'), text='%', width=5, height=2, bg=cor_04, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_02.place(x=118, y=0)
btn_03 = Button(frame_corpo, command=lambda:calcular('/'), text='/', width=5, height=2, bg=cor_05, fg=cor_02, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_03.place(x=177, y=0)

    # linha 2
btn_04 = Button(frame_corpo, command=lambda:calcular('7'), text='7', width=5, height=2, bg=cor_04, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_04.place(x=0, y=52)
btn_05 = Button(frame_corpo, command=lambda:calcular('8'), text='8', width=5, height=2, bg=cor_04, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_05.place(x=59, y=52)
btn_06 = Button(frame_corpo, command=lambda:calcular('9'), text='9', width=5, height=2, bg=cor_04, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_06.place(x=118, y=52)
btn_07 = Button(frame_corpo, command=lambda:calcular('*'), text='*', width=5, height=2, bg=cor_05, fg=cor_02, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_07.place(x=177, y=52)

    # linha 3
btn_08 = Button(frame_corpo, command=lambda:calcular('4'), text='4', width=5, height=2, bg=cor_04, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_08.place(x=0, y=104)
btn_09 = Button(frame_corpo, command=lambda:calcular('5'), text='5', width=5, height=2, bg=cor_04, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_09.place(x=59, y=104)
btn_10 = Button(frame_corpo, command=lambda:calcular('6'), text='6', width=5, height=2, bg=cor_04, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_10.place(x=118, y=104)
btn_11 = Button(frame_corpo, command=lambda:calcular('-'), text='-', width=5, height=2, bg=cor_05, fg=cor_02, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_11.place(x=177, y=104)

    # linha 4
btn_12 = Button(frame_corpo, command=lambda:calcular('1'), text='1', width=5, height=2, bg=cor_04, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_12.place(x=0, y=156)
btn_13 = Button(frame_corpo, command=lambda:calcular('2'), text='2', width=5, height=2, bg=cor_04, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_13.place(x=59, y=156)
btn_14 = Button(frame_corpo, command=lambda:calcular('3'), text='3', width=5, height=2, bg=cor_04, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_14.place(x=118, y=156)
btn_15 = Button(frame_corpo, command=lambda:calcular('+'), text='+', width=5, height=2, bg=cor_05, fg=cor_02, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_15.place(x=177, y=156)

    # linha 5
btn_16 = Button(frame_corpo, command=lambda:calcular('0'), text='0', width=11, height=2, bg=cor_04, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_16.place(x=0, y=208)
btn_17 = Button(frame_corpo, command=lambda:calcular('.'), text='.', width=5, height=2, bg=cor_04, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_17.place(x=118, y=208)
btn_18 = Button(frame_corpo, command=calcular_result, text='=', width=5, height=2, bg=cor_05, fg=cor_02, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_18.place(x=177, y=208)

janela.mainloop() # mainloop => cria a janela
from tkinter import *

janela = Tk()

cor = StringVar(janela)
cor.set("black")
janela.geometry('235x310')

l = Label(background=cor.get())
l.pack(fill='both',expand=True)

def pinta(): 
    l.config(background=cor.get())

for texto,valor in (
    ("preto","black"),
    ("vermelho","red"),
    ("azul","blue"), 
    ("verde","green"),
    ("rosa","pink"),
    ("amarelo","yellow"),
    ("cinza","grey"),
    ("violeta","violet"),
    ("laranja","orange")
): Radiobutton(text=texto,value=valor,variable=cor,command=pinta).pack(anchor=W)

janela.mainloop()
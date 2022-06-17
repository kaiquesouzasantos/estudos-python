import PySimpleGUI as sg
import random
import os

class PassGen:
    def __init__(self):
        sg.theme('Black')
        layout = [
            [sg.Text('Site/Software', size=(10,1)), sg.Input(key='site', size=(20,1))],
            [sg.Text('E-mail', size=(10,1)), sg.Input(key='usuario', size=(20,1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values = list(range(30)), key='total_chars', default_value=1, size=(3,1))],
            [sg.Output(size=(32,5))],
            [sg.Button('Gerar Senha')]

        ]

        self.janela = sg.Window('Password', layout=layout)

    def Iniciar(self):
        while True:
            event, valores = self.janela.read()
            if event == sg.WIN_CLOSED:
                break

            if event == 'Gerar Senha':

                self.nova_senha = self.gerar_senha(valores)
                self.Salvar(self.nova_senha, valores)
                print(self.nova_senha)

    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLONMPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$%&*()[]~/?|+=.,'
        chars = random.choices(char_list, k = int(valores['total_chars']))
        new_pass = ''.join(chars)

        return new_pass

    def Salvar(self, nova_senha, valores):
        nova_senha = self.nova_senha
        with open('senhas.txt','a',newline='') as arquivo:
            arquivo.write(f'Site: {valores["site"]}\nUsuario: {valores["usuario"]}\nNova Senha: {nova_senha}')
        print('Arquivo Salvo')

        
gen = PassGen()
gen.Iniciar()

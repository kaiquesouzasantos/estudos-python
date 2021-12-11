import PySimpleGUI as sg # pip install PySimpleGui
# pip install pyinstaller

class TelaPython():
    def __init__(self):
        # Tema
        sg.change_look_and_feel('DarkGrey2')

        # layout
        layout = [
            # size = tamanho 
            # key = nome da chave/atributo

            [sg.Text('Numero',size=(6,0)),sg.Input(size=(20,0),key='Numero')],
            [sg.Text('Limite',size=(6,0)),sg.Input(size=(20,0),key='Limite')],

            [sg.Button('Calcular')],

            [sg.Output(size=(40,12))]
        ]

        # Janela
        self.janela = sg.Window('Tabuada',element_justification='center',size=(300,300)).layout(layout)

    def Iniciar(self):
        while True:
            # Dados Extraidos
            self.button, self.values = self.janela.Read()

            # <varialvel> = self.values[<nome_da_key]
            numero = self.values['Numero']
            limite = self.values['Limite']
            numero = int(numero)
            limite = int(limite)

            # output na interface
            print("Tabuada do número ", numero)
            for valor in range(1,limite+1,1):
                print(str(numero) + " x " + str(valor) + " = " + str((numero*valor)))

tela = TelaPython()
tela.Iniciar()
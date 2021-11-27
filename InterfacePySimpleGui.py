import PySimpleGUI as sg # pip install PySimpleGui

class TelaPython():
    def __init__(self):
        # Tema
        sg.change_look_and_feel('DarkGrey2')

        # layout
        layout = [
            # size = tamanho 
            # key = nome da chave/atributo

            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0),key='Nome')],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0),key='Idade')],

            [sg.Text(' Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail',key='Gmail'),sg.Checkbox('Outlook',key='Outlook'),sg.Checkbox('Yahoo',key='Yahoo')],

            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim','cartoes',key='cartaoSim'),sg.Radio('Não','cartoes',key='cartaoNao')],

            [sg.Slider(range=(0,255),default_value=0,orientation='h',size=(15,20),key='sliderVelocidade')],

            [sg.Button('Enviar Dados')],

            [sg.Output(size=(30,20))]
        ]

        # Janela
        self.janela = sg.Window('Dados do Usuário').layout(layout)

    def Iniciar(self):
        while True:
            # Dados Extraidos
            self.button, self.values = self.janela.Read()

            # <varialvel> = self.values[<nome_da_key]
            nome = self.values['Nome']
            idade = self.values['Idade']
            gmail = self.values['Gmail']
            outlook = self.values['Outlook']
            yahoo = self.values['Yahoo']
            cartaoSim = self.values['cartaoSim']
            cartaoNao = self.values['cartaoNao']
            velocidadeScript = self.values['sliderVelocidade']

            # output na interface
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Aceita Gmail: {gmail}')
            print(f'Aceita Outlook: {outlook}')
            print(f'Aceita Yahoo: {yahoo}')
            print(f'Aceita Cartao {cartaoSim}')
            print(f'Nao Aceita Cartao {cartaoNao}')
            print(f'Velocidade do Script {velocidadeScript}')

tela = TelaPython()
tela.Iniciar()

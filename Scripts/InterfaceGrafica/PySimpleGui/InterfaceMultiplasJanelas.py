import PySimpleGUI as sg 

def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]

    return sg.Window('Login', layout=layout, finalize=True)

def janela_pedido():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('Pizza Pepperoni', key='pizza_001'),sg.Checkbox('Pizza Frango c/ Catupiry', key='pizza_002')],
        [sg.Button('Voltar'), sg.Button('Fazer Pedido')]
    ]

    return sg.Window('Pedido', layout=layout, finalize=True)

janela_01, janela_02 = janela_login(), None

while True:
    window, event, values = sg.read_all_windows()

    # fechar janela
    if window == janela_01 and event == sg.WIN_CLOSED:
        break

    # proxima janela
    if window == janela_01 and event == 'Continuar':
        janela_02 = janela_pedido()
        janela_01.hide()

    # janela anterior
    if window == janela_02 and event == 'Voltar':
        janela_02.hide() # hide() => oculta a janela
        janela_01.un_hide() # un_hide() => recupera a janela

    # verificação de tipo de pedido
    if window == janela_02 and event == 'Fazer Pedido':
        if values['pizza_001'] == True and values['pizza_002'] == True:
            sg.popup('Foram solicitados uma Pizza Pepperoni e uma Pizza Frango c/ Catupiry')
        elif values['pizza_001'] == True:
            sg.popup('Foram solicitados uma Pizza Pepperoni')
        elif values['pizza_002'] == True:
            sg.popup('Foram solicitados uma Pizza Frango c/ Catupiry')


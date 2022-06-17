import PySimpleGUI as sg

sg.ChangeLookAndFeel("Dark")

WIN_WIDTH = 90
WIN_HEIGTH = 25

arquivo_nome = None
arquivo_novo = "Novo        (CTRL+N)"
arquivo_abrir = "Abrir      (CTRL+O)"
arquivo_salvar = "Salvar      (CTRL+S)"

menu_layout = (
    ["Arquivo", [arquivo_novo, arquivo_abrir, arquivo_salvar, "Salvar como", "---", "Sair"]],
    ["Editar", ["Tornar caixa alta", "Tornar caixa baixa"]]
)

layout = [
    [sg.MenuBar(menu_layout)],
    [sg.Multiline(font=("Consolas", 12), text_color="white", size=(WIN_WIDTH, WIN_HEIGTH), key="_BODY_")]
]

window = sg.Window("Notepad",layout=layout,margins=(0, 0),resizable=True,return_keyboard_events=True,)
window.read(timeout=1)
window["_BODY_"].expand(expand_x=True, expand_y=True)


def novo_arquivo() -> str:
    window["_BODY_"].update(value="")
    arquivo_nome = None
    return arquivo_nome

def abrir_arquivo() -> str:
    try:
        arquivo_nome: str = sg.popup_get_file("Open File", no_window=True)
    except:
        return
    if arquivo_nome not in (None, "") and not isinstance(arquivo_nome, tuple):
        with open(arquivo_nome, "r") as f:
            window["_BODY_"].update(value=f.read())
    return arquivo_nome

def salvar_arquivo(arquivo_nome: str):
    if arquivo_nome not in (None, ""):
        with open(arquivo_nome, "w") as f:
            f.write(values.get("_BODY_"))
    else:
        salvar_arquivo_como()

def salvar_arquivo_como() -> str:
    try:
        arquivo_nome: str = sg.popup_get_file(
            "Save File",
            save_as=True,
            no_window=True,
            default_extension=".txt",
            file_types=(("Text", ".txt"),),
        )
    except:
        return
    if arquivo_nome not in (None, "") and not isinstance(arquivo_nome, tuple):
        with open(arquivo_nome, "w") as f:
            f.write(values.get("_BODY_"))
    return arquivo_nome

def tornar_caixa_baixa():
    window["_BODY_"].update(value=str(values["_BODY_"]).lower())

def tornar_caixa_alta():
    window["_BODY_"].update(value=str(values["_BODY_"]).upper())

while True:
    event, values = window.read()

    if event in (None, "Sair"):
        window.close()
        break
    if event in (arquivo_novo, "n:78"):
        arquivo_nome = novo_arquivo()
    if event in (arquivo_abrir, "o:79"):
        arquivo_nome = abrir_arquivo()
    if event in (arquivo_salvar, "s:83"):
        salvar_arquivo(arquivo_nome)
    if event in ("Save As",):
        arquivo_nome = salvar_arquivo_como()
    if event == "Tornar caixa alta":
        tornar_caixa_alta()
    if event == "Tornar caixa baixa":
        tornar_caixa_baixa()
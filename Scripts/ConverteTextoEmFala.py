#pip install pyttsx3 | Converte Texto em Fala

import pyttsx3 as ptk

pt = ptk.init()
pt.say(input("Digite o que devera ser falado: "))
pt.runAndWait()
pt.stop()
print("Processo finalizado!")



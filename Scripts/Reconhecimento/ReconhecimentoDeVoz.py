#pip install pyaudio | pip install SpeechRecognition | pip install os_sys | https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio -> pip install CaminhoDoArquivo 

import speech_recognition as sr
import os

def ouvir_microfone():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)

    try:
        frase = microfone.recognize_google(audio,language="pt-BR")
        print("Voce disse: "+frase)

        if "nagevador" in frase:
            os.system("start Chorme.exe")

    except sr.UnknownValueError:
        print("Não entedi")
        return frase

ouvir_microfone()

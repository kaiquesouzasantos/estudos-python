#pip install pyaudio | pip install SpeechRecognition | pip install os_sys | https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio -> pip install CaminhoDoArquivo 
#pip install pywhatkit | pip install opencv-python | Converte Texto em Manuscrito
#pip install pyttsx3 | Converte Texto em Fala

import speech_recognition as sr
import pywhatkit as kit
import cv2
import pyttsx3 as ptk

def ouvir_microfone():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        pti = ptk.init()
        pti.say("Diga alguma coisa:")
        pti.runAndWait()
        pti.stop()
        audio = microfone.listen(source)

    try:
        frase = microfone.recognize_google(audio,language="pt-BR")
        print("Voce disse: "+frase)

        texto = frase
        titulo = input("Digite o titulo: ")
        titulo = titulo+".png"
        kit.text_to_handwriting(texto ,save_to = titulo)
        img = cv2.imread(titulo)
        cv2.imshow(titulo,img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        pt = ptk.init()
        pt.say("Texto transcrito e convertido em manuscrito!")
        pt.runAndWait()
        pt.stop()

    except sr.UnknownValueError:
        print("Não entedi")
        
    return frase

ouvir_microfone()
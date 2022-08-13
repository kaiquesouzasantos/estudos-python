#pip install pywhatkit | pip install opencv-python | Converte Texto em Manuscrito

import pywhatkit as kit
import cv2

texto = input("Digite o texto: ")
titulo = input("Digite o titulo: ")
titulo = titulo+".png"
kit.text_to_handwriting(texto ,save_to = titulo)
img = cv2.imread(titulo)
cv2.imshow(titulo,img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Conversão realizada com sucesso!")
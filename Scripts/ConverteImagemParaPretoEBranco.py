#pip install Pillow | Converte imagem para preto e Branco

from PIL import Image

img = Image.open("imagem.png")
blackAndWhite = img.convert("L")
blackAndWhite.save("nomeDaImagemConvertida.png")
blackAndWhite.show()


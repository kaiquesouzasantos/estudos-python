#pip install python-barcode | Gera Código de Barras

from barcode import EAN13
from barcode.writer import ImageWriter

with open (r'D:\nomeDesejado.png','wb') as f:
    EAN13('12345678910113',writer=ImageWriter()).write(f)
    #necessita de 12 numbers
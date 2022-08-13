#pip install pyqrcode | pip install pypng | Gera QRCode

import pyqrcode
import png
from pyqrcode import QRCode

QRString = input('Link desejado: ')
url = pyqrcode.create(QRString)
url.png(r'D:\qr.png',scale=8)
print('QRCode gerado com sucesso!')
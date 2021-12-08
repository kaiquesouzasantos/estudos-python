#pip install translate | Traduz Texto

from translate import Translator

s = Translator(from_lang='english', to_lang='pt-br')
res = input('Digite o texto: ')
resp = s.translate(res)
print(resp)
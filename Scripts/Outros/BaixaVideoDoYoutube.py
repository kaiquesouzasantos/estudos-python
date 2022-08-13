#pip install pytube | Baixa Video do Youtube

from pytube import YouTube

link = input('Link do Video: ')
path = input('Diretorio de download: ')
yt = YouTube(link)

print('Titulo: ',yt.title)
print('Tamanho: ',yt.length, 'segundos')

ys = yt.streams.get_highest_resolution()

print('Baixando...')
ys.download(path)
print('Download completo!')
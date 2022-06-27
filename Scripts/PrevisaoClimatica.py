# pip install requests | pip install BeautifulSoup | previsao do tempo

import requests as rq
from bs4 import BeautifulSoup as bp

html = rq.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp").content
soup = bp(html, "html.parser")

resume = soup.find(class_='-gray _flex _align-center')
tempMin = soup.find(id='min-temp-1')
tempMax = soup.find(id='max-temp-1')

print(f"RESUMO: {resume}\nTEMPERATURA MIN: {tempMin}°C\nTEMPERATURA MAX: {tempMax}°C")

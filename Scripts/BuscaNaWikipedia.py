#pip install wikipedia | Busca na Wikipedia	

import wikipedia 

scan = input('Item para a pesquisa[sem espaços]: ')
result = wikipedia.summary(scan)
print(result)

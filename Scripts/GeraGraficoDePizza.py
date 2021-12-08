#pip install matplotlib | pip install numpy | Gera Grafico de Pizza

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,25,15]) #Valores
mylabels = ["Maça","Banana","Laranja","Melancia"] #Itens
myexplode = [0.2,0,0,0] #Margim

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show()
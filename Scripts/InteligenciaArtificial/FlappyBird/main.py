import os

from execucao.runIA import rodar 
from execucao.run import main

if __name__ == '__main__':
    # [1] - Flappy Bird com Ia
    # [2] - Flappy Bird 
    opcao = 1

    if opcao == 1:
        caminho = os.path.dirname(__file__)
        caminho_config = os.path.join(caminho, 'config/config.txt')
        rodar(caminho_config)
    elif opcao == 2:
        main()
    else:
        exit()
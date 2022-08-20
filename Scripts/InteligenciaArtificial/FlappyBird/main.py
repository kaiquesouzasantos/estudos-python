import os
import pygame

from classes.Botao import Botao
from execucao.runIA import rodar 
from execucao.run import main

TELA_LARGURA = 500
TELA_ALTURA = 800

LOOP = True
FPS = pygame.time.Clock()
TELA = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))

IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
TELA.blit(IMAGEM_BACKGROUND, (0, 0))

IMAGEM_RUN_IA = pygame.image.load('imgs/btn_ia.png').convert_alpha()
IMAGEM_RUN = pygame.image.load('imgs/btn_jogar.png').convert_alpha()

RUN_IA = Botao(50, 250, IMAGEM_RUN_IA, 0.8)
RUN = Botao(50, 400, IMAGEM_RUN, 0.8)

while LOOP:
    FPS.tick(60)

    if RUN_IA.click(TELA): 
        caminho = os.path.dirname(__file__)
        caminho_config = os.path.join(caminho, 'config/config.txt')
        rodar(caminho_config)
        LOOP = False
	
    if RUN.click(TELA): 
        main()
        LOOP = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            LOOP = False

    pygame.display.update()
pygame.quit()
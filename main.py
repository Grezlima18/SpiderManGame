import os
import pygame

pygame.init()
os.system("cls")
print("Começando o Jogo do Homem-Aranha!")

larguraDaTela = 800
alturaDaTela = 400
tamanhoDaTela = (larguraDaTela,alturaDaTela)

display = pygame.display.set_mode( tamanhoDaTela )
fps = pygame.time.Clock()
pygame.display.set_caption("Jogo do Homem-Aranha")


jogando = True

while jogando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False
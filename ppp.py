import pygame
import sys
pygame.init()

ancho,alto = 400,500

ventana = pygame.display.set_mode((ancho,alto))

negro = (0,0,0)

ventana.fill(negro)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

pygame.display.flip()

import pygame, sys
from pygame.locals import *
from Game import *

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bummbumm")

game = Game()

clock = pygame.time.Clock()  


while True:

    #### READ INPUT ###

    # check user events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #### UPDATE ###
    game.update()

    #### DRAW ###
    game.draw(displaysurface)

    # wait until next frame
    clock.tick(FPS)
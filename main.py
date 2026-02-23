import pygame
import sys
from grid import Grid
from blocks import *
pygame.init()

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption('TETRIS')

clock = pygame.time.Clock()

gameGrid = Grid()

block = IBlock()
gameGrid.printGrid()

darkBlue = (44, 44, 127)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # drawing
    screen.fill(darkBlue)
    gameGrid.draw(screen)
    block.draw(screen)
    pygame.display.update()
    clock.tick(60)


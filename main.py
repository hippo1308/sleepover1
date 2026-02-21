import pygame
import sys
from grid import Grid
pygame.init()

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption('TETRIS')

clock = pygame.time.Clock()

gameGrid = Grid()
gameGrid.grid[0][0] = 1
gameGrid.grid[3][5] = 4
gameGrid.grid[17][8] = 7


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
    pygame.display.update()
    clock.tick(60)


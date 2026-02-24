import pygame
import sys
from game import Game
pygame.init()

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption('TETRIS')

clock = pygame.time.Clock()

game = Game()

GAMEUPDATE = pygame.USEREVENT
pygame.time.set_timer(GAMEUPDATE, 300)

darkBlue = (44, 44, 127)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.moveLeft()
            if event.key == pygame.K_RIGHT:
                game.moveRight()
            if event.key == pygame.K_DOWN:
                game.moveDown()
            if event.key == pygame.K_SPACE:
                game.rotate()
        if event.type == GAMEUPDATE:
            game.moveDown()

    # drawing
    screen.fill(darkBlue)
    game.draw(screen)
    pygame.display.update()
    clock.tick(60)


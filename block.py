from colours import Colours
import pygame
from position import Position
class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cellSize = 30
        self.rowOffset = 0
        self.columnOffset = 0
        self.rotationState = 0
        self.colours = Colours.getCellColours()

    def move(self, rows, columns):
        self.rowOffset += rows
        self.columnOffset += columns

    def getCellPositions(self):
        tiles = self.cells[self.rotationState]
        movedTiles = []
        for position in tiles:
            position = Position(position.row+self.rowOffset, position.column+self.columnOffset)
            movedTiles.append(position)
        return movedTiles

    def rotate(self):
        self.rotationState += 1
        if self.rotationState == len(self.cells):
            self.rotationState = 0

    def undoRotation(self):
        self.rotationState -= 1
        if self.rotationState == -1:
            self.rotationState = len(self.cells) - 1


    def draw(self, screen):
        tiles = self.getCellPositions()
        for tile in tiles:
            tileRect = pygame.Rect(tile.column*self.cellSize+1, tile.row*self.cellSize+1,self.cellSize-1, self.cellSize-1)
            pygame.draw.rect(screen,self.colours[self.id], tileRect)



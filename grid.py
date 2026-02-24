import pygame
from colours import Colours


class Grid:
    def __init__(self):
        self.numRows = 20
        self.numCols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.numCols)] for i in range(self.numRows)]
        self.colours = Colours.getCellColours()

    def printGrid(self):
        for row in range(self.numRows):
            for column in range(self.numCols):
                print(self.grid[row][column], end='')
            print()

    def isInside(self, row, column):
        if row >= 0 and row < self.numRows and column >= 0 and column < self.numCols:
            return True
        return False

    def isEmpty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False

    def isRowFull(self,row):
        for column in range(self.numCols):
            if self.grid[row][column]== 0:
                return False
        return True
    def draw(self, screen):
        for row in range(self.numRows):
            for column in range(self.numCols):
                cellValue = self.grid[row][column]
                cellRect = pygame.Rect(column*self.cell_size+1, row*self.cell_size+1, self.cell_size-1, self.cell_size-1)
                pygame.draw.rect(screen, self.colours[cellValue], cellRect)


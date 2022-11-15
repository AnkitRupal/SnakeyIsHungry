import pygame
from constants import PIXELS

'''
    BODY Class
        The body class is the body of the snake. We create a list of these body elements
        to represent the whole body of the snake.
        The routines included are as follows:
            1) init : constructor
            2) draw : renders the body object to the display screen
'''
class Body:

    def __init__ (self, color, posX, posY):
        self.color = color
        self.posX = posX
        self.posY = posY
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.posX, self.posY, PIXELS, PIXELS))

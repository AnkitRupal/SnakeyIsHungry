import pygame
from constants import PIXELS, SQUARES
from colors import BG1, BG2

'''
    Background class
        The class initially make a chessboard type grid with two colours.
        The draw routine renders the background to the display screen.
'''
class Background:

    def draw(self,surface):
        for row in range(SQUARES):
            for col in range(SQUARES):
                if ((row+col)%2 == 0):
                    pygame.draw.rect(surface, BG2, (col*PIXELS, row*PIXELS, PIXELS, PIXELS))
                else:
                    pygame.draw.rect(surface, BG1, (col*PIXELS, row*PIXELS, PIXELS, PIXELS))
        return 

import pygame
import random
from constants import WIDTH, HEIGHT, PIXELS
from colors import RED

'''
    APPLE CLASS
        The routines in this class include:
            1) init  : constructor of the Apple object
            2) spawn : create an apple object at a random place
            3) draw  : render the object at the display screen
'''
class Apple:

    def __init__(self):
        self.color = RED
        self.spawn()
    
    def spawn(self):
        self.posX = random.randrange(0, WIDTH, PIXELS)
        self.posY = random.randrange(0, HEIGHT, PIXELS)
    
    def draw(self,surface):
        pygame.draw.rect(surface, self.color, (self.posX, self.posY, PIXELS, PIXELS))

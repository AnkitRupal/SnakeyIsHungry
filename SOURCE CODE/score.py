import pygame
from colors import BLACK

'''
    SCORE Class
        Updates the score of the player
        The routines included in this class: 
            1) init : constructor
            2) increaseScore : Increments the score of the player
            3) reset : sets score to zero
            4) show : renders the score label on the TOP-LEFT portion of the display screen
'''
class Score:

    def __init__(self):
        self.points = 0
        self.font = pygame.font.SysFont('monospace', 30, bold = False)
    
    def increaseScore(self):
        self.points += 1
    
    def reset(self):
        self.points = 0
    
    def show(self,surface):
        label = self.font.render('Score : ' + str(self.points), 1, BLACK)
        surface.blit(label, (5,5))

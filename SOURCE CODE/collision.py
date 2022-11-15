import math
from constants import PIXELS

'''
    COLLISION Class
        The collision detects two events:
            1) Eating of an apple   : Collision between Snake and Apple 
            2) Snake bitting itself : Collision between Snake and its Body
'''
class Collision:
    # Eating of the Apple
    def Snake__And__Apple(self,snake,apple):
        dist = math.sqrt( math.pow((snake.headX - apple.posX), 2) +  math.pow((snake.headY - apple.posY), 2))
        return dist < PIXELS
    
    # Snake bitting itself
    def Snake__And__Body(self,snake):
        for body in snake.bodies:
            dist = math.sqrt( math.pow((snake.headX - body.posX), 2) +  math.pow((snake.headY - body.posY), 2))
            if dist < PIXELS:
                return True
        return False

import pygame
import random
from constants import WIDTH, HEIGHT, PIXELS
from colors import BLUE
from body import Body

'''
    SNAKE Class
        The main object in the game. The snake class contains color,
        head positions, bodies list, body colour and movement state.
        
        Data Types:
            1) color : color of the snake
            2) headX : X position of the snake head
            3) headY : Y position of the snake's head
            4) bodies : a list of body objects
            5) body_color : the initial blue configuration of the snake's body color
            6) state : depicts the movement of the snake 
        
        Routines:
            1) init : constructor
            2) draw : renders the snake object to the display screen
            3) move_body : routine to help with the movement of the snake
            4) add_body : appends a body object to the bodies list
            5) move_head : routine to help with the movement of the snake's head
            6) die : destructor
'''
class Snake:
    # init routine -> constructor
    def __init__(self):
        self.color = BLUE
        self.headX = random.randrange(0, WIDTH, PIXELS)
        self.headY = random.randrange(0, HEIGHT, PIXELS)
        self.bodies = []
        self.body_color = 50
        self.state = "STOP" # STOP,UP,DOWN,LEFT,RIGHT
    
    # draw routine -> renders the snake object to the display screen
    def draw(self,surface):
        pygame.draw.rect(surface, self.color, (self.headX, self.headY, PIXELS, PIXELS))
        for body in self.bodies:
            body.draw(surface)
    
    # move_body routine -> routine to help with the movement of the snake
    def move_body(self):
        if len(self.bodies) > 0:
            for i in range(len(self.bodies)-1, 0, -1):
                self.bodies[i].posX = self.bodies[i-1].posX
                self.bodies[i].posY = self.bodies[i-1].posY
            self.bodies[0].posX = self.headX
            self.bodies[0].posY = self.headY
    
    # add_body routine -> appends a body object to the bodies list
    def add_body(self):
        if self.body_color != 250:
            self.body_color = (self.body_color + 10)
        body = Body((0, 0, self.body_color) , self.headX, self.headY)
        self.bodies.append(body)

    # move_head routine -> routine to help with the movement of the snake's head
    def move_head(self):
        if self.state == "UP":
            self.headY = (self.headY - PIXELS)%HEIGHT
        elif self.state == "DOWN":
            self.headY = (self.headY + PIXELS)%HEIGHT
        elif self.state == "LEFT":
            self.headX = (self.headX - PIXELS)%WIDTH
        elif self.state == "RIGHT":
            self.headX = (self.headX + PIXELS)%WIDTH
    
    # die routine -> destructor
    def die(self):
        self.headX = random.randrange(0, WIDTH, PIXELS)
        self.headY = random.randrange(0, HEIGHT, PIXELS)
        self.bodies = []
        self.body_color = 50
        self.state = "STOP"

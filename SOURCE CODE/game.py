'''
    IMPORTING ALL NECESSARY FILES AND LIBRARIES
        Two libraries are used:
            1) pygame : for GUI and the framework of the game
            2) sys : for giving exit command to OS.
        Six additional files are used which contains the implementation of several classes.
'''
import pygame
import sys
from constants import WIDTH, HEIGHT
from background import Background
from apple import Apple
from snake import Snake
from collision import Collision
from score import Score


'''
    The Standard funtion containing the MAINLOOP of the Game.
    All the Rendering, input and subroutine calling is done here.
'''
def main():
    #INITIALIZATION
    pygame.init()
    window = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("SNAKE GAME")

    #OBJECTS
    snake = Snake()
    apple = Apple()
    background = Background()
    collision = Collision()
    score = Score()

    #MAINLOOP
    while True:
        background.draw(window)
        snake.draw(window)
        apple.draw(window)
        score.show(window)

        '''
            Event Loop to catch the inputs from the user
            The following events are captured:
                1) exit - click
                2) down - key
                3) up - key
                4) left - key
                5) right - key
                6) space - key
        '''
        for event in pygame.event.get():
            # exit - click
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                # down - key
                if event.key == pygame.K_UP:
                    if snake.state != "DOWN":
                        snake.state = "UP"
                # up - key
                elif event.key == pygame.K_DOWN:
                    if snake.state != "UP":
                        snake.state = "DOWN"
                # left - key
                elif event.key == pygame.K_LEFT:
                    if snake.state != "RIGHT":
                        snake.state = "LEFT"
                #right - key
                elif event.key == pygame.K_RIGHT:
                    if snake.state != "LEFT":
                        snake.state = "RIGHT"
                # space - key
                elif event.key == pygame.K_SPACE:
                    snake.state = "STOP"
                else:
                    pass
        
        '''
            CAPTURING EVENTS -> EATING APPLE AND BITTING ITSELF
                We capture the events by considering a collision between 'objects' of different classes
                The following collisions are possible:

                    1) Snake and Apple : Eating of the apple. 
                        a) Increment Score
                        b) Increase Length of the snake
                        c) Create a new apple at a random position

                    2) Snake and Body : Bitting itself -> The game must stop. Additional tasks needs to 
                                        be performed.
                        a) Call destructor for the snake object
                        b) Reset score
                        c) Create a new apple at a random position
                        
        '''


        '''
            Collision between a Snake and an Apple
                Snake and Apple : Eating of the apple. 
                    a) Increment Score
                    b) Increase Length of the snake
                    c) Create a new apple at a random position
        '''
        if collision.Snake__And__Apple(snake, apple):
            apple.spawn()
            snake.add_body()
            score.increaseScore()
        
        '''
            MAKING MOVEMENT OF THE SNAKE
                We perform movement 'before checking' collision between snake and its body 
                because the new body is formed at the head position and it causes a collision, 
                making the game end as soon as the snake eats an apple'
        '''
        if snake.state != "STOP":
            snake.move_body()
            snake.move_head()     
        
        '''
            Collision between snake and its body
                Snake and Body : Bitting itself -> The game must stop. Additional tasks needs to be performed.
                    a) Call destructor for the snake object
                    b) Reset score
                    c) Create a new apple at a random position
        '''
        if collision.Snake__And__Body(snake):
            snake.die()
            apple.spawn()
            score.reset()
        
        # Adding delay to slow down the movement of the snake -> current delay of 95 ms
        pygame.time.delay(95)   
        
        # Updating the Game screen -> Already made changes in this iteration, display changes
        pygame.display.update()
    

if __name__ == "__main__":
    main()
# end of program
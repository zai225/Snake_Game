import pygame
from pygame.locals import *
import time

SIZE = 40

class Apple:
    def __init__(self,parent_screen,length):
        self.image = pygame.image.load("C:\\zaidd\\Snake_Game\\apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image,(self.x, self.y))
        pygame.display.flip()


class Snake:
    def __init__(self, parent_screen, lenght):
        self.lenght = lenght
        self.parent_screen = parent_screen
        self.block = pygame.image.load("C:\\zaidd\\Snake_Game\\block.jpg").convert()
        self.x = [SIZE]*lenght
        self.y = [SIZE]*lenght
        self.direction = 'down' 

    def move_up(self):
       self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def draw(self):
        self.parent_screen.fill((36, 28, 31))
        for i in range(self.lenght):
            self.parent_screen.blit(self.block,(self.x[i], self.y[i]))
        pygame.display.flip()

    def walk(self):
        for i in range(self.lenght-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction =='left':
            self.x[0] -= SIZE
        if self.direction =='right':
            self.x[0] += SIZE
        if self.direction =='up':
            self.y[0] -= SIZE
        if self.direction =='down':
            self.y[0] += SIZE

        self.draw()

    

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))
        self.snake = Snake(self.surface, 6)
        self.snake.draw()
        self.apple = Apple(self.surface,1)
        self.apple.draw()

    def run (self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()
                
                elif event.type == pygame.QUIT:
                    running = False

            self.snake.walk()
            self.apple.draw()
             
            time.sleep(0.3)      

if __name__ == "__main__":
    game = Game()
    game.run()
    


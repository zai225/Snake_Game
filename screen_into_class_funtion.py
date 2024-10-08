import pygame
from pygame.locals import *

class Snake:
    def __init__(self, surface):
        self.parent_screen = surface
        self.block = pygame.image.load("C:\\zaidd\\Snake_Game\\block.jpg").convert()
        self.x = 100 
        self.y = 100
    
    def move_up(self):
        self.y -= 10
        self.draw()

    def move_down(self):
        self.y += 10
        self.draw()

    def move_left(self):
        self.x -= 10
        self.draw()

    def move_right(self):
        self.x += 10
        self.draw()

    def draw(self):
        self.parent_screen.fill((36, 28, 31))
        self.parent_screen.blit(self.block,(self.x, self.y))
        pygame.display.flip()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))
        self.surface.fill((71, 93, 110))
        self.snake = Snake(self.surface)
        self.snake.draw()

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


if __name__ == "__main__":
    game = Game()
    game.run()
    




















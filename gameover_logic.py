import pygame
from pygame.locals import *
import time
import random

SIZE = 40
BACKGROUND_COLOR = (36, 28, 31)

class Apple:
    def __init__(self,parent_screen,):
        self.image = pygame.image.load("C:\\zaidd\\Snake_Game\\apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image,(self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0,19)*SIZE
        self.y = random.randint(0,14)*SIZE

class Snake:
    def __init__(self, parent_screen, lenght):
        self.lenght = lenght
        self.parent_screen = parent_screen
        self.block = pygame.image.load("C:\\zaidd\\Snake_Game\\block.jpg").convert()
        self.x = [SIZE]*lenght
        self.y = [SIZE]*lenght
        self.direction = 'down' 

    def increase_length(self):
        self.lenght+=1
        self.x.append(-1)
        self.y.append(-1)

    def move_up(self):
       self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def draw(self):
        self.parent_screen.fill((BACKGROUND_COLOR))
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
        self.surface = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Snake Game')
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False
    
    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        #snake colliding with apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

         #snake colliding itself
        for i in range(3,self.snake.lenght):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i],self.snake.y[i]):
                raise "Collison Occured"

    #making a new surface window for the game_over page
    def show_game_over(self):
        self.surface.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont('Arial', 30)
        line1 = font.render(f"Game is over! Your Score is {self.snake.lenght}", True,(255,255,255))
        self.surface.blit(line1, (200,300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255,255,255))
        self.surface.blit(line2, (200,350))
        
        pygame.display.flip()

    def display_score(self):
        font = pygame.font.SysFont('Arial', 30)
        score = font.render(f" Score: {self.snake.lenght}", True,(255,255,255))
        self.surface.blit(score, (680,20))

    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)

    def run (self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False

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
            
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()
            
            time.sleep(0.3)      

if __name__ == "__main__":
    game = Game()
    game.run()
    
    


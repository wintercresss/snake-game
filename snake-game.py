import pygame, random
from pygame.math import Vector2


class FRUIT:
    def __init__(self):  # create x and y position
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    
    def draw_fruit(self): # create and draw rectangle
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size) # x, y, width, height
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect) #surface, color, rectangle (temp color for now)

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
    
    def draw_snake(self):
        for block in self.body: # create rectangle from position and draw
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            snake_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (183, 191, 122), snake_rect)





pygame.init()

cell_size = 40 # using cells to mimic a grid
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size , cell_number * cell_size)) # width, height
pygame.display.set_caption("Snake Game!")
clock = pygame.time.Clock()
running = True

fruit = FRUIT()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((175, 215, 70)) # green background color
    fruit.draw_fruit()

    
        
    pygame.display.update()
    clock.tick(60)



pygame.quit()
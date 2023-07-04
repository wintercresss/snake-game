import pygame
from pygame.math import Vector2


class FRUIT:
    def __init__(self):  # create x and y position
        self.x = 5
        self.y = 4
        self.pos = Vector2(self.x, self.y)

    
    def draw_fruit(self): # create and draw rectangle
        fruit_rect = pygame.Rect(self.pos.x, self.pos.y, cell_size, cell_size) # x, y, width, height
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect) #surface, color, rectangle (temp color for now)




pygame.init()

cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size , cell_number * cell_size)) # width, height
pygame.display.set_caption("Snake Game!")
clock = pygame.time.Clock()
running = True



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((175, 215, 70)) # green background color
    

    
        
    pygame.display.update()
    clock.tick(60)



pygame.quit()
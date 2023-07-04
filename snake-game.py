import pygame, random
from pygame.math import Vector2


class FRUIT:
    def __init__(self):  # create x and y position
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    
    def draw_fruit(self): # create and draw fruit
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size) # x, y, width, height
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect) #surface, color, rectangle (temp color for now)

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0) # temporary direction (moving to right), add player input later
    
    def draw_snake(self):
        for block in self.body: # create rectangle from position and draw
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            snake_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (183, 111, 122), snake_rect)
    
    def move_snake(self):
        body_copy = self.body[:-1] # copies every item in the list except for the last one
        body_copy.insert(0, body_copy[0] + self.direction) # location of new head
        self.body = body_copy[:] # update body to new list

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    def update(self):
        self.snake.move_snake()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()


pygame.init()

cell_size = 40 # using cells to mimic a grid
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size , cell_number * cell_size)) # width, height
pygame.display.set_caption("Snake Game!")
clock = pygame.time.Clock()
running = True


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150) # make event trigger every 150 miliseconds (for moving snake)

main_game = MAIN()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN: # check for input on keyboard
            if event.key == pygame.K_UP: # change direction depending on input
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1, 0)


    screen.fill((175, 215, 70)) # green background color
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)



pygame.quit()
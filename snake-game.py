import pygame, random, sys
from pygame.math import Vector2


class FRUIT:
    def __init__(self):  # create x and y position
        self.randomize()

    def draw_fruit(self): # create and draw fruit
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size) # x, y, width, height
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0) # temporary direction (moving to right), add player input later
        self.new_block = False
    
    def draw_snake(self):
        for block in self.body: # create rectangle from position and draw
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            snake_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (183, 111, 122), snake_rect)
    
    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:] # copy every block (since new block is being added)
            body_copy.insert(0, body_copy[0] + self.direction) # location of new head
            self.body = body_copy[:] # update body to new list
            self.new_block = False # done with adding new block
        
        else:
            body_copy = self.body[:-1] # copies every item in the list except for the last one
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
    
    def add_block(self):
        self.new_block = True


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]: # if the head of the snake collides with the fruit
            self.fruit.randomize() # make new fruit spawn in new location
            self.snake.add_block()

    def check_fail(self):
        if (not 0 <= self.snake.body[0].x < cell_number) or (not 0 <= self.snake.body[0].y < cell_number): # if the head of the snake is out of the grid
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]: # if the head of snake collides with any part of its body, lose
                self.game_over()

    
    def game_over(self):
        pygame.quit()
        sys.exit()


pygame.init()
cell_size = 40 # using cells to mimic a grid
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size , cell_number * cell_size)) # width, height
pygame.display.set_caption("Snake Game!")
clock = pygame.time.Clock()
apple = pygame.image.load('Graphics/apple.png').convert_alpha()



SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150) # make event trigger every 150 miliseconds (for moving snake)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN: # check for input on keyboard
            if event.key == pygame.K_UP: # change direction depending on input
                if main_game.snake.direction.y != 1: # make snake unable to reverse into itself
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)


    screen.fill((175, 215, 70)) # green background color
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)




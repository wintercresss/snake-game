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

        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()

    
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()


        for index, block in enumerate(self.body): 
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)


            if index == 0: # head of snake
                screen.blit(self.head, block_rect)
            elif index == len(self.body)-1: # tail of snake (last item)
                screen.blit(self.tail, block_rect)
            else:
                prev_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block

                if prev_block.x == next_block.x: # x didn't move, snake has gone purely vertically (no turn)
                    screen.blit(self.body_vertical, block_rect)
                elif prev_block.y == next_block.y: # x didn't move, snake has gone purely horizontally (no turn)
                    screen.blit(self.body_horizontal, block_rect)
                else: # there is a turn (corner)
                    if (prev_block.x == -1 and next_block.y == -1) or (prev_block.y == -1 and next_block.x == -1): # have to account for both possible turns
                        screen.blit(self.body_tl, block_rect)
                    elif (prev_block.x == -1 and next_block.y == 1) or (prev_block.y == 1 and next_block.x == -1):
                        screen.blit(self.body_bl, block_rect)
                    elif (prev_block.x == 1 and next_block.y == -1) or (prev_block.y == -1 and next_block.x == 1):
                        screen.blit(self.body_tr, block_rect)
                    elif (prev_block.x == 1 and next_block.y == 1) or (prev_block.y == 1 and next_block.x == 1):
                        screen.blit(self.body_br, block_rect)


    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0] # find the direction that the snake is going

        if head_relation == Vector2(1, 0): self.head = self.head_left
        elif head_relation == Vector2(-1, 0): self.head = self.head_right
        elif head_relation == Vector2(0, 1): self.head = self.head_up
        elif head_relation == Vector2(0, -1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-1] - self.body[-2] # find direction that the tail is going

        if tail_relation == Vector2(1, 0): self.tail = self.tail_right
        elif tail_relation == Vector2(-1, 0): self.tail = self.tail_left
        elif tail_relation == Vector2(0, 1): self.tail = self.tail_down
        elif tail_relation == Vector2(0, -1): self.tail = self.tail_up
    
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
        self.draw_grass()
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
    
    def draw_grass(self): # create checkerboard pattern to the background
        grass_color = (167, 209, 61) # dark green color

        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size) # x, y, width, height
                        pygame.draw.rect(screen,grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size) # x, y, width, height
                        pygame.draw.rect(screen,grass_color, grass_rect)



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




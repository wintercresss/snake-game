import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Snake Game!")
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    pygame.display.update()
    clock.tick(60)



pygame.quit()
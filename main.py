import pygame

pygame.init()

width, height = 1000, 600
wn = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong_But_Better")
run = True

#Main loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


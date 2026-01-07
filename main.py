import pygame

pygame.init()

width, height = 1000, 600
wn = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong_But_Better")
run = True

#color
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

#for the ball
radius = 15
ball_x, ball_y = width/2 - radius, height/2 - radius
ball_vel_x, ball_vel_y = 0.7, 0.7

#paddle dimensions
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = height/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, width - (100 - paddle_width/2)

#Main loop
while run:
    wn.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #ball's movement controls
    if ball_y <= 0 + radius or ball_y >= height - radius:
        ball_vel_y += -1

    #movement
    ball_x += ball_vel_x
    ball_y += ball_vel_y

    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height) )
    pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height) )
    pygame.display.update() 


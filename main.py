import pygame
import random

pygame.init()

gadget_pair = 1
ch = int(input("Enter your choice for gadget pair"))
if ch == 1:
    gadget_pair = 1
elif ch == 2:
    gadget_pair = 2

width, height = 1000, 600
wn = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong_But_Better")
run = True
player_1 = player_2 = 0
direction = [0, 1]
angle = [0, 1, 2]

game_over = False
winner = None


#color
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#reset game
def reset_game():
    global ball_x, ball_y, ball_vel_x, ball_vel_y
    global dummy_ball_x, dummy_ball_y, dummy_ball_vel_x, dummy_ball_vel_y
    global left_paddle_y, right_paddle_y
    global second_left_paddle_y, second_right_paddle_y
    global left_gadget, right_gadget
    global left_gadget_remaining, right_gadget_remaining
    global player_1, player_2
    global game_over, winner

    player_1 = 0
    player_2 = 0

    ball_x, ball_y = width / 2, height / 2
    dummy_ball_x, dummy_ball_y = width / 2, height / 2

    ball_vel_x = random.choice([-1, 1]) * 0.7
    ball_vel_y = random.choice([-1, 1]) * 0.7
    dummy_ball_vel_x = ball_vel_x
    dummy_ball_vel_y = ball_vel_y

    left_paddle_y = right_paddle_y = height / 2 - paddle_height / 2
    second_left_paddle_y = second_right_paddle_y = height / 2 - paddle_height / 2

    left_gadget = right_gadget = 0
    left_gadget_remaining = right_gadget_remaining = 5

    game_over = False
    winner = None


#for the ball
radius = 15
ball_x, ball_y = width/2 - radius, height/2 - radius
ball_vel_x, ball_vel_y = 0.7, 0.7
#for the dummy ball
dummy_ball_x, dummy_ball_y = width/2 - radius, height/2 - radius
dummy_ball_vel_x, dummy_ball_vel_y = 0.7, 0.7


#paddle dimensions
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = height/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, width - (100 - paddle_width/2)
right_paddle_vel = left_paddle_vel = 0
#second paddle
second_left_paddle_y = second_right_paddle_y = height/2 - paddle_height/2
second_left_paddle_x, second_right_paddle_x = 100 - paddle_width/2, width - (100 - paddle_width/2)
second_right_paddle_vel = second_left_paddle_vel = 0

#gadgets
left_gadget = right_gadget = 0
left_gadget_remaining = right_gadget_remaining = 5

#Main loop
while run:
    wn.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_paddle_vel = -0.9
                second_right_paddle_vel = -0.9
            if i.key == pygame.K_DOWN:
                right_paddle_vel = 0.9
                second_right_paddle_vel = 0.9
            if i.key == pygame.K_RIGHT and right_gadget_remaining > 0:
                right_gadget = 1
            if i.key == pygame.K_LEFT and right_gadget_remaining > 0:
                right_gadget = 2
            if i.key == pygame.K_w:
                left_paddle_vel = -0.9
                second_left_paddle_vel = -0.9
            if i.key == pygame.K_s:
                left_paddle_vel = 0.9
                second_left_paddle_vel = 0.9
            if i.key == pygame.K_d and left_gadget_remaining > 0:
                left_gadget = 1
            if i.key == pygame.K_a and left_gadget_remaining > 0:
                left_gadget = 2
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_r and game_over:
                    reset_game()


        if i.type == pygame.KEYUP:
            second_right_paddle_vel = 0
            right_paddle_vel = 0
            second_left_paddle_vel = 0
            left_paddle_vel = 0

    # ball's movement controls
    if ball_y <= 0 + radius or ball_y >= height - radius:
        ball_vel_y *= -1
    if dummy_ball_y <= 0 + radius or dummy_ball_y >= height - radius:
        dummy_ball_vel_y *= -1

    if ball_x >= width - radius:
        player_1 += 1
        ball_x, ball_y = width/2 - radius, height/2 - radius
        dummy_ball_x, dummy_ball_y = width/2 - radius, height/2 - radius
        second_left_paddle_y = left_paddle_y
        second_right_paddle_y = right_paddle_y
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -1.4, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = -1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.7, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = -0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.7, 1.4
                dummy_ball_vel_y, dummy_ball_vel_x = -0.7, 1.4

        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 1.4, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = 1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.7, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = 0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.7, 1.4
                dummy_ball_vel_y, dummy_ball_vel_x = 0.7, 1.4
        ball_vel_x *= -1 
        dummy_ball_vel_x *= -1 

    if ball_x <= 0 + radius:
        player_2 += 1
        ball_x, ball_y = width/2 - radius, height/2 - radius
        dummy_ball_x, dummy_ball_y = width/2 - radius, height/2 - radius
        second_right_paddle_y = right_paddle_y
        second_left_paddle_y = left_paddle_y
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -1.4, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = -1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.7, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = -0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.7, 1.4
                dummy_ball_vel_y, dummy_ball_vel_x = -0.7, 1.4

        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 1.4, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = 1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.7, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = 0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.7, 1.4
                dummy_ball_vel_y, dummy_ball_vel_x = 0.7, 1.4
        

    #paddle's movement controls
    if left_paddle_y >= height - paddle_height:
        left_paddle_y = height - paddle_height
    if left_paddle_y <= 0:
        left_paddle_y = 0
    if right_paddle_y >= height - paddle_height:
        right_paddle_y = height - paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0
    #second paddle's movement controls
    if second_left_paddle_y >= height - paddle_height:
        second_left_paddle_y = height - paddle_height
    if second_left_paddle_y <= 0:
        second_left_paddle_y = 0
    if second_right_paddle_y >= height - paddle_height:
        second_right_paddle_y = height - paddle_height
    if second_right_paddle_y <= 0:
        second_right_paddle_y = 0

    #paddle Collisions
    #left paddle
    if second_left_paddle_y == left_paddle_y:
        if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
            if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                ball_x = left_paddle_x + paddle_width
                dummy_ball_x = left_paddle_x + paddle_width
                ball_vel_x *= -1
                dummy_ball_vel_x *= -1

    if second_left_paddle_y != left_paddle_y:
        if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
            if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                ball_x = left_paddle_x + paddle_width
                dummy_ball_x = left_paddle_x + paddle_width
                ball_vel_x *= -1
                dummy_ball_vel_x *= -1

        if second_left_paddle_x <= ball_x <= second_left_paddle_x + paddle_width:
            if second_left_paddle_y <= ball_y <= second_left_paddle_y + paddle_height:
                ball_x = left_paddle_x + paddle_width
                dummy_ball_x = left_paddle_x + paddle_width
                ball_vel_x *= -1
                dummy_ball_vel_x *= -1
    
    #right paddle
    if second_right_paddle_y == right_paddle_y:
        if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
            if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                ball_x = right_paddle_x
                dummy_ball_x = right_paddle_x
                ball_vel_x *= -1
                dummy_ball_vel_x *= -1

    if second_right_paddle_y != right_paddle_y:
        if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
            if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                ball_x = right_paddle_x
                dummy_ball_x = right_paddle_x
                ball_vel_x *= -1
                dummy_ball_vel_x *= -1

        if second_right_paddle_x <= ball_x <= second_right_paddle_x + paddle_width:
            if second_right_paddle_y <= ball_y <= second_right_paddle_y + paddle_height:
                ball_x = right_paddle_x
                dummy_ball_x = right_paddle_x
                ball_vel_x *= -1
                dummy_ball_vel_x *= -1

    #gadgets in action 
    #boost & teleport 
    if gadget_pair == 1:
        if left_gadget == 1:
            if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
                if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                    ball_x = left_paddle_x + paddle_width
                    ball_vel_x *= -3.5
                    dummy_ball_vel_x *= -3.5
                    left_gadget = 0
                    left_gadget_remaining -= 1
        elif left_gadget == 2:
            left_paddle_y = ball_y
            left_gadget = 0
            left_gadget_remaining -= 1

        if right_gadget == 1:
            if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
                if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                    ball_x = right_paddle_x
                    ball_vel_x *= 3.5
                    dummy_ball_vel_x *= 3.5
                    right_gadget = 0
                    right_gadget_remaining -= 1

        elif right_gadget == 2:
            right_paddle_y = ball_y
            right_gadget = 0
            right_gadget_remaining -= 1

    elif gadget_pair == 2:
        if left_gadget == 1:
            if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
                if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                    ball_x = left_paddle_x + paddle_width
                    dummy_ball_x = left_paddle_x + paddle_width
                    ball_vel_x *= -1
                    dummy_ball_vel_x *= -1
                    dummy_ball_vel_y *= -1
                    left_gadget = 0
                    left_gadget_remaining -= 1
        
        elif left_gadget == 2:
            second_left_paddle_y = left_paddle_y + 200
            left_gadget = 0
            left_gadget_remaining -= 1

        if right_gadget == 1:
            if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
                if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                    ball_x = right_paddle_x
                    dummy_ball_x = right_paddle_x
                    ball_vel_x *= -1
                    dummy_ball_vel_x *= -1
                    dummy_ball_vel_y *= -1 
                    right_gadget = 0
                    right_gadget_remaining -= 1 
        
        elif right_gadget == 2:
            second_right_paddle_y = right_paddle_y + 200
            right_gadget = 0
            right_gadget_remaining -= 1


    #movement
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    dummy_ball_x += dummy_ball_vel_x
    dummy_ball_y += dummy_ball_vel_y
    right_paddle_y += right_paddle_vel
    left_paddle_y += left_paddle_vel
    second_left_paddle_y += second_left_paddle_vel
    second_right_paddle_y += second_right_paddle_vel

    #scoreboard    
    font = pygame.font.SysFont('callibri', 32)
    score_1 = font.render("Plaayer_1:" + str (player_1), True, WHITE)
    wn.blit(score_1,(25,25))
    score_2 = font.render("Plaayer_2:" + str (player_2), True, WHITE)
    wn.blit(score_2,(825,25))
    gad_left_1 = font.render("Gad Left: " + str(left_gadget_remaining), True, WHITE)
    wn.blit(gad_left_1, (25,65))
    gad_left_2 = font.render("Gad Left: " + str(right_gadget_remaining), True, WHITE)
    wn.blit(gad_left_2, (825,65))


    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height) )
    pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height) )

    #dummy ball
    pygame.draw.circle(wn, BLUE, (dummy_ball_x, dummy_ball_y), radius)

    #second paddle
    pygame.draw.rect(wn, RED, pygame.Rect(second_left_paddle_x, second_left_paddle_y, paddle_width, paddle_height) )
    pygame.draw.rect(wn, RED, pygame.Rect(second_right_paddle_x, second_right_paddle_y, paddle_width, paddle_height) )

    if left_gadget == 1:
        pygame.draw.circle(wn, WHITE,(left_paddle_x + 10, left_paddle_y + 10), 4)
    if right_gadget == 1:
        pygame.draw.circle(wn, WHITE,(right_paddle_x + 10, right_paddle_y + 10), 4)

    #endscreen
    winning_font = pygame.font.SysFont('callibri', 100)
    if player_1 >= 3 and not game_over:
        game_over = True
        winner = "Player 1"

    if player_2 >= 3 and not game_over:
        game_over = True
        winner = "Player 2"

    if game_over:
        wn.fill(BLACK)
        endscreen = winning_font.render(f"{winner} Won!!!", True, WHITE)
        wn.blit(endscreen, (200, 250))
        restart_text = font.render("Press R to Restart", True, WHITE)
        wn.blit(restart_text, (350, 320))


    #stopping movement 
    if not game_over:
        ball_x += ball_vel_x
        ball_y += ball_vel_y
        dummy_ball_x += dummy_ball_vel_x
        dummy_ball_y += dummy_ball_vel_y
        right_paddle_y += right_paddle_vel
        left_paddle_y += left_paddle_vel
        second_left_paddle_y += second_left_paddle_vel
        second_right_paddle_y += second_right_paddle_vel


    pygame.display.update() 


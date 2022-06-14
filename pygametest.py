from sre_parse import WHITESPACE
from string import whitespace
import pygame, sys, random

pygame.init()   #required in ALL pygame projects

clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960

scoreA = 0
scoreB = 0

screen = pygame.display.set_mode((screen_width, screen_height))     #returns a display surface object stored in variable called "screen"

pygame.display.set_caption("P-O-N-G!")

#####~~~~~F_U_N_C_T_I_O_N~~~~~#####

def ball_restart ():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1, -1))

def ball_animation ():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top<= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()

    if ball.colliderect(player):
        global scoreA
        scoreA += 1
        ball_speed_x *= -1
    if ball.colliderect(opponent):
        global scoreB
        scoreB += 1
        ball_speed_x *= -1


def player_animation ():
    player.y += player_speed

    if player.top <=0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation ():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

ball = pygame.Rect(
    screen_width/2 - 15, 
    screen_height/2 -15, 30, 30)               # x & y position

player = pygame.Rect(
    screen_width - 20, 
    screen_height/2 - 70, 10, 140)

opponent = pygame.Rect(10,
    screen_height/2 -70, 10, 140
)

bg_color = pygame.Color("grey12")

score_value = 0



light_grey = (200, 200, 200)

#####~~~~~A_N_I_M_A_T_I_O_N~~~~~#####
####
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 8
####
#####~~~~~A_N_I_M_A_T_I_O_N~~~~~#####

scoreA = 0
scoreB = 0

while True:
    for event in pygame.event.get():    #all user input is classified as an event in python
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 8
            if event.key == pygame.K_UP:
                player_speed -= 8

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 8
            if event.key == pygame.K_UP:
                player_speed += 8
    
    ball_animation()
    player_animation()
    opponent_animation ()


    # if opponent.top < ball.y:
    #     opponent.top *= opponent_speed
    # if opponent.bottom > ball.y:
    #     opponent.bottom -= opponent_speed

    # if opponent.top <= 0:
    #     opponent.top = 0
    # if opponent.bottom >= screen_height:
    #     opponent.bottom = screen_height




    # player.y += player_speed

    # if player.top <=0:
    #     player.top = 0
    # if player.bottom >= screen_height:
    #     player.bottom = screen_height





    #####~~~~~A_N_I_M_A_T_I_O_N~~~~~#####
    ####
    # ball.x += ball_speed_x
    # ball.y += ball_speed_y

    # if ball.top<= 0 or ball.bottom >= screen_height:
    #     ball_speed_y *= -1

    # if ball.left <= 0 or ball.right >= screen_width:
    #     ball_speed_x *= -1

    # if ball.colliderect(player) or ball.colliderect(opponent):
    #     ball_speed_x *= -1
    ####
    #####~~~~~A_N_I_M_A_T_I_O_N~~~~~#####

    screen.fill(bg_color)            #drawn first, drawings after this will be placed on top

    pygame.draw.rect(screen,         #display, colour, object
    light_grey, player)

    pygame.draw.rect(screen,
    light_grey, opponent)

    pygame.draw.ellipse(screen,
    light_grey, ball)

    pygame.draw.aaline(screen,
    light_grey,
    (screen_width/2,0),
    (screen_width /2, screen_height))


    font = pygame.font.Font("freesansbold.ttf", 32)
    text = font.render(str(scoreB), 1, (255, 255, 55))
    screen.blit(text, (220,10))
    text = font.render(str(scoreA), 1, (255, 255, 55))
    screen.blit(text, (1020,10))


    pygame.display.flip()
    clock.tick(60)                   #limits speed of game


########E_X_P_E_R_I_M_E_N_T##########

# def show_score(x,y):
#     score = font.render("Score :" + str(score_value), True, (255, 255, 255))
#     screen.blit(score, (x, y))


# textX = 10
# textY = 10

# score_value = 0
# font = pygame.font.Font("freesansbold.ttf", 32)

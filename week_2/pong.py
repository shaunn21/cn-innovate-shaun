
import pygame, sys, random

pygame.init()

clock = pygame.time.Clock()


screen_width = 1280
screen_height = 960

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Free Balling")


def ball_animation():
    global ball_speed_x,ball_speed_y
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def ball_restart():
    global ball_speed_x, ball_speed_y

    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))


def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def score_func():

    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, white)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, white)
    screen.blit(text, (1020,10))

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 -70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)


background = pygame.image.load("week2/day2/pongbg2.jpg").convert()
bg_color = pygame.Color('grey12')
white = (255, 255, 255)
red = (250, 0 , 0)
yellow = (255, 255, 102)
screen.fill(bg_color)

scoreA = 0
scoreB = 0

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_animation()

    screen.blit(background, (0, 0))
    
    pygame.draw.rect(screen, red, player) 
    
    pygame.draw.rect(screen, yellow, opponent)
    
    pygame.draw.ellipse(screen, white,  ball)
    
    pygame.draw.aaline(screen, white, (screen_width/2,0), (screen_width/2, screen_height))
    
    score_func()

    pygame.display.flip()
    clock.tick(60)

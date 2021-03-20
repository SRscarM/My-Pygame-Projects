'''
Author = Sourav
Project for Hindosan times coding olampiad
Date = 28 September 2020

this game took me so many days to make i hope you like it
'''

import pygame,sys,random
from pygame.locals import*
from pygame import mixer

pygame.init()

mixer.music.load('sd.music.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

cell = 20
update_snake = 0
apple = [0, 0]
new_apple = True
new_piece = [0, 0]
game_over = False
clicked = False
score = 0

screen_x = 600
screen_y = 600
screen = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption('Snake Dash')

bg = (255, 255, 255)
body_inner = (0, 0, 0)
body_outer = (255, 0, 0)
food_col = (0,255,0)
blue = (0, 0, 255)
red = (255, 0, 0)

font = pygame.font.SysFont(None,40)

snake = [[int(screen_x / 2), int(screen_y/2)]]
snake.append([300,310])
snake.append([300,320])
snake.append([300,330])
direction = 1

go_sound = mixer.Sound('dead.wav')
apple_sound = mixer.Sound('apple.wav')
click_sound = mixer.Sound('click.wav')

go_sound1 = True
apple1 = True
click1 = True

def draw_screen():
    screen.fill(bg)

def draw_score():
    score_txt = 'SCORE - ' + str(score)
    score_img = font.render(score_txt, True, (0,0,0))
    screen.blit(score_img,(5,5))
    
def check_go(game_over):
    head_count = 0
    for x in snake:
        if snake[0] == x and head_count > 0:
            game_over = True
        head_count += 1
    
    if snake[0][0] < 0 or snake[0][0] > screen_x or snake[0][1] < 0 or snake[0][1] > screen_y:
        game_over = True
    return game_over

def draw_game_over():
    
    over_txt = 'Game Over'
    over_img = font.render(over_txt, True, (0,0,0))
    pygame.draw.rect(screen, bg, (screen_x // 2 - 80, screen_y // 2 - 60, 160, 50))
    screen.blit(over_img, (screen_x// 2 - 80, screen_y // 2 - 50))
    
    again_text = 'Click to Play Again'
    again_img = font.render(again_text, True, (0,0,0))
    screen.blit(again_img, (screen_x// 2 - (80 + 55), screen_y // 2 + 10))
    
run = True
while run:
    draw_screen()
    draw_score()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 3:
                direction = 1
            if event.key == pygame.K_RIGHT and direction != 4:
                direction = 2
            if event.key == pygame.K_DOWN and direction != 1:
                direction = 3
            if event.key == pygame.K_LEFT and direction != 2:
                direction = 4
                
    if new_apple == True:
        new_apple = False
        apple[0] = cell * random.randint(0, (screen_x / cell) - 1)
        apple[1] = cell * random.randint(0, (screen_y / cell) - 1)
                
    pygame.draw.rect(screen, food_col, (apple[0], apple[1], cell, cell))
	
    if snake[0] == apple:
        
        while apple1:
            apple_sound.play()
            apple1 = False
        
        new_apple = True
        new_piece = list(snake[-1])

        if direction == 1:
            new_piece[1] += cell
        if direction == 3:
            new_piece[1] += cell
        if direction == 2:
            new_piece[0] += cell
        if direction == 4:
            new_piece[0] += cell
            
        snake.append(new_piece)
		
        score += 1
        apple1 = True
        
    if game_over == False:
        
        if update_snake >99:
            update_snake = 0
            
            snake = snake[-1:] + snake[:-1]
            
            if direction == 1:
                snake[0][0] = snake[1][0]
                snake[0][1] = snake[1][1] - cell
                
            if direction == 3:
                snake[0][0] = snake[1][0]
                snake[0][1] = snake[1][1] + cell

            if direction == 2:
                snake[0][1] = snake[1][1]
                snake[0][0] = snake[1][0] + cell

            if direction == 4:
                snake[0][1] = snake[1][1]
                snake[0][0] = snake[1][0] - cell
                
            game_over = check_go(game_over)
         
    if game_over == True:
        
        while go_sound1:
            go_sound.play()
            go_sound1 = False
        
        draw_game_over()
        
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            
            while click1:
                click_sound.play()
                click1 = False
            
            go_sound1 = True
            click1 = True
            apple1 = True
            
            clicked = False
            game_over = False
            update_snake = 0
            apple = [0,0]
            new_apple = True
            new_piece = [0,0]
            
            snake = [[int(screen_x / 2), int(screen_y / 2)]]
            snake.append([300,310])
            snake.append([300,320])
            snake.append([300,330])
            
            direction = 1
            score = 0
            
    head = 1
    for x in snake:
            
        if head == 0:
            pygame.draw.rect(screen, body_outer, (x[0], x[1], cell, cell))
            pygame.draw.rect(screen, body_inner, (x[0] + 1, x[1] + 1, cell - 2, cell - 2))
            
        if head == 1:
            pygame.draw.rect(screen, body_outer, (x[0], x[1], cell, cell))
            pygame.draw.rect(screen, (0,0,255), (x[0] + 1, x[1] + 1, cell - 2, cell - 2))
                
            head = 0
            
    pygame.display.update()
        
    update_snake += 1
        
pygame.quit()
            
            



                            
                            






























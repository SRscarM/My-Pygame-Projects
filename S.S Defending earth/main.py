import pygame
import sys
import random
import math
from pygame import mixer

pygame.init()

Sound = True

mixer.music.load('s.s music.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

screen = pygame.display.set_mode((800,600))

background = pygame.image.load('background.png')
gameOver = pygame.image.load('game over.png')

pygame.display.set_caption("Space shooter Defending Earth")

icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)


playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_move = 0

enemyImg = []
enemyX = []
enemyY = []
enemyY_move = []
enemyX_move = []
no_enemy = 5

for i in range(no_enemy):

    enemyImg.append(pygame.image.load('enemy.png'))

    enemyX.append(random.randint(50,750))

    enemyY.append(random.randint(50,150))
    
    enemyX_move.append(2)
    
    enemyY_move.append(100)


bulletImg = pygame.image.load('laser.png')

bulletX = 0
bulletY = 480
bulletX_move = 0
bulletY_move = 7

bulletState = "ready"

score = 0
font = pygame.font.Font('freesansbold.ttf',15)
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf',32)

def player(x,y):
    screen.blit(playerImg, (x,y))
    
def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y))
    
def fire_bullet(x,y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg,(x + 16,y + 10))

def show_score(x,y):
    render_score = font.render("Score - " + str(score),True, (255,255,255))
    screen.blit(render_score, (x,y))
        
def game_over():
    screen.blit(gameOver, (0,0))
    over_text = over_font.render(" Your Score - " + str(score),True, (255,255,255))
    screen.blit(over_text, (250,250))
    
def isCollision(enemyX,enemyY,bulletX,bulletY):
    
    distance = math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance <30:
        return True
    else:
        return False

while True:
    
   screen.blit(background, (0,0))
     
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()

       if event.type == pygame.KEYDOWN:

           if event.key == pygame.K_SPACE:
               
               if bulletState == "ready":
                   bullet_sound = mixer.Sound('bullet.wav')
                   bullet_sound.play()
                   bulletX = playerX
                   fire_bullet(playerX,bulletY)

           
           if event.key == pygame.K_LEFT:
               playerX_move = -4
               
           if event.key == pygame.K_RIGHT:
               playerX_move = 4
        
                        
               
       if event.type == pygame.KEYUP:
           
           if event.key == pygame.K_LEFT:
               playerX_move = -0.01
               
           if event.key == pygame.K_RIGHT:
               playerX_move = 0.01 
   
   player(playerX, playerY)

   show_score(textX,textY)
   
   playerX += playerX_move
   
   if playerX <=0:
       playerX = 755
   elif playerX >=755:
       playerX = 0
       
   
   for i in range(no_enemy):
       
       if enemyY[i]>400:
           
            for j in range(no_enemy):
                enemyY[j]=2000
                playerX = 2000
                
            game_over()

            while Sound:
                gameOver_sound = mixer.Sound('game over.wav')
                gameOver_sound.play()
                Sound = False
            break

       enemy(enemyX[i], enemyY[i],i)
        
       enemyX[i] += enemyX_move[i]
       
       if enemyX[i] <=0:
                    
           enemyX_move[i] = 2
           enemyY[i] += enemyY_move[i]
           
       elif enemyX[i] >=750:
           enemyX_move[i] = -2
           enemyY [i]+= enemyY_move[i]
              
       collision =  isCollision(enemyX[i],enemyY[i],bulletX,bulletY)   
       
       if collision:
           
           enemy_sound = mixer.Sound('enemy.wav')
           enemy_sound.play()
           
           bulletY = 480
           bulletState = "ready"
           score +=1

           enemyX[i] = random.randint(50,750)

           enemyY[i] = random.randint(50,150)
           
   if bulletY <= 0:
       bulletY = 480
       bulletState = "ready"
       
   if bulletState == "fire":
       fire_bullet(bulletX,bulletY)
       bulletY -= bulletY_move
       
       

   pygame.display.update()
   
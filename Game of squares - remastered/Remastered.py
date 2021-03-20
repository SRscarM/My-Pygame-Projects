import pygame
import sys
from pygame import mixer

pygame.init()

mixer.music.load('theme.mpeg')
mixer.music.set_volume(0.2)
mixer.music.play(-1)

screenX = 800
screenY = 600
display = pygame.display.set_mode((screenX,screenY))
icon = pygame.image.load('A BOT.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('GoS -Remastered')

enemyX = 100
enemyY = 100

playerX = 300
playerY = 300

playerVel = 3
enemyVel = 2

run = True
gameDisplay = True

clock = pygame.time.Clock()
font = pygame.font.Font(None, 25)

frame_count = 0
frame_rate = 60
start_time = 90

def player(x,y):
    playerImg = pygame.image.load('player.png')
    display.blit(playerImg, (x,y))
    
def enemy(x,y):
    enemyImg = pygame.image.load('enemy.png')
    display.blit(enemyImg, (x,y))
    
def game():
    display.fill((190,190,190))
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
    
def exitGame():
    pygame.quit()
    sys.exit()
    

while run:
    
    pygame.time.delay(25) 
    
    if playerX <= 0:
        playerX = 0 
        
    if playerX >= 764:
        playerX = 764
        
    if playerY <= 0:
        playerY = 0
        
    if playerY >= 564:
        playerY = 564
    
    if enemyX < playerX - 20:
        enemyX = enemyX + enemyVel
        game()
        
    elif enemyX > playerX + 20: 
        game()
        enemyX = enemyX - enemyVel
  
    elif enemyY < playerY - 20: 
        enemyY = enemyY + enemyVel
          
    elif enemyY > playerY + 20:
        enemyY = enemyY - enemyVel
        
    else:
        mixer.music.load('hit.wav')
        mixer.music.play(1)
        text = font.render(output_string, False, (0,0,0))
        run = False
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerX -= playerVel
        
    if keys[pygame.K_RIGHT]:
        playerX += playerVel
        
    if keys[pygame.K_UP]:
        playerY -= playerVel
        
    if keys[pygame.K_DOWN]:
        playerY += playerVel
        
    while gameDisplay:
        game()
        gameDisplay = False
        
        
    total_seconds = frame_count // frame_rate
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    
    output_string = "Time Survived: {0:02}:{1:02}".format(minutes, seconds)
    
    text = font.render(output_string, True, (0,0,0))
    
    display.blit(text, [5, 5])
    
    total_seconds = start_time - (frame_count // frame_rate)
    
    if total_seconds < 0:
        total_seconds = 0
        
    frame_count += 1
    
    clock.tick(frame_rate)
    
    pygame.display.flip()
         
            
    pygame.display.update()
    
    
exitGame()

            
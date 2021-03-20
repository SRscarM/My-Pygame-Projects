'''
Author : Sourav
For    : Hindostan times coding olampiad
date   : 3/0/2020
'''
#importing modules
import pygame, sys, random, math
from pygame import mixer

#defining global variables
sx = 800
sy = 600
tx = 10
ty = 10
screen = pygame.display.set_mode((sx,sy))
icon = pygame.image.load('A BOT.png')
bg = pygame.image.load('background.png')
gameImg = {}
gameSounds = {}
fps = 150
fps_clock = pygame.time.Clock()
score = 0
once = True

#define game variables
game_over = False
run = False
Exit = True

#player variables
pX = (sx / 2) - 32
pY = (sy - 62) - 10
x_vel = 0
y_vel = 0

#enemy variables
enemyImg = []
enemyX = []
enemyY = []
enemyY_move = []
enemyX_move = []
no_enemy = 10

#the code i took from my other game
for i in range(no_enemy):
    
    enemyImg.append(pygame.image.load('Z BOT.png').convert_alpha())
    enemyX.append(random.randint(5,(sx - 68)))
    enemyY.append(random.randint(5,150))
    enemyX_move.append(1)
    enemyY_move.append(1)

#player functon
def player(x,y):
    screen.blit(gameImg['player'],(x,y))

#enemy functon
def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y))

#exit functon
def Exit():
    pygame.quit()
    sys.exit()
   
def show_score(x,y):
    font = pygame.font.Font('freesansbold.ttf',25)
    render_score = font.render("SCORE - " + str(score),True, (255,0,0))
    screen.blit(render_score, (x,y))
  
#collision detection (this would be a lot easier in unity , C#) functon
#i took help of google to write this as it was very complex in other way
def collisionDetection(enemyX,enemyY,pX,pY):
    
    distance = math.sqrt((math.pow(enemyX-pX,2))+(math.pow(enemyY-pY,2)))
    
    if distance < 50:
        return True
    else:
        return False


#a new code i learned from pygames documentation
if __name__ == "__main__":
    
    #inetialising pygame
    pygame.init()
    
    #icon and the caption of the game
    pygame.display.set_icon(icon)
    pygame.display.set_caption('A.BOT')
    
    #starting music for the game
    mixer.music.load('start screen music.mp3')
    mixer.music.set_volume(0.5)
    mixer.music.play(-1)
    
    #adding the game sounds
    gameSounds['click'] = mixer.Sound('click.wav')
    gameSounds['bump'] = mixer.Sound('bump.wav')
    
    #adding images and coverting them
    gameImg['player'] = pygame.image.load('A BOT.png').convert_alpha()
    gameImg['background'] = pygame.image.load('background.png').convert_alpha()
    gameImg['main screen'] = pygame.image.load('main.png').convert_alpha()   

    #bliting the main screen
    screen.blit(gameImg['main screen'], (0,0))
    
    #ok so this is going to be the loop which will run the main screen and check for events 
    while Exit:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                Exit()
                Exit = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    
                    #starting the game music
                    mixer.music.load('game music.mp3')
                    mixer.music.set_volume(0.3)
                    mixer.music.play(-1)
                    
                    #playing the click sound
                    gameSounds['click'].play()
                    
                    Exit = False
                    run = True
                    
            #Setting the fps of the game
            fps_clock.tick(fps)
            
            pygame.display.update()

    #starting the infinate game looooooooooooooooooop
    while run:
    
        for event in pygame.event.get():

            #exiting the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #movement of the player throught key strocks
            if event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_LEFT:
                    x_vel -= 2
                if event.key == pygame.K_RIGHT:
                    x_vel += 2
                if event.key == pygame.K_UP:
                    y_vel -= 2
                if event.key == pygame.K_DOWN:
                    y_vel += 2
                
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT:
                    x_vel = 0
                if event.key == pygame.K_RIGHT:
                    x_vel = 0
                if event.key == pygame.K_UP:
                    y_vel = 0
                if event.key == pygame.K_DOWN:
                    y_vel = 0
    
        #bliting the game background
        screen.blit(gameImg['background'], (0,0))
        show_score(tx,ty)
        player(pX,pY)
        pX += x_vel
        pY += y_vel

        for i in range(no_enemy):
 
            enemy(enemyX[i], enemyY[i],i)
       
            enemyY[i] += enemyY_move[i]
                
            if enemyY[i] >= (sy - 62):
                gameSounds['bump'].play()
                score += 1
                enemyX[i] = random.randint(5,(sx - 68))
                enemyY_move[i] = -1
                enemyY[i] += enemyY_move[i]
           
            if enemyY[i] <= (0 + 5):
                gameSounds['bump'].play()
                enemyX[i] = random.randint(5,(sx - 68))
                enemyY_move[i] = 1
                enemyY[i] += enemyY_move[i]
                
            collision =  collisionDetection(enemyX[i],enemyY[i],pX,pY)   
       
            if collision:
                pygame.quit()
                sys.exit()
        
        if pX <= 5:
            pX = 5
        
        if pX >= (sx - 68):
            pX = (sx - 68)
        
        if pY <= 5:
            pY = 5
        
        if pY >= (sy - 62):
            pY = (sy - 62)
            
        #Setting the fps of the game
        fps_clock.tick(fps)

        pygame.display.update()
           
        
    




























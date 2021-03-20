'''
Author : Sourav
For    : Hindostan times coding olampiad
date   : 10/10/2020
'''

# importing thinks
import pygame, sys, math, random
from pygame import mixer

#screen x ,y 
sx = 1000
sy = 800
screen = pygame.display.set_mode((sx, sy))

# all the game images and sounds in this dictionary
gameSprites = {}
gameSounds = {}

#random boolin
mainScreenBool = True
mainGameBool = False
once =  True

#fps of the game
fps = 100
fps_clock = pygame.time.Clock()

#colors
lred = (255,0,0)
dred = (164,0,0)
lg = (0,255,0)
dg = (0,164,0)

#rect x and y
rectx = (sx/2) - (250/2)
recty = (sy/2) - 100

#player class
class Player:
    
    def __init__(self):
        
        self.px = 32
        self.py = sy - 150
    
    def showPlayer(self):
        screen.blit(gameSprites['play'],(self.px,self.py))
    
#enemy class
class Enemy:
    
    def __init__(self):
        
        #enemy variables
        self.enemyImg = []
        self.ex = []
        self.ey = []
        self.ex_move = []
        self.ey_move = []
        self.no_enemy = 5 
        
        for i in range(self.no_enemy):
    
            self.enemyImg.append(pygame.image.load('enemy.png').convert_alpha())
            self.ex.append(random.randint((sx/2),sx + 50))
            self.ey.append(sy - 150)
            self.ex_move.append(1)
            self.ey_move.append(0)
    
    def showEnemy(self,i):
        screen.blit(self.enemyImg[i],(self.ex[i],self.ey[i]))
        
bulletX = 0
bulletY = sy - 110
bulletX_move = 7
bulletState = "ready"
    
tx = 10
ty = 10
score = 0
    
gox = (sx / 2) - 350
goy = (sy / (2) - 200)
go = "YOUR DIDN'T SURVIVE"

def fire_bullet(x,y):
    global bulletState
    bulletState = "fire"
    screen.blit(gameSprites['boom'],(x + 80,y))

def showScore(x,y):
    tfont = pygame.font.Font('freesansbold.ttf',32)
    render = tfont.render("ZOMBIE KILLED - " + str(score),True, (100,0,0))
    screen.blit(render, (x,y))

def  GAME_OVER(x,y):
    screen.blit(gameSprites['bg'],(0,0))
    gofont = pygame.font.Font('freesansbold.ttf',64)
    gotext = gofont.render(go,True, (50,0,0))
    screen.blit(gotext, (x,y))

def butten(x,y):
    
    #font
    rectfont = pygame.font.Font('freesansbold.ttf',35)
    
    #variables
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    state = None
    
    #changing the color of the butten when the curser is over the butten
    
    #rect 1
    if x + 250 > mouse[0] > x and y + 50 > mouse[1] > y:
        
        #play rect (with dark colour)
        pygame.draw.rect(screen, dg, (x,y,250,50))
        recttext = rectfont.render('PLAY',True, (0,0,0))
        screen.blit(recttext, ((x + 80),(y + 10)))
        state = 'playing'
        
        if click[0] == 1 and state != None:
            gameSounds['click'].play()
            return True
        
    else:
        
        #play rect (with light colour)
        pygame.draw.rect(screen, lg, (x,y,250,50))
        recttext = rectfont.render('PLAY',True, (0,0,0))
        screen.blit(recttext, ((x + 80),(y + 10)))
        state = None

    #rect 2
    if x + 250 > mouse[0] > x and (y + 100)+ 50 > mouse[1] > (y + 100):
        
        #quit rect (with dark colour)
        pygame.draw.rect(screen, dred, (x,(y + 100),250,50))
        recttexttwo = rectfont.render('QUIT',True, (0,0,0))
        screen.blit(recttexttwo, ((x + 80),(y + 110)))
        state = 'give up'
        
        if click[0] == 1 and state != None:
            gameSounds['click'].play()
            pygame.quit()
            sys.exit()
        
    else:
        
        #quit rect (with light colour)
        pygame.draw.rect(screen, lred, (x,(y + 100),250,50))
        recttexttwo = rectfont.render('QUIT',True, (0,0,0))
        screen.blit(recttexttwo, ((x + 80),(y + 110)))
        state = None

def ifCollision(ex,ey,bx,by):
    
    dis = math.sqrt((math.pow(ex-bx,2))+(math.pow(ey-by,2)))
    
    if dis < 50:
        return True
    else:
        return False
    

#you know what this is
if __name__ == "__main__":
    
    #init pygame
    pygame.init()
    
    #creating a objectes
    player = Player()
    enemy = Enemy()
    
    #assigning images to the distionary
    gameSprites['main screen'] = pygame.image.load('main screen.png').convert_alpha()
    gameSprites['icon'] = pygame.image.load('icon.png').convert_alpha()
    gameSprites['bg'] = pygame.image.load('background.png').convert_alpha()
    gameSprites['play'] = pygame.image.load('player.png').convert_alpha()
    gameSprites['boom'] = pygame.image.load('bullet.png').convert_alpha()
    
    #denineing the game sounds in the distionay
    gameSounds['click'] = mixer.Sound('click.wav')
    gameSounds['hit'] = mixer.Sound('hit.wav')
    gameSounds['bullet'] = mixer.Sound('bullet.wav')
    gameSounds['game over'] = mixer.Sound('dead.wav')
    gameSounds['next level'] = mixer.Sound('power up (not for the player).wav')
    
    #defining icon and title
    pygame.display.set_caption('RIP AND TEAR')
    pygame.display.set_icon(gameSprites['icon'])
    
    #first game loop
    while mainScreenBool:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        #bliting the screen
        screen.blit(gameSprites['main screen'],(0,0))
        
        #this is the butten function
        butten(rectx,recty)
        
        b = butten(rectx,recty)
        if b:
            
            mixer.music.load('music.mp3')
            mixer.music.play(-1)
            
            mainScreenBool = False
            mainGameBool = True
        
        #updateing screen after the bliting of the images
        pygame.display.update()
        
    #second game loop
    while mainGameBool:
        
        screen.blit(gameSprites['bg'],(0,0))
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
               
                    if bulletState == "ready":
                        
                        gameSounds['bullet'].play()
                        bulletX = player.px
                        fire_bullet(player.px,bulletY)
                        
        showScore(tx,ty)
        player.showPlayer()
        
        #Enemy for loop
        for i in range(enemy.no_enemy):

            enemy.showEnemy(i)
       
            enemy.ex[i] -= enemy.ex_move[i]
            
            
            collision =  ifCollision(enemy.ex[i],enemy.ey[i],bulletX,bulletY)   
            
            if collision:
                
                enemy.ex[i] = random.randint((800),sx + 50)
                gameSounds['hit'].play()
                score +=1
                bulletX = player.px + 125
                bulletState = "ready"
                
            if enemy.ex[i] <= player.px + 250:

                for j in range(enemy.no_enemy): 
                    
                    enemy.ex[j] = 2000
                    player.px = 20000
                    enemy.ex_move[j] = 0
                
                while once:
                    gameSounds['game over'].play()
                    once = False
                    
                GAME_OVER(gox,goy)
                
            if score == 20 or score == 40 or score == 60 or score == 80 or score == 100:
                
                gameSounds['next level'].play()
                score += 1
                
                for j in range(enemy.no_enemy): 
                    
                    enemy.ex_move[j] += 0.3

        
        if bulletX >= sx:
            bulletX = player.px + 120
            bulletState = "ready"
       
        if bulletState == "fire":
            fire_bullet(bulletX,bulletY)
            bulletX += bulletX_move
            
            
        #Setting the fps of the game
        fps_clock.tick(fps)
       
        
        pygame.display.update()
    
    
    

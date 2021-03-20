'''
Author: Sourav
Date created: 3/11/2020
'''

#importing the modules
import pygame
import sys
import random

#pygame init
pygame.init()

#font init
pygame.font.init()

#all screen variables
sx = 900
sy = 900
screen = pygame.display.set_mode((sx,sy))

#defining the colour variables
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
grey = (100,100,100)

#defining the caption
pygame.display.set_caption('Click it!')

#defining the variable
FPS = 25
clock = pygame.time.Clock()
clock.tick(FPS)

score = 0

#bool variables
start = True
main = False

#defining the variable for circle
px = int(random.randint(10,sx - 25))
py = int(random.randint(10,sy - 25))

#circle class
class Square():
    
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        self.colour = black

    def drawCircle(self):# ;)
        pygame.draw.rect(screen, self.colour, pygame.Rect(self.x, self.y, 25, 25)) 
        
square = Square(px, py)

#start screen function
def startWindow():
    screen.fill(white)
    
    font = pygame.font.SysFont("comicsans", 50)
    text = font.render('Press mouse to start!', 1, black)
    
    textHeight = text.get_height()
    textWidth = text.get_width()
    
    textx = (sx/2) - (textWidth/2)
    texty = (sy/2) - (textHeight/2)
    
    screen.blit(text, (textx,texty))
    
    pygame.display.update()
 
def gameWindow():
    screen.fill(white)  
    square.drawCircle() 
    Score()
    
def Click(x, y):
    
    #variables
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    state = None

    if x + 25 > mouse[0] > x and y + 25 > mouse[1] > y:
        square.colour = grey
        state = 'clicked'
        
        if click[0] == 1 and state != None:
            return True
    else:
        square.colour = black
        state = None

def Score():
    
    font = pygame.font.SysFont("comicsans", 50)
    text = font.render(f'SCORE - {score}', 1, black)
    
    textx = 25
    texty = 25
    
    screen.blit(text, (textx,texty))

#start screen game loop
while start:
    
    startWindow()
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            run = True
            start = False
    
#main game loop
while run:
    
    square = Square(px, py)
    Click(px, py)
    gameWindow()
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    c = Click(px, py)
    if c:
        px = int(random.randint(10,sx - 25))
        py = int(random.randint(10,sy - 25))
        score += 1
    
    pygame.display.update()
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
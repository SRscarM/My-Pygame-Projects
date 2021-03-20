'''
Code written by Sourav
Music and sound effects are also made by Sourav

well i want to say that this is not my first game as i have made a 3d game using unity game engnie and the C# or C sharp coding language
i also know how to make 3d modal in blender. the game name is A BOT but it is not on play store. lol . Enjoy my game. bye
'''

# Importing libaries which i will be needing for the game
import pygame
import sys
import random
from pygame import mixer

# Init the pygame library
pygame.init()

# Color of the screen, logo, background, caption.
display = pygame.display.set_mode((800,600))
logo = pygame.image.load('A BOT.png')
background = pygame.image.load('background.png')
pygame.display.set_caption('Guess it')
pygame.display.set_icon(logo)

# X,Y position of the text.
textX = 280
textY = 380
font = pygame.font.Font('freesansbold.ttf',25)
right_font = pygame.font.Font('freesansbold.ttf',60)

# loop inside a loop. paradox?
run = True

# These are functions i guess
def mainGame():
    display.fill((210,210,210))
    display.blit(background, (0,20))
    mixer.music.load('music.mpeg')
    mixer.music.set_volume(0.3)
    mixer.music.play(-1)
    # binod
    
# RaNdOm NuMbEr 0_0
def RandomNumber():
    global i
    i = random.randint(0,9)
    
# HaHa u WIN
def Right():
    '''| tHIS code took me 1 ay to figure out
      \/
    '''
    display.fill((210,210,210))
    display.blit(background, (0,20))
    
    right = right_font.render("Right!", True, (0,255,0))
    display.blit(right, (textX  , textY + 50))
    # Sound if you are right
    right_sound = mixer.Sound('right.wav')
    right_sound.play()
    
# HaHa u LOSE
def Wrong():
    display.fill((210,210,210))
    display.blit(background, (0,20))
    
    wrong = right_font.render("Wrong!", True, (255,0,0))
    display.blit(wrong, (textX  , textY + 50))
    # Sound if you are wrong
    wrong_sound = mixer.Sound('wrong.wav')
    wrong_sound.play()

    
# This is the game loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooop. ;)
while True:
    
    RandomNumber()

    while run:
        mainGame()
        pygame.time
        run = False
        
        
    # Key strorek and events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                if i == 0:
                    Right()
                    number = font.render("0", True, (0,0,0))
                    your_number = font.render("Your Number:", True, (0,0,0))
                    display.blit(number, (textX + 200, textY))
                    display.blit(your_number, (textX,textY))
                    
                elif i != 0: 
                    Wrong()
                    number = font.render("0", True, (0,0,0))
                    your_number = font.render("Your Number:", True, (0,0,0))
                    display.blit(number, (textX + 200, textY))
                    display.blit(your_number, (textX,textY))
                    
            if event.key == pygame.K_1:
                if i == 1:
                    Right()
                    number = font.render("1", True, (0,0,0))
                    your_number = font.render("Your Number:", True, (0,0,0))
                    display.blit(number, (textX + 200, textY))
                    display.blit(your_number, (textX,textY))
                    
                elif i != 1:
                    Wrong()
                    number = font.render("1", True, (0,0,0))
                    your_number = font.render("Your Number:", True, (0,0,0))
                    display.blit(number, (textX + 200, textY))
                    display.blit(your_number, (textX,textY))
                    
            if event.key == pygame.K_2:
                if i == 2:
                    Right()
                    number = font.render("2", True, (0,0,0))
                    your_number = font.render("Your Number:", True, (0,0,0))
                    display.blit(number, (textX + 200, textY))
                    display.blit(your_number, (textX,textY))
                    
                elif i != 2:
                    Wrong()
                    number = font.render("2", True, (0,0,0))
                    your_number = font.render("Your Number:", True, (0,0,0))
                    display.blit(number, (textX + 200, textY))
                    display.blit(your_number, (textX,textY))
                    
            if event.key == pygame.K_3:
                if i == 3:
                    Right()
                    number = font.render("3", True, (0,0,0))
                    your_number = font.render("Your Number:", True, (0,0,0))
                    display.blit(number, (textX + 200, textY))
                    display.blit(your_number, (textX,textY))
                    
                elif i != 3:
                    Wrong()
                    number = font.render("3", True, (0,0,0))
                    your_number = font.render("Your Number:", True, (0,0,0))
                    display.blit(number, (textX + 200, textY))
                    display.blit(your_number, (textX,textY))
                    
            if event.key == pygame.K_4:
                if i == 4:
                    Right()
                    number = font.render("4", True, (0,0,0))
                    your_number = font.render("Your Number:", True, (0,0,0))
                    display.blit(number, (textX + 200, textY))
                    display.blit(your_number, (textX,textY))
                    
                elif i != 4:
                    Wrong()
                    number = font.render("4", True, (0,0,0))
                    your_number = font.render("Your Number:", True, (0,0,0))
                    display.blit(number, (textX + 200, textY))
                    display.blit(your_number, (textX,textY))
                    
            if event.key == pygame.K_5:
                if i == 5:
                    Right()
                    number = font.render("5", True, (0,0,0))
                    your_number = font.render("Your Number:", True, (0,0,0))
                    display.blit(number, (textX + 200, textY))
                    display.blit(your_number, (textX,textY))
                    
                elif i != 5:
                    Wrong()
                    number = font.render("5", True, (0,0,0))
                    your_number = font.render("Your Number:", True, (0,0,0))
                    display.blit(number, (textX + 200, textY))
                    display.blit(your_number, (textX,textY))
                    
            if event.key == pygame.K_6:
                if i == 6:
                    Right()
                    number = font.render("6", True, (0,0,0))
                    your_number = font.render("Your Number:", True, (0,0,0))
                    display.blit(number, (textX + 200, textY))
                    display.blit(your_number, (textX,textY))
                    
                elif i != 6:
                    Wrong()
                    number = font.render("6", True, (0,0,0))
                    your_number = font.render("Your Number:", True, (0,0,0))
                    display.blit(number, (textX + 200, textY))
                    display.blit(your_number, (textX,textY))
                    
            if event.key == pygame.K_7:
                if i == 7:
                    Right()
                    number = font.render("7", True, (0,0,0))
                    your_number = font.render("Your Number:", True, (0,0,0))
                    display.blit(number, (textX + 200, textY))
                    display.blit(your_number, (textX,textY))
                    
                elif i != 7:
                    Wrong()
                    number = font.render("7", True, (0,0,0))
                    your_number = font.render("Your Number:", True, (0,0,0))
                    display.blit(number, (textX + 200, textY))
                    display.blit(your_number, (textX,textY))
                    
            if event.key == pygame.K_8:
                if i == 8:
                    Right()
                    number = font.render("8", True, (0,0,0))
                    your_number = font.render("Your Number:", True, (0,0,0))
                    display.blit(number, (textX + 200, textY))
                    display.blit(your_number, (textX,textY))
                    
                elif i != 8:
                    Wrong()
                    number = font.render("8", True, (0,0,0))
                    your_number = font.render("Your Number:", True, (0,0,0))
                    display.blit(number, (textX + 200, textY))
                    display.blit(your_number, (textX,textY))
                    
            if event.key == pygame.K_9:
                if i == 9:
                    Right()
                    number = font.render("9", True, (0,0,0))
                    your_number = font.render("Your Number:", True, (0,0,0))
                    display.blit(number, (textX + 200, textY))
                    display.blit(your_number, (textX,textY))
                    
                elif i != 9:
                    Wrong()
                    number = font.render("9", True, (0,0,0))
                    your_number = font.render("Your Number:", True, (0,0,0))
                    display.blit(number, (textX + 200, textY))
                    display.blit(your_number, (textX,textY))
                    
                
    # This code is the most improtant if you didn't write it you do not know how to code lol
    pygame.display.update()
        




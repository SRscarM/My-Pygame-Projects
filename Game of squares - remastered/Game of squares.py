import pygame
import sys

pygame.init()

display = pygame.display.set_mode((800, 600))
pygame.display.set_caption("GoS -Remastered")

bluex = 100
bluey = 100

redX = 300
redY = 300

bluevel = 6
redVel = 4

def drawGame():
     win.fill((0, 0, 0)) #color of screen= black
     pygame.draw.rect(win, (0, 0, 255), (bluex, bluey, 20, 20)) #players position is > enmys
     pygame.draw.rect(win, (255, 0, 0), (redX, redY, 40, 40))
     pygame.display.update() # updating the game

while True:
    
      pygame.time.delay(100) #time delay

      if redX < bluex - 10: 
          redX = redX + redVel 
          drawGame() 
          
      elif redX > bluex + 10:
          drawGame()
          redX = redX - redVel
          
      elif redY < bluey - 10: 
          redY = redY + redVel 
          
      elif redY > bluey + 10:
          redY = redY - redVel
          
      else:
          run = False
      
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  run = False

      keys = pygame.key.get_pressed()

      if keys[pygame.K_LEFT]:
            bluex -= bluevel

      if keys[pygame.K_RIGHT]:
            bluex += bluevel
      
      if keys[pygame.K_UP]:
            bluey -= bluevel
      
      if keys[pygame.K_DOWN]:
            bluey += bluevel
      
      drawGame()
          
pygame.quit()  

    
    
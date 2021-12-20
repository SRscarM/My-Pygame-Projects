'''
Author: Sourav
Date of Creation: 19/12/21
Class: 9th
Section: A
'''
#OXYGEN

#importing modules
import pygame
import math
import sys, os

pygame.init()

#screen variables
screenX = 1000
screenY = 800
screen = pygame.display.set_mode((screenX, screenY))

#variables
mainGame = True
fps =  30
clock = pygame.time.Clock()
images = {}

#game images
images['icon'] = pygame.image.load(os.path.join("data", "Images", "icon.png")).convert_alpha()

images['Obg'] = pygame.image.load(os.path.join("data", "Images", "oxygen", "OxygenBg.png")).convert_alpha()
images['OElc1'] = pygame.image.load(os.path.join("data", "Images", "oxygen", "HeliumElectrons.png")).convert_alpha()
images['OElc2'] = pygame.image.load(os.path.join("data", "Images", "oxygen", "OxygenElectron2.png")).convert_alpha()



#HYDROGEN object
class OxygenOne:

  def __init__(self):
    self.angle = 0
    self.image = images['OElc1']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotateOxygenOne(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitOxygenOne(self):
    self.angle +=   4
    oxygenRotated, oxygenRotatedRect = self.rotateOxygenOne(self.image, self.angle)
    screen.blit(oxygenRotated, oxygenRotatedRect)

class OxygenTwo:

  def __init__(self):
    self.angle = 0
    self.image = images['OElc2']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotateOxygenTwo(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitOxygenTwo(self):
    self.angle +=   2
    oxygenRotated, oxygenRotatedRect = self.rotateOxygenTwo(self.image, self.angle)
    screen.blit(oxygenRotated,oxygenRotatedRect)


#objects
oxygen = OxygenOne()
oxygenTwo = OxygenTwo()

oxygenRectImage = images['OElc1'].get_rect(center = (oxygen.positionX,oxygen.positionY))
oxygenTwoRectImage = images['OElc2'].get_rect(center = (oxygenTwo.positionX,oxygenTwo.positionY))

#defining icon and title
pygame.display.set_caption('Oxygen')
pygame.display.set_icon(images['icon'])

#game loop
while mainGame:
  screen.blit(images['Obg'],(0,0))
  
  oxygen.blitOxygenOne()
  oxygenTwo.blitOxygenTwo()

  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  clock.tick(fps)
  pygame.display.update()





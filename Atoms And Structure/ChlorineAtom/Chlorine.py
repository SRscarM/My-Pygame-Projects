'''
Author: Sourav
Date of Creation: 19/12/21
Class: 9th
Section: A
'''
#CHLORINE

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

images['Clbg'] = pygame.image.load(os.path.join("data", "Images", "chlorine", "ChlorineBg.png")).convert_alpha()
images['ClElc1'] = pygame.image.load(os.path.join("data", "Images", "chlorine", "HeliumElectrons.png")).convert_alpha()
images['ClElc2'] = pygame.image.load(os.path.join("data", "Images", "chlorine", "ChlorineElectron2.png")).convert_alpha()
images['ClElc3'] = pygame.image.load(os.path.join("data", "Images", "chlorine", "ChlorineElectron3.png")).convert_alpha()

#HYDROGEN object
class chlorineOne:

  def __init__(self):
    self.angle = 0
    self.image = images['ClElc1']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotatechlorineOne(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitchlorineOne(self):
    self.angle +=   4
    chlorineRotated, chlorineRotatedRect = self.rotatechlorineOne(self.image, self.angle)
    screen.blit(chlorineRotated, chlorineRotatedRect)

class chlorineTwo:

  def __init__(self):
    self.angle = 0
    self.image = images['ClElc2']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotatechlorineTwo(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitchlorineTwo(self):
    self.angle +=   3
    chlorineRotated, chlorineRotatedRect = self.rotatechlorineTwo(self.image, self.angle)
    screen.blit(chlorineRotated,chlorineRotatedRect)

class chlorineThree:

  def __init__(self):
    self.angle = 0
    self.image = images['ClElc3']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotatechlorineThree(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitchlorineThree(self):
    self.angle +=   2
    chlorineRotated, chlorineRotatedRect = self.rotatechlorineThree(self.image, self.angle)
    screen.blit(chlorineRotated,chlorineRotatedRect)


#objects
chlorine = chlorineOne()
chlorineTwo = chlorineTwo()
chlorineThree = chlorineThree()

chlorineRectImage = images['ClElc1'].get_rect(center = (chlorine.positionX,chlorine.positionY))
chlorineTwoRectImage = images['ClElc2'].get_rect(center = (chlorineTwo.positionX,chlorineTwo.positionY))
chlorineThreeRectImage = images['ClElc3'].get_rect(center = (chlorineThree.positionX,chlorineThree.positionY))

#defining icon and title
pygame.display.set_caption('Chlorine')
pygame.display.set_icon(images['icon'])

#game loop
while mainGame:
  screen.blit(images['Clbg'],(0,0))
  
  chlorine.blitchlorineOne()
  chlorineTwo.blitchlorineTwo()
  chlorineThree.blitchlorineThree()

  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  clock.tick(fps)
  pygame.display.update()





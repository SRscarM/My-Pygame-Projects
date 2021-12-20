'''
Author: Sourav
Date of Creation: 19/12/21
Class: 9th
Section: A
'''
#POTASSIUM

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

images['Kbg'] = pygame.image.load(os.path.join("data", "Images", "potassium", "Potassium.png")).convert_alpha()
images['KElc1'] = pygame.image.load(os.path.join("data", "Images", "potassium", "HeliumElectrons.png")).convert_alpha()
images['KElc2'] = pygame.image.load(os.path.join("data", "Images", "potassium", "ChlorineElectron2.png")).convert_alpha()
images['KElc3'] = pygame.image.load(os.path.join("data", "Images", "potassium", "NitrogenElectron.png")).convert_alpha()
images['KElc4'] = pygame.image.load(os.path.join("data", "Images", "potassium", "Potassiumeletron.png")).convert_alpha()

#HYDROGEN object
class potassiumOne:

  def __init__(self):
    self.angle = 0
    self.image = images['KElc1']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotatepotassiumOne(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitpotassiumOne(self):
    self.angle +=   4
    potassiumRotated, potassiumRotatedRect = self.rotatepotassiumOne(self.image, self.angle)
    screen.blit(potassiumRotated, potassiumRotatedRect)

class potassiumTwo:

  def __init__(self):
    self.angle = 0
    self.image = images['KElc2']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotatepotassiumTwo(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitpotassiumTwo(self):
    self.angle +=   3
    potassiumRotated, potassiumRotatedRect = self.rotatepotassiumTwo(self.image, self.angle)
    screen.blit(potassiumRotated,potassiumRotatedRect)

class potassiumThree:

  def __init__(self):
    self.angle = 0
    self.image = images['KElc3']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotatepotassiumThree(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitpotassiumThree(self):
    self.angle +=   2
    potassiumRotated, potassiumRotatedRect = self.rotatepotassiumThree(self.image, self.angle)
    screen.blit(potassiumRotated,potassiumRotatedRect)

class potassiumFour:

  def __init__(self):
    self.angle = 0
    self.image = images['KElc4']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotatepotassiumFour(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitpotassiumFour(self):
    self.angle +=   1
    potassiumRotated, potassiumRotatedRect = self.rotatepotassiumFour(self.image, self.angle)
    screen.blit(potassiumRotated,potassiumRotatedRect)


#objects
potassium= potassiumOne()
potassiumTwo = potassiumTwo()
potassiumThree = potassiumThree()
potassiumFour = potassiumFour()

potassiumRectImage = images['KElc1'].get_rect(center = (potassium.positionX,potassium.positionY))
potassiumTwoRectImage = images['KElc2'].get_rect(center = (potassiumTwo.positionX,potassiumTwo.positionY))
potassiumThreeRectImage = images['KElc3'].get_rect(center = (potassiumThree.positionX,potassiumThree.positionY))
potassiumFourRectImage = images['KElc4'].get_rect(center = (potassiumFour.positionX,potassiumFour.positionY))

#defining icon and title
pygame.display.set_caption('Potassium')
pygame.display.set_icon(images['icon'])

#game loop
while mainGame:
  screen.blit(images['Kbg'],(0,0))
  
  potassium.blitpotassiumOne()
  potassiumTwo.blitpotassiumTwo()
  potassiumThree.blitpotassiumThree()
  potassiumFour.blitpotassiumFour()

  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  clock.tick(fps)
  pygame.display.update()





'''
Author: Sourav
Date of Creation: 19/12/21
Class: 9th
Section: A
'''
#ARGON

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

images['Abg'] = pygame.image.load(os.path.join("data", "Images", "argon", "argonbg.png")).convert_alpha()
images['AElc1'] = pygame.image.load(os.path.join("data", "Images", "argon", "HeliumElectrons.png")).convert_alpha()
images['AElc2'] = pygame.image.load(os.path.join("data", "Images", "argon", "ChlorineElectron2.png")).convert_alpha()
images['AElc3'] = pygame.image.load(os.path.join("data", "Images", "argon", "NitrogenElectron.png")).convert_alpha()

#HYDROGEN object
class argonOne:

  def __init__(self):
    self.angle = 0
    self.image = images['AElc1']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotateargonOne(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitargonOne(self):
    self.angle +=   4
    argonRotated, argonRotatedRect = self.rotateargonOne(self.image, self.angle)
    screen.blit(argonRotated, argonRotatedRect)

class argonTwo:

  def __init__(self):
    self.angle = 0
    self.image = images['AElc2']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotateargonTwo(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitargonTwo(self):
    self.angle +=   3
    argonRotated, argonRotatedRect = self.rotateargonTwo(self.image, self.angle)
    screen.blit(argonRotated,argonRotatedRect)

class argonThree:

  def __init__(self):
    self.angle = 0
    self.image = images['AElc3']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotateargonThree(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitargonThree(self):
    self.angle +=   2
    argonRotated, argonRotatedRect = self.rotateargonThree(self.image, self.angle)
    screen.blit(argonRotated,argonRotatedRect)


#objects
argon = argonOne()
argonTwo = argonTwo()
argonThree = argonThree()

argonRectImage = images['AElc1'].get_rect(center = (argon.positionX,argon.positionY))
argonTwoRectImage = images['AElc2'].get_rect(center = (argonTwo.positionX,argonTwo.positionY))
argonThreeRectImage = images['AElc3'].get_rect(center = (argonThree.positionX,argonThree.positionY))

#defining icon and title
pygame.display.set_caption('Argon')
pygame.display.set_icon(images['icon'])

#game loop
while mainGame:
  screen.blit(images['Abg'],(0,0))
  
  argon.blitargonOne()
  argonTwo.blitargonTwo()
  argonThree.blitargonThree()

  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  clock.tick(fps)
  pygame.display.update()





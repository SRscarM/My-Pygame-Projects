'''
Author: Sourav
Date of Creation: 19/12/21
Class: 9th
Section: A
'''
#NITROGEN

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

images['Nbg'] = pygame.image.load(os.path.join("data", "Images", "nytrogen", "NitrogenBg.png")).convert_alpha()
images['NElc1'] =pygame.image.load(os.path.join("data", "Images", "nytrogen", "HeliumElectrons.png")).convert_alpha()
images['NElc2'] = pygame.image.load(os.path.join("data", "Images", "nytrogen", "NitrogenElectron2.png")).convert_alpha()

#HYDROGEN object
class NytrogenOne:

  def __init__(self):
    self.angle = 0
    self.image = images['NElc1']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotateNytrogenOne(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitNytrogenOne(self):
    self.angle +=   4
    nytrogenRotated, nytrogenRotatedRect = self.rotateNytrogenOne(self.image, self.angle)
    screen.blit(nytrogenRotated, nytrogenRotatedRect)

class NytrogenTwo:

  def __init__(self):
    self.angle = 0
    self.image = images['NElc2']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotateNytrogenTwo(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitNytrogenTwo(self):
    self.angle +=   2
    nytrogenRotated, nytrogenRotatedRect = self.rotateNytrogenTwo(self.image, self.angle)
    screen.blit(nytrogenRotated, nytrogenRotatedRect)


#objects
nytrogen = NytrogenOne()
nytrogenTwo = NytrogenTwo()

nytrogenRectImage = images['NElc1'].get_rect(center = (nytrogen.positionX,nytrogen.positionY))
nytrogenTwoRectImage = images['NElc2'].get_rect(center = (nytrogenTwo.positionX,nytrogenTwo.positionY))

#defining icon and title
pygame.display.set_caption('Nytrogen')
pygame.display.set_icon(images['icon'])

#game loop
while mainGame:
  screen.blit(images['Nbg'],(0,0))
  
  nytrogen.blitNytrogenOne()
  nytrogenTwo.blitNytrogenTwo()

  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  clock.tick(fps)
  pygame.display.update()





'''
Author: Sourav
Date of Creation: 19/12/21
Class: 9th
Section: A
'''
#LITHUM


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

images['Lbg'] = pygame.image.load(os.path.join("data", "Images", "lithium", "LithiumBg.png")).convert_alpha()
images['LElc1'] =pygame.image.load(os.path.join("data", "Images", "lithium", "HeliumElectrons.png")).convert_alpha()
images['LElc2'] = pygame.image.load(os.path.join("data", "Images", "lithium", "LithiumElectron2.png")).convert_alpha()

#HYDROGEN object
class LithiumOne:

  def __init__(self):
    self.angle = 0
    self.image = images['LElc1']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotateLithiumOne(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitLithiumOne(self):
    self.angle +=   4
    lithiumRotated, lithiumRotatedRect = self.rotateLithiumOne(self.image, self.angle)
    screen.blit(lithiumRotated, lithiumRotatedRect)

class LithiumTwo:

  def __init__(self):
    self.angle = 0
    self.image = images['LElc2']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotateLithiumTwo(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitLithiumTwo(self):
    self.angle +=   2
    lithiumRotated, lithiumRotatedRect = self.rotateLithiumTwo(self.image, self.angle)
    screen.blit(lithiumRotated, lithiumRotatedRect)


#objects
lithium = LithiumOne()
lithiumTwo = LithiumTwo()

lithiumRectImage = images['LElc1'].get_rect(center = (lithium.positionX,lithium.positionY))
lithiumTwoRectImage = images['LElc2'].get_rect(center = (lithiumTwo.positionX,lithiumTwo.positionY))

#defining icon and title
pygame.display.set_caption('Lithium')
pygame.display.set_icon(images['icon'])

#game loop
while mainGame:
  screen.blit(images['Lbg'],(0,0))
  
  lithium.blitLithiumOne()
  lithiumTwo.blitLithiumTwo()

  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  clock.tick(fps)
  pygame.display.update()





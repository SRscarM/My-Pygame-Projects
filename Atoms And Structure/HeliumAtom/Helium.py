'''
Author: Sourav
Date of Creation: 19/12/21
Class: 9th
Section: A
'''
#HELIUM


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

images['Hebg'] = pygame.image.load(os.path.join("data", "Images", "helium", "HeliumBg.png")).convert_alpha()
images['HeElc'] = pygame.image.load(os.path.join("data", "Images", "helium", "HeliumElectrons.png")).convert_alpha()

#HYDROGEN object
class Helium:

  def __init__(self):
    self.angle = 0
    self.image = images['HeElc']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotateHelium(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitHelium(self):
    self.angle +=   4
    heliumRotated, heliumRotatedRect = self.rotateHelium(self.image, self.angle)
    screen.blit(heliumRotated, heliumRotatedRect)


#objects
helium= Helium()

heliumRectImage = images['HeElc'].get_rect(center = (helium.positionX,helium.positionY))

#defining icon and title
pygame.display.set_caption('Helium')
pygame.display.set_icon(images['icon'])

#game loop
while mainGame:
  screen.blit(images['Hebg'],(0,0))
  
  helium.blitHelium()

  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  clock.tick(fps)
  pygame.display.update()





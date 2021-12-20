'''
Author: Sourav
Date of Creation: 19/12/21
Class: 9th
Section: A
'''
#HYDROGEN


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

images['Hbg'] = pygame.image.load(os.path.join("data", "Images", "hydrogen", "HydrogenBg.png")).convert_alpha()
images['HbgElc'] = pygame.image.load(os.path.join("data", "Images", "hydrogen", "HydrogenEelectron.png")).convert_alpha()

#HYDROGEN object
class Hydrogen:

  def __init__(self):
    self.angle = 0
    self.image = images['HbgElc']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotateHydrogen(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitHydrogen(self):
    self.angle +=   4
    hydrogenRotated, hydrogenRotatedRect = self.rotateHydrogen(self.image, self.angle)
    screen.blit(hydrogenRotated, hydrogenRotatedRect)


#objects
hydrogen = Hydrogen()

hydrogenRectImage = images['HbgElc'].get_rect(center = (hydrogen.positionX,hydrogen.positionY))

#defining icon and title
pygame.display.set_caption('Hydrogen')
pygame.display.set_icon(images['icon'])

#game loop
while mainGame:
  screen.blit(images['Hbg'],(0,0))
  
  hydrogen.blitHydrogen()

  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  clock.tick(fps)
  pygame.display.update()





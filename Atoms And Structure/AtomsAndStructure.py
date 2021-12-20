'''
Author: Sourav
Date of Creation: 19/12/21
Class: 9th
Section: A
'''

#importing modules
import pygame
import math
import sys

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
images['HbgElc'] = pygame.image.load(os.path.join("data", "Images", "hydrogen", "HydrogenElectron.png")).convert_alpha()

images['Hebg'] = pygame.image.load(os.path.join("data", "Images", "helium", "HeliumBg.png")).convert_alpha()
images['HeElc'] = pygame.image.load(os.path.join("data", "Images", "helium", "HeliumElectrons.png")).convert_alpha()

images['Lbg'] = pygame.image.load(os.path.join("data", "Images", "lithium", "LithiumBg.png")).convert_alpha()
images['LElc1'] = images['HeElc']
images['LElc2'] = pygame.image.load(os.path.join("data", "Images", "lithium", "LithiumElectron2.png")).convert_alpha()

images['Nbg'] = pygame.image.load(os.path.join("data", "Images", "nytrogen", "NitrogenBg.png")).convert_alpha()
images['NElc1'] = images['HeElc']
images['NElc2'] = pygame.image.load(os.path.join("data", "Images", "nytrogen", "NitrogenElectron2.png")).convert_alpha()

images['Obg'] = pygame.image.load(os.path.join("data", "Images", "oxygen", "OxygenBg.png")).convert_alpha()
images['OElc1'] = images['HeElc']
images['OElc2'] = pygame.image.load(os.path.join("data", "Images", "oxygen", "OxygenElectron2.png")).convert_alpha()

images['Clbg'] = pygame.image.load(os.path.join("data", "Images", "chlorine", "OxygenBg.png")).convert_alpha()
images['ClElc1'] = images['HeElc']
images['ClElc2'] = pygame.image.load(os.path.join("data", "Images", "chlorine", "OxygenElectron2.png")).convert_alpha()

#mercury object
class Mercury:

  def __init__(self):
    self.angle = 0
    self.image = images['mercury']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotateMercury(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitMercury(self):
    self.angle +=   1.6074546675621
    mercuryRotated,mercuryRotatedRect = self.rotateMercury(self.image, self.angle)
    screen.blit(mercuryRotated,mercuryRotatedRect)

#venus object
class Venus:

  def __init__(self):
    self.angle = 0
    self.image = images['venus']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotateVenus(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitVenus(self):
    self.angle +=  1.175957018133
    venusRotated,venusRotatedRect = self.rotateVenus(self.image, self.angle)
    screen.blit(venusRotated,venusRotatedRect)

#earth object
class Earth:

  def __init__(self):
    self.angle = 0
    self.image = images['earth']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotateEarth(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitEarth(self):
    self.angle += 1
    earthRotated,earthRotatedRect = self.rotateEarth(self.image, self.angle)
    screen.blit(earthRotated,earthRotatedRect)

#mars object
class Mars:

  def __init__(self):
    self.angle = 0
    self.image = images['mars']
    self.positionX = (screenX / 2)
    self.positionY = (screenY / 2)

  def rotateMars(self, surface, angle):
    rotatedSurface = pygame.transform.rotozoom(surface, -angle, 1)
    rotatedRect = rotatedSurface.get_rect(center = (self.positionX,self.positionY))
    return rotatedSurface, rotatedRect

  def blitMars(self):
    self.angle += 0.80849563465413
    marsRotated,marsRotatedRect = self.rotateMars(self.image, self.angle)
    screen.blit(marsRotated,marsRotatedRect)

#objects
earth = Earth()
mercury = Mercury()
venus = Venus()
mars = Mars()

mercuryRectImage = images['mercury'].get_rect(center = (mercury.positionX,mercury.positionY))
venusRectImage = images['venus'].get_rect(center = (venus.positionX,venus.positionY))
earthRectImage = images['earth'].get_rect(center = (earth.positionX,earth.positionY))
marsRectImage = images['mars'].get_rect(center = (earth.positionX,earth.positionY))

#defining icon and title
pygame.display.set_caption('Solar System')
pygame.display.set_icon(images['icon'])

#game loop
while mainGame:
  screen.blit(images['bg'],(0,0))
  
  mercury.blitMercury()
  venus.blitVenus()
  earth.blitEarth()
  mars.blitMars()

  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  clock.tick(fps)
  pygame.display.update()





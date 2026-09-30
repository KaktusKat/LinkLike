import pygame
import math
import copy
from hitBox import hitBox
from Vector import Vector

class sprite:
   def __init__(self, img, posX, posY, w, h,images,hitBoxL, count = 1, soild = False):
      self.x      = posX
      self.y      = posY
      self.image  = []
      self.hitBox = hitBox(self,copy.deepcopy(hitBoxL))
      for i in range(len(img)):
         self.image.append("images/"+img[i])
         image = pygame.image.load("images/"+img[i])
         images[self.image[i]] = pygame.transform.scale(image,(w,h))
      self.h           = h
      self.w           = w
      self.flip        = False
      self.flipS       = False
      self.num         = count
      self.image_index = 0
      self.soild       = soild
      self.velocityX   = 0
      self.velocityY   = 0
      self.circleTiles = []

   def move(self,offsetb = 0,offseta = 0):
      self.image_index += 1
      if self.image_index >= len(self.image)-offseta:
          self.image_index = 0+offsetb

   def draw(self, screen):
      img = screen.images[self.image[self.image_index]]
      if self.flipS:
         img = pygame.transform.flip(img,True,False)
      if self.flip:
         img = pygame.transform.flip(img,False,True)
      screen.blit(img, self.x, self.y)

   def circle(self,radius,screen,place,player):
      self.circleTiles = []
      for x in range(int(2*radius+1)):
         for y in range(int(2*radius+1)):
            X   = x-int(radius) + self.x//58
            Y   = y-int(radius) + self.y//58
            key = place.genKeyC(X, Y)
            if not key in place.map_dic:
               return
            tile = place.map_dic[key]
            ab   = ((tile.x-self.x)//58)**2+((tile.y-self.y)//58)**2
            if ab <= radius**2:
               self.circleTiles.append(tile)



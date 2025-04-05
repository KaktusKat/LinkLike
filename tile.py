import pygame
from sprite import sprite

class tile(sprite):
   def __init__(self,img,posX,posY,w,h):
       super().__init__(img,posX,posY,w,h)
   
   def draw(self,screen):
       screen.blit(self.image[0],(self.x,self.y))

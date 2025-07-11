import pygame
from sprite import sprite

class tile(sprite):
   def __init__(self, img, posX, posY, w, h,soild,breakable = True):
       super().__init__(img, posX, posY, w, h, soild=soild)
       self.breakable = breakable

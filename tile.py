import pygame
from sprite import sprite

class tile(sprite):
   def __init__(self, img, posX, posY, w, h,stuff):
       super().__init__(img, posX, posY, w, h, stuff=stuff)

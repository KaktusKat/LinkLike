import pygame
import numpy as np
import random
from sprite import sprite

class tile(sprite):
   def __init__(self, img, posX, posY, w, h,images,soild):
       super().__init__(img, posX, posY, w, h,images, soild=soild)
       self.numRow       = 0
       self.bounce       = 0.95
       self.chestList    = [0]
       self.connectS     = {-1:False,1:False}
       self.connectU     = {-1:False,1:False}
       self.nextTo       = []
       self.emptyNear    = 0
       self.health       = 0
       self.iframes      = False
       self.toolHit      = 0

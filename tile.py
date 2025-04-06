import pygame
from sprite import sprite

class tile(sprite):
   def __init__(self, img, posX, posY, w, h,stuff):
       super().__init__(img, posX, posY, w, h, stuff=stuff)
   
   def draw(self,screen):
       screen.blit(self.image[0],(self.x,self.y))

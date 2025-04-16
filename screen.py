
import pygame

class screen:
   def __init__(self, width, height):
      self.screen = pygame.display.set_mode((width, height))
      self.width  = width
      self.height = height 

   def clear(self, x, y):
      self.screen.fill((9,110,0))
      self.pos_x = x - (self.width//2)
      self.pos_y = y - (self.height//2)
      

   def blit(self, image, x, y):
      self.screen.blit(image, (x - self.pos_x, y - self.pos_y))


import pygame

class screen:
   def __init__(self, width, height):
      self.screen = pygame.display.set_mode((width, height))
      self.width  = width
      self.height = height 
      self.background_col = (9, 110, 0)

   def clear(self, centre_x, centre_y):
      self.screen.fill(self.background_col)
      self.top_left_x = centre_x - (self.width//2)
      self.top_left_y = centre_y - (self.height//2)
      
   def blit(self, image, world_x, world_y):
      self.screen.blit(image, (world_x - self.top_left_x, world_y - self.top_left_y))

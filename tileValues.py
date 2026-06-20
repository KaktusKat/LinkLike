import pygame

class tileValues:
   def __init__(self,image,soild,breakable,w,h):
      self.image = []
      for img in image:
         image = pygame.image.load(img)
         self.image.append(pygame.transform.scale(image,(w,h)))
      self.soild     = soild
      self.breakable = breakable

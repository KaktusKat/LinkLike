import pygame

class tileValues:
   def __init__(self,image,soild,breakable,w,h,toolList = [],item = [],change = [],portal = False):
      self.image = []
      for img in image:
         image = pygame.image.load("images/"+img)
         self.image.append(pygame.transform.scale(image,(w,h)))
      self.soild     = soild
      self.breakable = breakable
      self.toolList  = toolList
      self.item      = item
      self.change    = change
      self.portal    = portal

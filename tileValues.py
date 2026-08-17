import pygame

class tileValues:
   def __init__(self,image,soild,breakable,w,h,images,toolList = [],item = [],change = [],portal = False):
      self.image = []
      for img in image:
         self.image.append("images/"+img)
         image = pygame.image.load("images/"+img)
         images["images/"+img] = pygame.transform.scale(image,(w,h))
      self.soild     = soild
      self.breakable = breakable
      self.toolList  = toolList
      self.item      = item
      self.change    = change
      self.portal    = portal

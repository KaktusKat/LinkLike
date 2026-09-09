import pygame

class tileValues:
   def __init__(self,image,soild,breakable,w,h,images,sound,noise = [],toolList = [],item = [],change = [],bounce = 0.95,portal = False,aW = 58,aH = 58):
      self.image = []
      for img in image:
         self.image.append("images/"+img)
         image = pygame.image.load("images/"+img)
         images["images/"+img] = pygame.transform.scale(image,(aW,aH))
      self.noise = []
      for n in noise:
          self.noise = sound.loadS(n)
      self.soild     = soild
      self.breakable = breakable
      self.toolList  = toolList
      self.item      = item
      self.bounce    = bounce
      self.change    = change
      self.w         = w
      self.h         = h
      self.portal    = portal

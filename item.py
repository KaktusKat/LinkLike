import pygame

class item:
   def __init__(self,x,y,w,h,name,img,pageNum):
      self.x       = x
      self.y       = y
      self.w       = w
      self.h       = h
      self.name    = name
      self.image   = pygame.image.load(img)
      self.image   = pygame.transform.scale(self.image,(w,h))
      self.amount  = 0
      self.pageNum = pageNum

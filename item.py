import pygame

class item:
   def __init__(self,x,y,w,h,images,name,img,pageNum):
      self.x             = x
      self.y             = y
      self.w             = w
      self.h             = h
      self.name          = name
      self.image         = "images/"+img
      image              = pygame.image.load("images/"+img)
      images[self.image] = pygame.transform.scale(image,(w,h))
      self.amount        = 0
      self.pageNum       = pageNum

import pygame

class item:
   def __init__(self,x,y,w,h,images,name,img,pageNum,health = 0,level = 0):
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
      self.health        = health
      self.level         = level

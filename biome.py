import pygame

class biome:
   def __init__(self,name,size,rarity,images):
      self.name   = name
      self.size   = size
      self.rarity = rarity
      self.images = []
      self.prob   = []
      total       = 0
      for img in images:
         self.images.append(img[0])
         total += img[1]
      for img in images:
         self.prob.append(img[1]/total)

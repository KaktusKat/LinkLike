import pygame

class biome:
   def __init__(self,name,size,rarity,images1,images2,connectors):
      self.name       = name
      self.size       = size
      self.rarity     = rarity
      self.images1    = []
      self.images2    = []
      self.prob1      = []
      self.prob2      = []
      self.connectors = connectors
      total           = 0
      for img in images1:
         self.images1.append(img[0])
         total += img[1]
      for img in images1:
         self.prob1.append(img[1]/total)
      total           = 0
      for img in images2:
         self.images2.append(img[0])
         total += img[1]
      for img in images2:
         self.prob2.append(img[1]/total)


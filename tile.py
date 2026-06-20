import pygame
from sprite import sprite

class tile(sprite):
   def __init__(self, img, posX, posY, w, h,soild,biomes = [],breakable = True,portal = False,craft = False,spike = False,justMade = False):
       super().__init__(img, posX, posY, w, h, soild=soild)
       self.breakable = breakable
       self.portal    = portal
       self.craft     = False
       self.spike     = spike
       self.nextTo     = []
       self.emptyNear  = 0
       self.biomeNear  = {}
       self.nameList   = []
       self.numbList   = []
       self.biomes     = biomes
       self.rarity     = 0
       self.maxProb    = 0
       self.biome      = 0
       self.justMade   = justMade
       a = -1
       for biome in self.biomes:
          a += 1
          self.biomeNear[biome.name] = 0
          self.nameList.append(biome.name)
          self.numbList.append(a)
          self.rarity += biome.rarity


   def near(self,titleList,place):
      self.biomeNear = {}
      for biome in self.biomes:
         self.biomeNear[biome.name] = 0
      self.emptyNear = 0
      self.nextTo = []
      self.nextTo.append(titleList[place.genKeyC((self.x//58)+1,self.y//58)])
      self.nextTo.append(titleList[place.genKeyC((self.x//58)-1,self.y//58)])
      self.nextTo.append(titleList[place.genKeyC(self.x//58,(self.y//58)+1)])
      self.nextTo.append(titleList[place.genKeyC(self.x//58,(self.y//58)-1)])
      for title in self.nextTo:
         if title.biome == 0:
            self.emptyNear += 1
         for biome in self.biomes:
            if title.biome == biome.name:
               self.biomeNear[biome.name] += 1


   def probabilaty(self):
      self.prob = {}
      for biome in self.biomes:
         self.prob[biome.name] = 0
      sumSizes = self.emptyNear
      for biome in self.biomes:
         prob    = (self.biomeNear[biome.name]*biome.size) + (self.emptyNear*biome.rarity/self.rarity)
         sumSizes += self.biomeNear[biome.name]*biome.size
         self.prob[biome.name] = prob
      for k in self.prob:
         self.prob[k] /= (sumSizes)
#      print(self.prob)
      self.maxProb = max(list(dict.values(self.prob)))




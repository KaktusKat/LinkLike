import pygame
import numpy as np
import random
from sprite import sprite

class tile(sprite):
   def __init__(self, img, posX, posY, w, h,soild,biomes = [],breakable = True,portal = False,craft = False,spike = False,justMade = False,numRow = 0,reducedNoise = False):
       super().__init__(img, posX, posY, w, h, soild=soild)
       self.numRow       = numRow
       self.reducedNoise = reducedNoise
       self.breakable    = breakable
       self.portal       = portal
       self.craft        = False
       self.spike        = spike
       self.nextTo       = []
       self.emptyNear    = 0
       self.biomeNear    = {}
       self.nameList     = []
       self.numbList     = []
       self.biomes       = biomes
       self.type         = 0
       self.rarity       = 0
       self.maxProb      = 0
       self.biome        = 0
       self.justMade     = justMade
       self.iron         = False
       self.health       = 0
       self.iframes      = False
       self.toolHit      = 0
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
      self.maxProb = max(list(dict.values(self.prob)))


   def randomPlace(self,img1,img2):
      if random.randint(0,1) == 1:
         self.type  = "wall"
         self.image = [img1]
         self.soild = True
      else:
        self.type  = "empty"
        self.image = [img2]
        self.soild = False

   def nebiors(self,tileList,width):
      posList     = [self.x//29,self.y//29]
      posList     = [int(posList[0]),int(posList[1])]
      self.nextTo = []
      for x in range(-1,2):
         for y in range(-1,2):
            self.nextTo.append(tileList[(posList[0]+x)][(posList[1]+y)])

   def reduceNoise(self,backG,block,blocks):
      numWall  = 0
      numEmpty = 0
      for tile in self.nextTo:
         if tile.type == "wall":
           numWall += 1
         else:
           numEmpty += 1
      self.type   = "empty"
      self.image  = [backG]
      self.soild  = False
      if numWall >= 5:
         self.type   = "wall"
         a           = np.random.choice(blocks,p = [0.95,0.05])
         self.soild  = True
         if a == "stone":
            self.image = [block[0]]
         else:
            self.image = [block[1]]
            self.iron  = True
                                                                                                                


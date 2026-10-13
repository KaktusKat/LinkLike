import random
from tileF import tileF
import numpy as np
import pygame
from tileC import tileC

class Cave:

   def __init__(self,biomes,outLine):
      self.tileList  = {}
      self.tileList2 = {}
      self.tile1     = {"wall":{},"empty":{}}
      self.prob1     = {"wall":{},"empty":{}}
      self.tile2     = {"wall":{},"empty":{}}
      self.prob2     = {"wall":{},"empty":{}}
      self.biomes    = biomes
      self.outLine   = outLine
      for biome in biomes:
         self.tile1["empty"][biome.name] = biome.images1
         self.prob1["empty"][biome.name] = biome.prob1
         self.tile1["wall"][biome.name]  = biome.images1W
         self.prob1["wall"][biome.name]  = biome.prob1W
         self.tile2["empty"][biome.name] = biome.images2
         self.prob2["empty"][biome.name] = biome.prob2
         self.tile2["wall"][biome.name]  = biome.images2W
         self.prob2["wall"][biome.name]  = biome.prob2W

   def update(self,screen,sound,player,weaponList,biomeList,perlinNoiseL,struct):
      near = []
      keys = pygame.key.get_pressed()
      new  = []
      for x in range (-14,14):
         for y in range(-14,14):
            keyX   = x+(player.x//29)
            keyY   = y+(player.y//29)
            inList = True
            out    = False
            noise  = []
            for value in [-14,13]:
               if x == value:
                  out = [value / abs(value),0]
               if y == value:
                  out = [0,value / abs(value)]
            if not keyX in self.tileList:
               self.tileList[keyX]  = {}
               self.tileList2[keyX] = {}
            if not keyY in self.tileList[keyX]:
               self.tileList[keyX][keyY]  = tileC(["CaveWall.png"],keyX*29,keyY*29,29,29,screen.images,[[0,0,29,29]],True,1,numRow = 1)
               self.tileList2[keyX][keyY] = tileC(["CaveWall.png"],keyX*29,keyY*29,29,29,screen.images,[[0,0,29,29]],True,2,numRow = 1)
               self.tileList[keyX][keyY].randomPlace()
               if out:
                  self.tileList[keyX][keyY].outD = out
                  self.tileList[keyX][keyY].out  = True
               if not out:
                  self.tileList[keyX][keyY].out = False
                  new.append(self.tileList[keyX][keyY]) 
                  inList = False 
            if inList:
               if not self.tileList[keyX][keyY].reducedNoise and not out:
                  self.tileList[keyX][keyY].out = False
                  new.append(self.tileList[keyX][keyY])
               near.append(self.tileList[keyX][keyY])
               if keys[pygame.K_p]:
                  near.append(self.tileList2[keyX][keyY])
      self.add(new,keyX,keyY,screen.images,biomeList,perlinNoiseL,struct)
      for tiles in near:
          tiles.checkMined(weaponList,player,sound)
          tiles.draw(screen)

   def add(self,new,keyX,keyY,images,biomeList,perlinNoiseL,struct):
      for tile in new:
             tile.nebiors(self.tileList,580)
      for i in range(5):
         for tile in new:
            tile.reduceNoise()
            tile.reducedNoise = True
      for tile in new:
         self.makeTile(tile.x//29,tile.y//29,images,biomeList,perlinNoiseL)
         if tile.type == "empty" and tile.row == 1:
            self.outLine.load(tile,self)
         if not tile.outD == [0,0]:
            x = tile.x // 29 - tile.outD[0]
            y = tile.y // 29 - tile.outD[1]
            if self.tileList[x][y].type == "empty":
               self.outLine.load(self.tileList[x][y],self)

   def makeTile(self,keyX,keyY,images,biomeList,perlinNoiseL):
      value = []
      for perlinNoise in perlinNoiseL:
         value.append(perlinNoise.value(keyX,keyY))
         for biome in biomeList:
             biomeC = True
             for i in range(len(biome.maxMin)):
                if not (value[i] <= biome.maxMin[i][0] and value[i] >= biome.maxMin[i][1]):
                   biomeC = False
             if biomeC:
                self.change(keyX,keyY,biome)
   
   def change(self,x,y,biome):
      tileV = np.random.choice(self.tile1[self.tileList[x][y].type][biome.name],p = self.prob1[self.tileList[x][y].type][biome.name])
      tileV.makeTile(self.tileList[x][y])
      tileV = np.random.choice(self.tile2[self.tileList[x][y].type][biome.name],p = self.prob2[self.tileList[x][y].type][biome.name])
      tileV.makeTile(self.tileList2[x][y])

   def get_cell(self,x,y):
      return self.tileList[x][y]

   def getCell(self,x,y,xA = 0,yA = 0):
      return self.tileList[x//29 + xA][y//29 + yA]

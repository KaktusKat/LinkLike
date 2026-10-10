import random
import pygame
from tileC import tileC

class Cave:

   def __init__(self,biomes,Simage):
      self.tileList = {}
      self.biomes   = biomes

   def update(self,screen,player,pickaxe,iron):
      near = []
      new  = []
      for x in range (-14,14):
         for y in range(-14,14):
            keyX   = x+(player.x//29)
            keyY   = y+(player.y//29)
            inList = True
            out    = False
            noise  = []
            if (x == -14 or x == 13) or (y == -14 or y == 13):
               out = True
            if not keyX in self.tileList:
               self.tileList[keyX] = {}
            if not keyY in self.tileList[keyX]:
               self.tileList[keyX][keyY] = tileC(["CaveBackground.png"],keyX*29,keyY*29,29,29,screen.images,[[0,0,29,29]],True,numRow = 1)
               self.tileList[keyX][keyY].randomPlace(self.images[1],self.images[0])
               if not out:
                  new.append(self.tileList[keyX][keyY])
                  inList = False
            if inList:
               if not self.tileList[keyX][keyY].reducedNoise and not out:
                  new.append(self.tileList[keyX][keyY]) 
               near.append(self.tileList[keyX][keyY])
      self.add(new)
      for tiles in near:
          if pickaxe.attacking and tiles.isHit(pickaxe) and tiles.soild:
             tiles.image = [self.images[0]]
             tiles.soild = False
             if tiles.iron:
                iron.amount += 1
                tiles.iron = False
          tiles.draw(screen)

   def add(self,new):
      for tile in new:
             tile.nebiors(self.tileList,580)
      for i in range(5):
         for tile in new:
            tile.reduceNoise(self.images[0],[self.images[1],self.images[2]],["stone","iron"])
            tile.reducedNoise = True

   def get_cell(self,x,y):
      return self.tileList[x][y]

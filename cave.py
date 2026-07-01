import random
import pygame
from tile import tile

class Cave:

   def __init__(self,images):
      self.images   = []
      for img in images:
         image = pygame.image.load(img)
         image = pygame.transform.scale(image,(58,58))
         self.images.append(image)
      self.spikes   = 0
      self.tileList = {}

   def update(self,screen,player,pickaxe):
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
               self.tileList[keyX][keyY] = tile(["CaveBackground.png"],(player.x//29)*29+x*29,(player.y//29)*29+y*29,29,29,True,numRow = 1)
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
          tiles.draw(screen)

   def add(self,new):
      for tile in new:
             tile.nebiors(self.tileList,580)
      for i in range(5):
         for tile in new:
            tile.reduceNoise(self.images[0],self.images[1])
            tile.reducedNoise = True

   def get_cell(self,x,y):
      return self.tileList[x][y]

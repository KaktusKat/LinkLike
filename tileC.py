import numpy as np
import random
from tile import tile

class tileC(tile):
   def __init__(self,img,posX,posY,w,h,images,hitBoxL,soild,row,numRow = 0):
      super().__init__(img,posX,posY,w,h,images,hitBoxL,soild)
      self.reducedNoise = False
      self.outD         = [0,0]
      self.numRow       = numRow
      self.fence        = False
      self.fenceDraw    = []
      self.row          = row
      self.type         = 0
      self.toolList     = []
      self.iron         = False
      self.nextTo       = []

   def randomPlace(self):
      if random.randint(0,1) == 1:
         self.type  = "wall"
      else:
        self.type  = "empty"

   def nebiors(self,tileList,width):
      posList     = [self.x//58,self.y//58]
      posList     = [int(posList[0]),int(posList[1])]
      self.nextTo = []
      for x in range(-1,2):
         for y in range(-1,2):
            self.nextTo.append(tileList[(posList[0]+x)][(posList[1]+y)])

   def reduceNoise(self):
      numWall  = 0
      numEmpty = 0
      for tile in self.nextTo:
         if tile.type == "wall":
           numWall += 1
         else:
           numEmpty += 1
      self.type   = "empty"
      if numWall >= 5:
         self.type   = "wall"

   def draw(self,screen):
      img = screen.images[self.image[self.image_index]]
      if self.flipS:
         img = pygame.transform.flip(img,True,False)
      if self.flip:
         img = pygame.transform.flip(img,False,True)
      screen.blit(img, self.x, self.y)

      for draw in self.fenceDraw:
         screen.blit(screen.images[draw[0]], self.x+draw[1], self.y+draw[2])

   def checkMined(self,weaponList,player,sound,outLine,place):
      if len(self.toolList) > 0:
         for tool in self.toolList:
            if self.hitBox.isHit(weaponList[tool[0]].hitBox) and weaponList[tool[0]].attacking and not self.iframes:
               self.health += 1
               sound.playS(self.noise)
               weaponList[tool[0]].hit   = True
               self.iframes = True
               if len(tool) == 4:
                  tool[2].amount += tool[3]
               self.toolHit = tool[0]
               if self.health >= tool[1]:
                  self.item.amount += 1
                  self.soild        = False
                  self.type         = "empty"
                  outLine.unload(self,place)
                  self.change[0].makeTile(self)


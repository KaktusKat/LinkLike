import pygame
import numpy as np
import random
from sprite import sprite

class tile(sprite):
   def __init__(self, img, posX, posY, w, h,images,hitBoxL,soild):
       super().__init__(img, posX, posY, w, h,images,hitBoxL, soild=soild)
       self.numRow       = 0
       self.bounce       = 0.95
       self.chestList    = [0]
       self.nextTo       = []
       self.lightSource  = False
       self.emptyNear    = 0
       self.health       = 0
       self.iframes      = False
       self.toolHit      = 0

   def checkMined(self,weaponList,player,sound,place):
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
                  self.change[0].makeTile(self)


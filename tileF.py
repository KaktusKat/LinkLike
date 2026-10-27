from tile import tile

class tileF(tile):
   def __init__(self,img,posX,posY,w,h,images,hitBoxL,solid,fenceO,**args):
      super().__init__(img,posX,posY,w,h,images,hitBoxL,solid,**args)
      self.fenceDraw = []
      self.fence     = True
      self.fenceO    = fenceO

   def draw(self,screen):
      super().draw(screen)

      for draw in self.fenceDraw:
         screen.blit(screen.images[draw[0]], self.x+draw[1], self.y+draw[2])

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
                  self.fenceO.objectList.remove(self)
                  self.fenceO.unloadN(self,place)
                  self.change[0].makeTile(self)
      

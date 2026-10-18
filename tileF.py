from tileO import tileO

class tileF(tileO):
   def __init__(self,img,posX,posY,w,h,images,hitBoxL,solid,fenceO,biomes = []):
      super().__init__(img,posX,posY,w,h,images,hitBoxL,solid,biomes)
      self.fenceDraw = []
      self.fenceO    = fenceO

   def draw(self,screen):
      img = screen.images[self.image[self.image_index]]
      if self.flipS:
         img = pygame.transform.flip(img,True,False)
      if self.flip:
         img = pygame.transform.flip(img,False,True)
      screen.blit(img, self.x, self.y)

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
      

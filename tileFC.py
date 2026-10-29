from tileC import tileC
from tileF import tileF

class tileFC(tileF,tileC):
   def __init__(self,img,posX,posY,w,h,images,hitBoxL,solid,fenceO,row,numRow = 0):
      super().__init__(img=img,posX=posX,posY=posY,w=w,h=h,images=images,hitBoxL=hitBoxL,solid=solid,fenceO=fenceO,row=row,numRow=numRow)

   def checkMined(self,weaponList,player,sound,outLine,place):
      if len(self.toolList) > 0:
         for tool in self.toolList:
            if self.hitBox.isHit(weaponList[tool[0]].hitBox) and weaponList[tool[0]].attacking and not self.iframes:
               self.health += 1
               sound.playS(self.noise)
               weaponList[tool[0]].hit   = self
               self.iframes = True
               if len(tool) == 4:
                  tool[2].amount += tool[3]
               self.toolHit = tool[0]
               if self.health >= tool[1]:
                  self.item.amount += 1
                  self.soild        = False
                  self.type         = "empty"
                  outLine.unload(self,place)
                  self.fenceO.objectList.remove(self)
                  self.fenceO.unloadN(self,place)
                  self.change[0].makeTile(self)


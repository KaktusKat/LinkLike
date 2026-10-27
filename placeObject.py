from tileO import tileO
from tileFO import tileFO
from tileFC import tileFC
import pygame
from place import place as Place
from cave  import Cave

class placeObject:
   def __init__(self,name,item,images,change,hitBoxLC,w,h,aW,aH,tileV,imageI):
      self.changeI    = change
      self.item       = item
      self.tileV      = tileV
      self.w          = w
      self.name       = name
      self.hitBoxLC   = hitBoxLC
      self.h          = h
      self.objectList = []
      self.timer      = 0
      self.imageI     = "images/"+imageI
      image = pygame.image.load("images/"+imageI)
      images[self.imageI] = pygame.transform.scale(image,(75,75))
      self.select     = "images/select.png"
      image = pygame.image.load(self.select)
      images[self.select] = pygame.transform.scale(image,(75,75))
      self.imagesC = []
      for img in change:
         image = pygame.image.load("images/"+change[img][0])
         images[change[img][0]] = pygame.transform.scale(image,(change[img][3],change[img][4]))


   def place(self,itemDict,place,screen,biomeList):
      self.timer += 1
      Mpress = pygame.mouse.get_pressed()
      Mpos   = pygame.mouse.get_pos()

      if Mpress[2] and self.timer > 0 and itemDict[self.item.name].amount > 0:
         self.timer = -15
         x,y  = screen.convertSTW(Mpos[0],Mpos[1])
         tile  = place.getCell(x,y,level = 1)
         tile2 = place.getCell(x,y,level = 2)
         if tile:
            if not tile.soild and not tile2.soild:
               itemDict[self.item.name].amount -= 1
               self.change(tile,place,screen.images,biomeList)

   def change(self,tile,place,images,biomeList):
      x   = tile.x
      y   = tile.y

      if type(place) is Place:
         tile = tileFO(["empty.png"],x,y,58,58,images,[],True,biomeList,self)
         place.map_dic2[place.genKeyP(tile.x,tile.y)] = tile
      else:
         tile = tileFC(["empty.png"],x,y,58,58,images,[],True,self,1)
         place.tileList2[tile.x//58][tile.y//58] = tile
      self.tileV.makeTile(tile)
      self.loadN(tile,place)
      self.objectList.append(tile)
      

   def unloadN(self,tile,place):
      tile.fence = False
      for x in range(-1,2):
         for y in range(-1,2):

            if not abs(x) + abs(y) == 2 and not abs(x) + abs(y) == 0:

               tileC  = place.getCell(tile.x,tile.y,x,y,2)
               if tileC:
                  if tileC.fence:
                     tile.hitBox.hitBoxList.remove(self.hitBoxLC[str(x)+str(y)])
                     tile.fenceDraw.remove(self.changeI[str(x)+str(y)])
                     
                     tileC.hitBox.hitBoxList.remove(self.hitBoxLC[str(-x)+str(-y)])
                     tileC.fenceDraw.remove(self.changeI[str(-x)+str(-y)])
   
   def loadN(self,tile,place):
      for x in range(-1,2):
         for y in range(-1,2):

            if not abs(x) + abs(y) == 2 and not abs(x) + abs(y) == 0:

               tileC = place.getCell(tile.x,tile.y,x,y,2)
               if tileC:
                  if tileC.fence:
                     tile.hitBox.hitBoxList.append(self.hitBoxLC[str(x)+str(y)])
                     tile.fenceDraw.append(self.changeI[str(x)+str(y)])

                     tileC.hitBox.hitBoxList.append(self.hitBoxLC[str(-x)+str(-y)])
                     tileC.fenceDraw.append(self.changeI[str(-x)+str(-y)])

   def draw(self,screen):
      screen.screen.blit(screen.images[self.select],(110,10))
      screen.screen.blit(screen.images[self.imageI],(110,10))



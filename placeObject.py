from tileO import tileO
from tileF import tileF
import pygame

class placeObject:
   def __init__(self,name,item,images,change,hitBoxLC,w,h,aW,aH,imagesC,tileV,imageI,connector = True):
      self.changeI    = change
      self.connector  = connector
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
      for i in range(len(imagesC)):
         self.imagesC.append("images/"+imagesC[i][0])
         image = pygame.image.load("images/"+imagesC[i][0])
         images[self.imagesC[i]] = pygame.transform.scale(image,(imagesC[i][1],imagesC[i][2]))


   def place(self,itemDict,place,screen,biomeList):
      self.timer += 1
      Mpress = pygame.mouse.get_pressed()
      Mpos   = pygame.mouse.get_pos()

      if Mpress[2] and self.timer > 0 and itemDict[self.item.name].amount > 0:
         self.timer = -15
         x,y = screen.convertSTW(Mpos[0],Mpos[1])
         x   = x // 58
         y   = y // 58
         key = place.genKeyC(x,y)
         if not place.map_dic2[key].soild:
            itemDict[self.item.name].amount -= 1
            self.change(place,key,screen.images,biomeList)

   def change(self,place,key,images,biomeList):
            x = place.map_dic2[key].x
            y = place.map_dic2[key].y

            if self.connector:
               place.map_dic2[key]    = tileF(["empty.png"],x,y,58,58,images,[],True,biomeList)
               tile                   = place.map_dic2[key]
               tile.fence = True
            else:
               place.map_dic2[key]    = tileO(["empty.png"],x,y,58,58,images,[],True,biomeList)
            tile                   = place.map_dic2[key]
            self.tileV.makeTile(tile)
            self.loadN(tile,place)
            self.objectList.append(tile)
      

   def unloadN(self,tile,place):
      tile.fence = False
      for x in range(-1,2):
         for y in range(-1,2):

            if not abs(x) + abs(y) == 2 and not abs(x) + abs(y) == 0:

               key   = place.genKeyP(x * 58+tile.x,y * 58+tile.y)
               if key in place.map_dic2:
                  tileC = place.map_dic2[key]
                  if tileC.fence and self.hitBoxLC[str(x)+str(y)] in tile.hitBox.hitBoxList:
                     tile.hitBox.hitBoxList.remove(self.hitBoxLC[str(x)+str(y)])
                     tile.fenceDraw.remove(self.changeI[str(x)+str(y)])

                     tileC.hitBox.hitBoxList.remove(self.hitBoxLC[str(-x)+str(-y)])
                     tileC.fenceDraw.remove(self.changeI[str(-x)+str(-y)])
   
   def loadN(self,tile,place):
      for x in range(-1,2):
         for y in range(-1,2):

            if not abs(x) + abs(y) == 2 and not abs(x) + abs(y) == 0:

               key   = place.genKeyP(x * 58+tile.x,y * 58+tile.y)
               if key in place.map_dic2:
                  tileC = place.map_dic2[key]
                  if tileC.fence:
                     tile.hitBox.hitBoxList.append(self.hitBoxLC[str(x)+str(y)])
                     tile.fenceDraw.append(self.changeI[str(x)+str(y)])

                     tileC.hitBox.hitBoxList.append(self.hitBoxLC[str(-x)+str(-y)])
                     tileC.fenceDraw.append(self.changeI[str(-x)+str(-y)])

   def draw(self,screen):
      screen.screen.blit(screen.images[self.select],(110,10))
      screen.screen.blit(screen.images[self.imageI],(110,10))



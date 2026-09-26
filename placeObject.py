from tileF import tileF
import pygame

class placeObject:
   def __init__(self,item,img,images,change,hitBoxL,hitBoxLC,w,h,aW,aH,imagesC,name,noise,toolList,bounce = 0.95):
      self.item       = item
      self.changeI    = change
      self.soild      = True
      self.w          = w
      self.check      = False
      self.hitBoxL    = hitBoxL
      self.hitBoxLC   = hitBoxLC
      self.h          = h
      self.name       = name
      self.objectList = []
      self.toolList   = toolList
      self.noise      = noise
      self.timer      = 0
      self.bounce     = bounce
      self.image      = ["images/"+img]
      self.img        = [img]
      image = pygame.image.load("images/"+img)
      images[self.image[0]] = pygame.transform.scale(image,(aW,aH))
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

            place.map_dic2[key]    = tileF(self.img,x,y,58,58,images,self.hitBoxL,True,biomeList)
            tile                   = place.map_dic2[key]
            tile.toolList          = self.toolList
            tile.justMade          = place.map_dic[key].justMade
            tile.noise             = self.noise
            tile.item              = self.item
            tile.bounce            = self.bounce
            tile.made              = True
            tile.fence             = True
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



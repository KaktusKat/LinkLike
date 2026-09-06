import pygame

class placeObject:
   def __init__(self,item,img,images,w,h,aW,aH,imagesC,name,noise,toolList):
      self.item       = item
      self.w          = w
      self.h          = h
      self.name       = name
      self.objectList = []
      self.toolList   = toolList
      self.noise      = noise
      self.timer      = 0
      self.image = "images/"+img
      image = pygame.image.load("images/"+img)
      images[self.image] = pygame.transform.scale(image,(aW,aH))
      self.imagesC = []
      for i in range(len(imagesC)):
         self.imagesC.append("images/"+imagesC[i][0])
         image = pygame.image.load("images/"+imagesC[i][0])
         images[self.imagesC[i]] = pygame.transform.scale(image,(imagesC[i][1],imagesC[i][2]))


   def place(self,itemDict,place,screen):
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
            tile          = place.map_dic2[key]
            tile.image    = [self.image]
            tile.soild    = True
            tile.toolList = self.toolList
            tile.noise    = self.noise
            tile.item     = self.item
            tile.w        = self.w
            tile.h        = self.h
            self.load(tile)
            self.objectList.append(tile)

   def load(self,tile):
       for tiles in self.objectList:
           if tile.y - tiles.y == 0:
              tile.connectS[(tile.x-tiles.x)//58]         = True
              tiles.connectS[((tile.x-tiles.x)//58) * -1] = True
           if tile.x - tiles.x == 0:
              tile.connectU[(tile.y-tiles.y)//58]         = True
              tiles.connectU[((tile.y-tiles.y)//58) * -1] = True

   def draw(self,screen):
      for tile in self.objectList:
         if tile.connectS[-1]:
            screen.blit(screen.images[self.imagesC[0]],tile.x+58/2,tile.y)
         if tile.connectS[1]:
            screen.blit(screen.images[self.imagesC[0]],tile.x,tile.y)
         if tile.connectU[-1]:
            screen.blit(screen.images[self.imagesC[1]],tile.x,tile.y+58/2)
         if tile.connectU[1]:
            screen.blit(screen.images[self.imagesC[1]],tile.x,tile.y)


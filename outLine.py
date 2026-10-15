import pygame

class outLine:
   def __init__(self,images,code,Ucode,imagesS):
      self.images = images
      self.code   = code
      self.Ucode  = Ucode
      for img in images:
         image   = pygame.image.load("images/"+images[img][0])
         image   = pygame.transform.scale(image,(images[img][1],images[img][2]))
         for x in range(0,2):
            for y in range(0,2):
               imagesS[images[img][0]+str(x)+str(y)] = pygame.transform.flip(image,x,y)

   def load(self,tile,place):
      a      = 0
      placeL = []
      for x in range(-1,2):
         placeL.append([])
         for y in range(-1,2):
            tileC = place.getCell(tile.x,tile.y,x,y)
            if self.code(tileC):
               placeL[x+1].append("1")
            else:
               placeL[x+1].append("0")
      rotate = 0 
      for x in range(0,2):
         for y in range(0,2):

            cornerX = x * 2
            cornerY = y * 2

            corner  = placeL[cornerX][cornerY]
            secondS = placeL[cornerX + (1 - 2 * x)][cornerY]
            thridS  = placeL[cornerX][cornerY + (1 - 2 * y)]

            if not corner+secondS+thridS == "000":
               image    = self.images[corner+secondS+thridS]
               image    = image[0] + str(x) + str(y)
               tile.fenceDraw.append([image,0,0])
   
   def unload(self,tile,place):
      for x in range(-1,2):
         for y in range(-1,2):
            tileC = place.getCell(tile.x,tile.y,x,y)
            if self.Ucode(tileC):
               self.load(tileC,place)


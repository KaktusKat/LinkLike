import pygame

class outLine:
   def __init__(self,images,code):
      self.images = images
      self.code   = code
      for img in images:
         rotate = 0
         image   = pygame.image.load("images/"+images[img][0])
         image   = pygame.transform.scale(image,(images[img][3],images[img][4]))
         for i in range(4):
            rotate += 45
            images[images[img][0]+str(rotate)] = pygame.transform.rotate(image,rotate)


   def load(self,tile,place,screen):
      placeL = []
      for x in range(-1,2):
         placeL.append([])
         for y in range(-1,2):
            
            tileC = place.getCell(tile.x,tile.y,x,y)
            if self.code(tileC):
               placeL[x].append("1")
            else:
               placeL[x].append("0")
      rotate = 0 
      for x in range(0,2):
         for y in range(0,2):
            rotate += 45

            cornerX = x * 2
            cornerY = y * 2

            corner  = placeL[cornerX][cornerY]
            secondS = placeL[cornerX + (1 - 2 * x)][cornerY]
            thridS  = placeL[cornerX][cornerY + (1 - 2 * x)]

            image    = self.images[corner+secondS+thridS]
            image[0] = image[0] + str(rotate)
            tile.fenceDraw.append(image)

import pygame

class placeObjectT:
   def __init__(self,item,tile,name,images,image):
      self.tile       = tile
      self.objectList = []
      self.name       = name
      self.item       = item.name
      self.image      = "images/"+image
      image = pygame.image.load("images/"+image)
      images[self.image] = pygame.transform.scale(image,(75,75))
      self.select        = "images/select.png"
      image = pygame.image.load(self.select)
      images[self.select] = pygame.transform.scale(image,(75,75))


   def place(self,itemDict,place,screen,biomeList):
      Mpos   = pygame.mouse.get_pos()
      Mpress = pygame.mouse.get_pressed()
      if Mpress[2]:
        x,y  = screen.convertSTW(Mpos[0],Mpos[1])
        tile = place.getCell(x,y)
        if not tile.soild and itemDict[self.item].amount > 0:
          itemDict[self.item].amount -= 1
          self.tile.makeTile(tile)

   def draw(self,screen):
      screen.screen.blit(screen.images[self.select],(110,10))
      screen.screen.blit(screen.images[self.image],(110,10))


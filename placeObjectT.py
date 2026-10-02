import
import pygame

class placeObjectT:
   def __init__(self,tile,item):
      self.tile = tile
      self.item = item

   def place(self,itemDict,place,screen,biomeList):
      Mpos   = pygame.mouse.get_pos()
      Mpress = pygame.mouse.get_pressed()
      if Mpress[0]:
        x,y                = pygame.covertSTW(Mpos[0],Mpos[1])
        key                = place.genKeyP(x,y)
        place.map_dic[key] = 

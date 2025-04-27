import pygame

class invetory:
   def __init__(self,woodNum,wood):
      self.woodNum    = woodNum
      self.window     = False
      self.wood       = pygame.image.load(wood)
      self.wood       = pygame.transform.scale(self.wood,(50,50))
      self.placeBlock = 0
      self.place      = False
      self.timer      = 0

   def open(self,screen,keys,player,place):
       if keys[pygame.K_q] or self.window:
          pygame.draw.rect(screen.screen,(81,74,74),(screen.width/2 - 150,screen.height/2 - 150,300,300))
          self.window = True
          self.craft(screen,player,place)
       if keys[pygame.K_c]:
          self.window = False

   def craft(self,screen,player,place):
      self.woodNum = place.treesCut
      num          = pygame.font.SysFont("I don't think this dose anything",40)
      num          = num.render(f"{self.woodNum}",False,(0,0,0))
      screen.blit(num,-40+player.x,-40+player.y)
      screen.blit(self.wood,-90+player.x,-90+player.y)

   def make(self,place,screen,player):
      self.timer  -= 1 
      x,y          = pygame.mouse.get_pos()
      Mpress       = pygame.mouse.get_pressed()
      if Mpress[2] and place.treesCut > 0 and self.timer < 1:
         image = pygame.image.load("woodPlanks.png")
         x,y   = screen.convertSTW(x,y)
         key   = place.genKeyP(x,y)
         place.map_dic[key].image[0] = pygame.transform.scale(image,(58,58))
         place.map_dic[key].soild    = True
         place.treesCut -= 1
         self.timer = 20

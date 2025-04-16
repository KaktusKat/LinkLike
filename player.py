import pygame
from sprite import sprite
import math

class player(sprite):
   def __init__(self,img,posX,posY,w,h,tool):
      super().__init__(img,posX,posY,w,h)
      self.tool   = tool
      self.b      = False
      self.t      = -10
      self.wep    = 0
      self.a      = 0

   def update(self,keys,screen,place):
      a          = 0
      self.t    += 1
      Mpos       = pygame.mouse.get_pos()
      mousePress = pygame.mouse.get_pressed()
      if mousePress[0]:
         self.tool[self.wep].attack(self)
      if keys[pygame.K_SPACE] and self.t > 0:
         Rx       = Mpos[0] - self.x
         Ry       = Mpos[1] - self.y
         length   = math.sqrt(Rx*Rx + Ry*Ry)
         Dx       = Rx / length
         Dy       = Ry / length
         self.x  -= Dx * 150
         self.y  -= Dy * 150
         self.t   = -60
         return
      if keys[pygame.K_w]:
         self.y -= 1.5
         self.checkMove(0,-1.5,place)
         a+=1
      if keys[pygame.K_s]:
         self.y += 1.5
         self.checkMove(0,1.5,place)
         a+=1
      if keys[pygame.K_d]:
         self.x += 1.5
         self.checkMove(1.5,0,place)
         a+=1
      if keys[pygame.K_a]:
         self.x -= 1.5
         self.checkMove(-1.5,0,place)
         a+=1
      if a > 0:
         self.move()
      if Mpos[0] < self.x and not self.b:
         self.image[0] = pygame.transform.flip(self.image[0],True,False)
         self.image[1] = pygame.transform.flip(self.image[1],True,False)
         self.b = True
      if Mpos[0] > self.x and self.b:         
         self.image[0] = pygame.transform.flip(self.image[0],True,False)
         self.image[1] = pygame.transform.flip(self.image[1],True,False)
         self.b = False
      self.tool[self.wep].use(screen,self)

   def weponChange(self,keys):
      self.a -= 1
      if keys[pygame.K_e] and self.a < 0:
         self.wep += 1
         self.a = 100
      if self.wep == 2:
         self.wep = 0

   def draw(self,screen):
      img = self.image[self.image_index]
      if self.flip:
         img = pygame.transform.flip(img,False,True)
      screen.blit(img, self.x, self.y)
   
   def checkMove(self,movex,movey,place):
      print('----------------------------------')
      for y in range(-2, 3):
         for x in range(-2, 3):
            X   = x + self.x//50
            Y   = y + self.y//50
            key = place.genKeyC(X, Y)
            if key in place.map_dic:
               thing = place.map_dic[key]
               if thing.stuff == "tree":
                  print(' T', end='')
                  #if thing.isHit(self):
                  #   self.x -= movex
                  #   self.y -= movey
               else:
                  print(' _', end='')
         print()


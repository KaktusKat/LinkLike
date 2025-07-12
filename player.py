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
      self.inMaze = False

   def update(self,keys,screen,place,maze):
      a          = 0
      self.t    += 1
      Mpos       = pygame.mouse.get_pos()
      mousePress = pygame.mouse.get_pressed()
      if mousePress[0]:
         self.tool[self.wep].attack(self,screen)
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
         if self.inMaze:
            self.checkMoveM(0,-1.5,maze)
         else:
            self.checkMove(0,-1.5,place)
         a+=1
      if keys[pygame.K_s]:
         self.y += 1.5
         if self.inMaze:
           self.checkMoveM(0,1.5,maze)
         else:
           self.checkMove(0,1.5,place)
         a+=1
      if keys[pygame.K_d]:
         self.x += 1.5
         if self.inMaze:
            self.checkMoveM(1.5,0,maze)
         else:
            self.checkMove(1.5,0,place)
         a+=1
      if keys[pygame.K_a]:
         self.x -= 1.5
         if self.inMaze:
            self.checkMoveM(-1.5,0,maze)
         else:
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
      if self.wep == 3:
         self.wep = 0

   def draw(self,screen):
      img = self.image[self.image_index]
      if self.flip:
         img = pygame.transform.flip(img,False,True)
      screen.blit(img, self.x, self.y)

   def inPortal(self,place):
       mapX = self.x//58
       mapY = self.y//58
       key  = place.genKeyC(mapX,mapY)
       if key in place.map_dic:
          if place.map_dic[key].portal:
             self.x = 70
             self.y = 70
          if place.map_dic[key].portal or self.inMaze:
             self.inMaze = True
             return True
       return False
          

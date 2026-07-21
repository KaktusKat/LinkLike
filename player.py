import pygame
from sprite import sprite
import time
import math

class player(sprite):
   def __init__(self,img,posX,posY,w,h,tool,heath,sheild,spear):
      super().__init__(img,posX,posY,w,h)
      self.tool      = tool
      self.b         = False
      self.t         = -10
      self.wep       = 0
      self.a         = 0
      self.inMaze    = False
      self.health    = heath
      self.sheild    = sheild
      self.sheildC   = []
      self.table     = True
      self.spearGot  = True
      self.spear     = spear
      self.iFrames   = False
      self.hit       = False

   def update(self,keys,screen,place,maze,invetory,ballList,enemyList):
      if self.hit == True:
         self.hit         = False
         self.image_index = 2
         self.iFrames     = True
         self.draw(screen)
         return
      if self.iFrames == True:
         self.iFrames     = False
         self.image_index = 2
         time.sleep(0.1)
      else:
         self.image_index = 1
      if self.health <= 0:
         return
      if "spear" in invetory.craftList and self.spearGot:
         self.tool.append(self.spear)
         self.spearGot = False
      a          = 0
      self.t    += 1
      Mpos       = pygame.mouse.get_pos()
      mousePress = pygame.mouse.get_pressed()
      if mousePress[0] and not self.sheild.attacking:
         self.tool[self.wep].attack(self,screen)
      if mousePress[2] and self.inMaze:
         craft = maze.get_cell(int(((Mpos[0]+self.x)//70)-4),int(((Mpos[1]+self.y)//70)-4))
         if not invetory.window:
            if self.isHitXY(Mpos[0]+self.x-290,Mpos[1]+self.y-290,1,1,craft):
               if craft.craft:
                  self.table   = True
                  invetory.table = True
      if len(ballList) > 0:
         delList = []
         for ball in ballList:
             if ball.isHit(self):
                self.health -= 1
                delList.append(ball)
         for ball in delList:
             ballList.remove(ball)
      if len(self.sheildC) >= 1 and mousePress[2]:
         self.sheild.block(self,screen)
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
         self.velocityY -= 0.2
         a+=1
      if keys[pygame.K_s]:
         self.velocityY += 0.2
         a+=1
      if keys[pygame.K_d]:
         self.flipS  = False
         self.velocityX += 0.2
         a+=1
      if keys[pygame.K_a]:
         self.flipS = True
         self.velocityX -= 0.2
         a+=1
      if self.inMaze:
         self.checkMoveM(maze)
      if not self.inMaze:
         self.checkMove(place)
      if keys[pygame.K_r] and self.inMaze:
         self.inMaze = False
         self.x      = 0
         self.y      = 0
         a+=1
      if a > 0:
         self.move(1)
      if Mpos[0] < self.x and not self.b:
         self.image[0] = pygame.transform.flip(self.image[0],True,False)
         self.image[1] = pygame.transform.flip(self.image[1],True,False)
         self.b = True
      if Mpos[0] > self.x and self.b:         
         self.image[0] = pygame.transform.flip(self.image[0],True,False)
         self.image[1] = pygame.transform.flip(self.image[1],True,False)
         self.b = False
      self.tool[self.wep].use(screen,self)
      self.sheild.use(screen,self)
 
   def weponChange(self,keys):
      self.a -= 1
      if keys[pygame.K_e] and self.a < 0:
         self.wep += 1
         self.a = 100
      if self.wep == len(self.tool):
         self.wep = 0

   def inPortal(self,place):
       mapX = self.x//58
       mapY = self.y//58
       key  = place.genKeyC(mapX,mapY)
       if key in place.map_dic:
          if place.map_dic[key].portal:
             self.x = 70
             self.y = 70
          if place.map_dic[key].portal:
             self.inMaze = True
             return True
       if self.inMaze:
          return True
       return False


   def draw(self, screen):
      if self.image_index >= len(self.image):
         return
      img = self.image[self.image_index]
      if self.flipS:
         img = pygame.transform.flip(img,True,False)
      if self.flip:
         img = pygame.transform.flip(img,False,True)
      screen.blit(img, self.x, self.y)
          

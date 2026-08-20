import pickle
import pygame
from sprite import sprite
import time
import math

class player(sprite):
   def __init__(self,img,posX,posY,w,h,images,tool,heath,spear):
      super().__init__(img,posX,posY,w,h,images)
      self.tool       = tool
      self.b          = False
      self.t          = -10
      self.wep        = 0
      self.a          = 0
      self.inMaze     = False
      self.health     = heath
      self.table      = True
      self.iFrames    = 1
      self.iFrameTime = 40
      self.hit        = False
      self.animate    = 0
      self.animated   = False
      self.lastMove   = [0,0]
      self.roll       = 0
      self.rotated    = 0

   def update(self,keys,screen,place,maze,invetory,ballList,enemyList,weaponList):
      if invetory.table:
         return
      self.roll -= 1
      if self.iFrames >= 1:
         self.iFrames -= 1
      if self.hit == True:
         self.hit         = False
         self.image_index = 3
         self.iFrames     = self.iFrameTime
         return
      if self.iFrames == self.iFrameTime - 1:
         self.image_index = 2
         time.sleep(0.1)
         self.image_index = 1
      if self.health <= 0:
         return
      self.t    += 1
      Mpos       = pygame.mouse.get_pos()
      mousePress = pygame.mouse.get_pressed()
      if mousePress[2] and self.inMaze:
         craft = maze.get_cell(int(((Mpos[0]+self.x)//70)-4),int(((Mpos[1]+self.y)//70)-4))
         if not invetory.window:
            if self.isHitXY(Mpos[0]+self.x-290,Mpos[1]+self.y-290,1,1,craft):
               if craft.craft:
                  self.table   = True
                  invetory.table = True

      self.circleTiles = []
      for x in range(8):
         for y in range(8):
            X   = x-3 + self.x//58
            Y   = y-3 + self.y//58
            key = place.genKeyC(X, Y)
            tile = place.map_dic[key]
            ab   = ((tile.x-self.x)//58)**2+((tile.y-self.y)//58)**2
            if ab <= 3.5**2:
               self.circleTiles.append(tile)
              
              
      if len(ballList) > 0:
         delList = []
         for ball in ballList:
             if ball.isHit(self):
                self.health -= 1
                delList.append(ball)
         for ball in delList:
             ballList.remove(ball)
      if keys[pygame.K_SPACE] and self.t > 0:
         totalDistance  = abs(self.lastMove[0])+abs(self.lastMove[1])
         if totalDistance == 2:
            self.lastMove[0] = math.sqrt(self.lastMove[0]**2+self.lastMove[1]**2)/2*(self.lastMove[0]/abs(self.lastMove[0]))
            self.lastMove[1] = math.sqrt(self.lastMove[0]**2+self.lastMove[1]**2)/2*(self.lastMove[1]/abs(self.lastMove[1]))
         self.velocityX += self.lastMove[0]*12
         self.velocityY += self.lastMove[1]*12
         self.iFrames     = 40
         self.roll        = 40
         self.image_index = 5
         self.t           = -60
         return
      if self.roll > 0:
         return
      self.lastMove = [0,0]
      if keys[pygame.K_w]:
         self.velocityY -= 0.2
         self.lastMove[1] = -1
         if not self.animated:
            self.animate += 1
            self.animated = True
      if keys[pygame.K_s]:
         self.velocityY += 0.2
         self.lastMove[1] = 1
         if not self.animated:
            self.animate += 1
            self.animated = True
      if keys[pygame.K_d]:
         self.flipS  = False
         self.velocityX += 0.2
         self.lastMove[0] = 1
         if not self.animated:
            self.animate += 1
            self.animated = True
      if keys[pygame.K_a]:
         self.flipS = True
         self.velocityX -= 0.2
         self.lastMove[0] = -1
         if not self.animated:
            self.animate += 1
            self.animated = True
      self.animated = False
      if self.inMaze:
         self.checkMoveM(maze,screen)
      if not self.inMaze:
         self.checkMove(place,screen)
      if keys[pygame.K_r] and self.inMaze:
         self.inMaze = False
         self.x      = 0
         self.y      = 0
      if self.animate > 0:
         self.move(1,3)
         self.animate = -10
#      if Mpos[0] < self.x and not self.b:
 #        self.image[0] = pygame.transform.flip(self.image[0],True,False)
  #       self.image[1] = pygame.transform.flip(self.image[1],True,False)
   #      self.b = True
    #  if Mpos[0] > self.x and self.b:         
     #    self.image[0] = pygame.transform.flip(self.image[0],True,False)
      #   self.image[1] = pygame.transform.flip(self.image[1],True,False)
       #  self.b = False
      weaponList[self.tool[self.wep]].attack(screen,self)
      if self.iFrames > 0:
         self.image_index = 4
 
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
      img = screen.images[self.image[self.image_index]]
      if self.roll > 0:
         self.rotated += 10
         img = screen.images[self.image[5]]
         img = pygame.transform.rotate(img,self.rotated)
      if self.flipS:
         img = pygame.transform.flip(img,True,False)
      if self.flip:
         img = pygame.transform.flip(img,False,True)
      screen.blit(img, self.x, self.y)

   def LOST(self,radius,target,place,maze = False):
      distanceX     = self.x - target.x
      distanceY     = self.y - target.y
      totalDistance = distanceX + distanceY

      if distanceX >= radius or distanceY >= radius:
         return False

      travelX = (20/totalDistance)*distanceX
      travelX = (20/totalDistance)*distanceY
      posX    = self.x
      posY    = self.y

      for i in range(math.ceil(totalDistance/20)):
         posX += travelX
         posY += travelY

         if maze:
            for oy in range(-2, 3):
               for ox in range(-2, 3):
                  X   = ox + posX//29
                  Y   = oy + posY//29
                  X = int(X)
                  Y = int(Y)
                  thing = place.get_cell(X, Y)

                  if thing.isHitXY(posX,posY,self.w,self.h):
                     if thing.soild:
                        return False
                     else:
                        thing.LOS = True
         else:
            for y in range(-2, 3):
               for x in range(-2, 3):
                  X   = x + posX//58
                  Y   = y + posY//58
                  key = place.genKeyC(X, Y)

                  if thing.isHitXY(posX,posY,self.w,self.h):
                     if thing.soild:
                        return False
                     else:
                        thing.LOS = True
      return True


          

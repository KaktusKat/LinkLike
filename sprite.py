import pygame
import math
from Vector import Vector

class sprite:
   def __init__(self, img, posX, posY, w, h,images, count = 1, soild = False):
      self.x      = posX
      self.y      = posY
      self.image  = []
      for i in range(len(img)):
         self.image.append("images/"+img[i])
         image = pygame.image.load("images/"+img[i])
         images[self.image[i]] = pygame.transform.scale(image,(w,h))
      self.h           = h
      self.w           = w
      self.flip        = False
      self.flipS       = False
      self.num         = count
      self.image_index = 0
      self.soild       = soild
      self.velocityX   = 0
      self.velocityY   = 0
      self.circleTiles = []

   def move(self,offsetb = 0,offseta = 0):
      self.image_index += 1
      if self.image_index >= len(self.image)-offseta:
          self.image_index = 0+offsetb

   def draw(self, screen):
      img = screen.images[self.image[self.image_index]]
      if self.flipS:
         img = pygame.transform.flip(img,True,False)
      if self.flip:
         img = pygame.transform.flip(img,False,True)
      screen.blit(img, self.x, self.y)


   def isHitSide_(self, other, direct):

       self_pos   = Vector((self.x, self.y))
       self_size  = Vector((self.w, self.h))
       self_vel   = Vector((self.velocityX, self.velocityY))
       other_pos  = Vector((other.x, other.y))
       other_size = Vector((other.w, other.h))
       other_vel  = Vector((other.velocityX, other.velocityY))

       self_bl  = self_pos + self_vel * direct
       self_tr  = self_bl  + self_size
       other_bl = other_pos + other_vel * direct
       other_tr = other_bl  + other_size

       return (other_bl.x < self_tr.x) and (other_tr.x > self_bl.x) and \
              (other_bl.y < self_tr.y) and (other_tr.y > self_bl.y)

   def isHitSide2(self, other):

       self_pos   = Vector((self.x, self.y))
       self_size  = Vector((self.w, self.h))
       other_pos  = Vector((other.x, other.y))
       other_size = Vector((other.w, other.h))

       self_bl  = self_pos
       self_tr  = self_bl  + self_size
       other_bl = other_pos
       other_tr = other_bl  + other_size

       if (other_bl.x < self_tr.x) and (other_tr.x > self_bl.x) and \
          (other_bl.y < self_tr.y) and (other_tr.y > self_bl.y):
          return "BAD"

       self_bl  = self_pos + Vector((self.velocityX, 0))
       self_tr  = self_bl  + self_size
       other_bl = other_pos + Vector((other.velocityX, 0))
       other_tr = other_bl  + other_size

       if (other_bl.x < self_tr.x) and (other_tr.x > self_bl.x) and \
          (other_bl.y < self_tr.y) and (other_tr.y > self_bl.y):
          return "x"

       self_bl  = self_pos + Vector((0, self.velocityY))
       self_tr  = self_bl  + self_size
       other_bl = other_pos + Vector((0, other.velocityY))
       other_tr = other_bl  + other_size

       if (other_bl.x < self_tr.x) and (other_tr.x > self_bl.x) and \
          (other_bl.y < self_tr.y) and (other_tr.y > self_bl.y):
          return "y"

       return None


   def isHitSide(self,other,screen,rect = False):

      moveList = [ [ [0, 0],
                     [self.velocityY, other.velocityY]
                     ,"y"],

                     [ [self.velocityX, other.velocityX],
                     [0,0],
                     "x"]
                   ]

      offsetX = (screen.images[other.image[0]].get_width()-other.w)/2
      offsetY = (screen.images[other.image[0]].get_height()-other.h)/2

      rectX,rectY   = screen.convertWTS(other.x +offsetX,other.y+offsetY)
      
      if rect:
         pygame.draw.rect(screen.screen,(250,0,0),pygame.Rect(rectX,rectY,other.w,other.h),2)
 
      for move in moveList:

         playerX = self.x + move[0][0]
         playerY = self.y + move[1][0]
         top_x   = playerX + self.w
         top_y   = playerY + self.h

         otherX      = other.x + move[0][1]+offsetX
         otherY      = other.y + move[1][1]+offsetY
         other_top_x = otherX + other.w
         other_top_y = otherY + other.h


         if (otherX < top_x) and (other_top_x > playerX) and \
            (otherY < top_y) and (other_top_y > playerY):
            return move[2]
               
   
   def isHitXY(self,playerX,playerY,playerW,playerH, other,screen = 0,offsetX = 0,offsetY = 0):


      playerX += offsetX
      playerY += offsetY
      if not screen == 0:
         x,y = screen.convertWTS(playerX,playerY)
         pygame.draw.rect(screen.screen,(250,0,0),pygame.Rect(x,y,playerW,playerH),2)
      top_x    = playerX + playerW
      top_y    = playerY + playerH

      other_top_x = other.x + other.w
      other_top_y = other.y + other.h

      return (other.x < top_x) and (other_top_x > playerX) and \
             (other.y < top_y) and (other_top_y > playerY)
   
   def isHitXYXY(self,playerX,playerY,playerW,playerH, otherX,otherY,otherW,otherH):

      top_x = playerX + playerW
      top_y = playerY + playerH

      other_top_x = otherX + otherW
      other_top_y = otherY + otherH

      return (otherX < top_x) and (other_top_x > playerX) and \
             (otherY < top_y) and (other_top_y > playerY)

   def isHit(self, other):

      if self == other:
         return False

      top_x = self.x + self.w
      top_y = self.y + self.h

      other_top_x = other.x + other.w
      other_top_y = other.y + other.h


      return (other.x < top_x) and (other_top_x > self.x) and \
             (other.y < top_y) and (other_top_y > self.y)

   def isHitC(self, Ox,Oy,Ow,Oh):
      top_x = self.x + self.w
      top_y = self.y + self.h

      other_top_x = Ox + Ow
      other_top_y = Oy + Oh

      return (Ox < top_x) and (other_top_x > self.x) and \
             (Oy < top_y) and (other_top_y > self.y)

   def checkMove(self,place,screen):
      for y in range(-2, 3):
         for x in range(-2, 3):
            X   = x + self.x//58
            Y   = y + self.y//58
            key = place.genKeyC(X, Y)

            if key in place.map_dic:
               thing = place.map_dic[key]
               if thing.soild:
                  side = self.isHitSide(thing,screen)
                  if side == "x":
                     self.velocityX = -self.velocityX
                     return
                  if side == "y":
                     self.velocityY = -self.velocityY
                     return
   
   def checkMoveTF(self,place,screen):
      for y in range(-2, 3):
         for x in range(-2, 3):
            X   = x + self.x//58
            Y   = y + self.y//58
            key = place.genKeyC(X, Y)

            if key in place.map_dic:
               thing = place.map_dic[key]
               if thing.soild:
                  side = self.isHitSide(thing,screen)
                  if side == "x":
                     self.velocityX = -self.velocityX
                     return True
                  if side == "y":
                     self.velocityY = -self.velocityY
                     return True
      return False
   
   def checkMoveM(self,maze,screen):
    #  self.velocityX *= 0.95
     # self.velocityY *= 0.95
      for oy in range(-2, 3):
         for ox in range(-2, 3):
            X   = ox + self.x//29
            Y   = oy + self.y//29
            X = int(X)
            Y = int(Y)
            thing = maze.get_cell(X, Y)
            if thing and thing.soild:
               side = self.isHitSide(thing,screen)
               if side == "x":
                  self.velocityX = -self.velocityX
                  return
               if side == "y":
                  self.velocityY = -self.velocityY
                  return

   def checkMoveE(self,enemyList,screen):
      for i in range(len(enemyList)):

         selfVelocityX = self.velocityX
         selfVelocityY = self.velocityY

         side = self.isHitSide(enemyList[i],screen)
         if side == "x":
            self.velocityX         = enemyList[i].velocityX
            enemyList[i].velocityX = selfVelocityX
            return
         if side == "y":
            self.velocityY         = enemyList[i].velocityY
            enemyList[i].velocityY = selfVelocityY
            return

   def LOS(self,radius,target,place,screen = 0,maze = False):
      distanceX     = self.x - target.x
      distanceY     = self.y - target.y
      totalDistance = distanceX + distanceY

      if abs(distanceX) >= radius*58 or abs(distanceY) >= radius*58:
         return False
      if totalDistance == 0:
         return True

      travelX = (20/totalDistance)*distanceX
      travelY = (20/totalDistance)*distanceY
      posX    = self.x
      posY    = self.y

      for i in range(math.ceil(totalDistance/20)):
         posX -= travelX
         posY -= travelY

         if maze:
            for oy in range(-2, 3):
               for ox in range(-2, 3):
                  X   = ox + posX//29
                  Y   = oy + posY//29
                  X = int(X)
                  Y = int(Y)
                  thing = maze.get_cell(X, Y)

                  if thing.isHitXY(posX,posY,self.w,self.h,thing) and thing.soild:
                     return False
         else:
            for y in range(-2, 3):
               for x in range(-2, 3):
                  X   = x + posX//58
                  Y   = y + posY//58
                  key = place.genKeyC(X, Y)
                  if not key in place.map_dic:
                     return False
                  thing = place.map_dic[key]

                  if thing.isHitXY(posX,posY,self.w,self.h,thing,screen) and thing.soild:
                     return False
      return True

   def circle(self,radius,screen,place,player):
      self.circleTiles = []
      for x in range(int(2*radius+1)):
         for y in range(int(2*radius+1)):
            X   = x-int(radius) + self.x//58
            Y   = y-int(radius) + self.y//58
            key = place.genKeyC(X, Y)
            if not key in place.map_dic:
               return
            tile = place.map_dic[key]
            ab   = ((tile.x-self.x)//58)**2+((tile.y-self.y)//58)**2
            if ab <= radius**2:
               self.circleTiles.append(tile)
#               pygame.draw.rect(screen.screen,(0,250,0),pygame.Rect(tile.x+290-player.x,tile.y-player.y+290,40,40),2)



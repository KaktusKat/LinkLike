import pygame
from Vector import Vector

class sprite:
   def __init__(self, img, posX, posY, w, h, count = 1, soild = False):
      self.x      = posX
      self.y      = posY
      self.image  = []
      for i in range(len(img)):
         image = pygame.image.load("images/"+img[i])
         self.image.append(pygame.transform.scale(image,(w,h)))
      self.h           = h
      self.w           = w
      self.flip        = False
      self.flipS       = False
      self.num         = count
      self.image_index = 0
      self.soild       = soild
      self.velocityX   = 0
      self.velocityY   = 0

   def move(self,offset = 0):
      self.image_index += 1
      if self.image_index == len(self.image)-offset:
          self.image_index = 0

   def draw(self, screen):
      img = self.image[self.image_index]
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


   def isHitSide(self,other):

      moveList = [ [ [0, 0],
                     [self.velocityY, other.velocityY]
                     ,"y"],

                     [ [self.velocityX, other.velocityX],
                     [0,0],
                     "x"]
                   ]

      for move in moveList:

         playerX = self.x + move[0][0]
         playerY = self.y + move[1][0]
         top_x   = playerX + self.w
         top_y   = playerY + self.h

         otherX      = other.x + move[0][1]
         otherY      = other.y + move[1][1]
         other_top_x = otherX + other.w
         other_top_y = otherY + other.h


         if (otherX < top_x) and (other_top_x > playerX) and \
            (otherY < top_y) and (other_top_y > playerY):
            return move[2]
               
   
   def isHitXY(self,playerX,playerY,playerW,playerH, other):

      if self == other:
         return False

      top_x = playerX + playerW
      top_y = playerY + playerH

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

   def checkMove(self,place):
      self.velocityX *= 0.95
      self.velocityY *= 0.95

      for y in range(-2, 3):
         for x in range(-2, 3):
            X   = x + self.x//58
            Y   = y + self.y//58
            key = place.genKeyC(X, Y)

            if key in place.map_dic:
               thing = place.map_dic[key]
               if thing.soild:
                  side = self.isHitSide(thing)
                  if side == "x":
                     self.velocityX = -self.velocityX
                     return
                  if side == "y":
                     self.velocityY = -self.velocityY
                     return
   
   def checkMoveTF(self,place):
      self.velocityX *= 0.95
      self.velocityY *= 0.95

      for y in range(-2, 3):
         for x in range(-2, 3):
            X   = x + self.x//58
            Y   = y + self.y//58
            key = place.genKeyC(X, Y)

            if key in place.map_dic:
               thing = place.map_dic[key]
               if thing.soild:
                  side = self.isHitSide(thing)
                  if side == "x":
                     self.velocityX = -self.velocityX
                     return True
                  if side == "y":
                     self.velocityY = -self.velocityY
                     return True
      return False
   
   def checkMoveM(self,maze):
      self.velocityX *= 0.95
      self.velocityY *= 0.95
      for oy in range(-2, 3):
         for ox in range(-2, 3):
            X   = ox + self.x//29
            Y   = oy + self.y//29
            X = int(X)
            Y = int(Y)
            thing = maze.get_cell(X, Y)
            if thing and thing.soild:
               side = self.isHitSide(thing)
               if side == "x":
                  self.velocityX = -self.velocityX
                  return
               if side == "y":
                  self.velocityY = -self.velocityY
                  return

   def checkMoveE(self,enemyList):
      for i in range(len(enemyList)):

         selfVelocityX = self.velocityX
         selfVelocityY = self.velocityY

         side = self.isHitSide(enemyList[i])
         if side == "x":
            self.velocityX         = enemyList[i].velocityX
            enemyList[i].velocityX = selfVelocityX
            return
         if side == "y":
            self.velocityY         = enemyList[i].velocityY
            enemyList[i].velocityY = selfVelocityY
            return


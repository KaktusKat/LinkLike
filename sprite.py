import pygame

class sprite:
   def __init__(self, img, posX, posY, w, h, count = 1, soild = False):
      self.x      = posX
      self.y      = posY
      self.image  = []
      for i in range(len(img)):
         image = pygame.image.load(img[i])
         self.image.append(pygame.transform.scale(image,(w,h)))
      self.h           = h
      self.w           = w
      self.flip        = False
      self.num         = count
      self.image_index = 0
      self.soild       = soild
      self.velocityX   = 0
      self.velocityY   = 0

   def move(self):
      self.image_index += 1
      if self.image_index == len(self.image):
          self.image_index = 0

   def draw(self, screen):
      img = self.image[self.image_index]
      if self.flip:
         img = pygame.transform.flip(img,False,True)
      screen.blit(img, self.x, self.y)

   def isHitXYSide(self,playerX,playerY,playerW,playerH,other,moveList):

      for move in moveList:

         if self == other:
            return False

         playerX = playerX + move[0]
         playerY = playerY + move[1]
         top_x   = playerX + playerW
         top_y   = playerY + playerH

         other_top_x = other.x + other.w
         other_top_y = other.y + other.h

         if (other.x < top_x) and (other_top_x > playerX) and \
            (other.y < top_y) and (other_top_y > playerY):
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

   def checkMove(self,movex,movey,place):
      self.velocityX *= 0.95
      self.velocityY *= 0.95

      for y in range(-2, 3):
         for x in range(-2, 3):
            X   = x + self.x//58
            Y   = y + self.y//58
            key = place.genKeyC(X, Y)

            newX     = self.x + movex
            newY     = self.x + movey
            moveList = [[0,movey,"y"],[movex,0,"x"]]

            if key in place.map_dic:
               thing = place.map_dic[key]
               if thing.soild:
                  side = self.isHitXYSide(self.x,self.y,self.w,self.h,thing,moveList)
                  if side == "x":
                     self.velocityX = -self.velocityX
                     return
                  if side == "y":
                     self.velocityY = -self.velocityY
                     return
   
   def checkMoveTF(self,movex,movey,place):
      self.velocityX *= 0.95
      self.velocityY *= 0.95

      for y in range(-2, 3):
         for x in range(-2, 3):
            X   = x + self.x//58
            Y   = y + self.y//58
            key = place.genKeyC(X, Y)

            newX     = self.x + movex
            newY     = self.x + movey
            moveList = [[0,movex,"y"],[movey,0,"x"]]

            if key in place.map_dic:
               thing = place.map_dic[key]
               if thing.soild:
                  side = self.isHitXYSide(self.x,self.y,self.w,self.h,thing,moveList)
                  if side == "x":
                     self.velocityX = -self.velocityX
                  if side == "y":
                     self.velocityY = -self.velocityY
                  if self.isHitXY(newX,newY,self.x,self.y,thing):
                     return True
      return False
   
   def checkMoveM(self,movex,movey,maze):
      self.velocityX *= 0.95
      self.velocityY *= 0.95
      for oy in range(-2, 3):
         for ox in range(-2, 3):
            X   = ox + self.x//29
            Y   = oy + self.y//29
            X = int(X)
            Y = int(Y)
            thing = maze.get_cell(X, Y)
            moveList = [[0,self.velocityX,"y"],[self.velocityY,0,"x"],[self.velocityX,self.velocityY,"both"]]
            if thing and thing.soild:
               side = self.isHitXYSide(self.x,self.y,self.w,self.h,thing,moveList)
               if side == "x":
                  self.velocityX = -self.velocityX
               if side == "y":
                  self.velocityY = -self.velocityY


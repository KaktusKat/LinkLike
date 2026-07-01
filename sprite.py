import pygame

class sprite:
   def __init__(self, img, posX, posY, w, h, count = 1, soild = False):
      self.x      = posX
      self.y      = posY
      self.image  = []
      for i in range(len(img)):
         image = pygame.image.load(img[i])
         self.image.append(pygame.transform.scale(image,(w,h)))
      self.h      = h
      self.w      = w
      self.flip   = False
      self.num    = count
      self.image_index = 0
      self.soild  = soild

   def move(self):
      self.image_index += 1
      if self.image_index == len(self.image):
          self.image_index = 0

   def draw(self, screen):
      img = self.image[self.image_index]
      if self.flip:
         img = pygame.transform.flip(img,False,True)
      screen.blit(img, self.x, self.y)

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
      for y in range(-2, 3):
         for x in range(-2, 3):
            X   = x + self.x//50
            Y   = y + self.y//50
            key = place.genKeyC(X, Y)
            if key in place.map_dic:
               thing = place.map_dic[key]
               if thing.soild:
                  if thing.isHit(self):
                     self.x -= movex
                     self.y -= movey
   
   def checkMoveTF(self,movex,movey,place):
      for y in range(-2, 3):
         for x in range(-2, 3):
            X   = x + self.x//50
            Y   = y + self.y//50
            key = place.genKeyC(X, Y)
            if key in place.map_dic:
               thing = place.map_dic[key]
               if thing.soild:
                  if thing.isHit(self):
                     self.x -= movex
                     self.y -= movey
                     return True
      return False
   
   def checkMoveM(self,movex,movey,maze):
      for oy in range(-2, 3):
         for ox in range(-2, 3):
            X   = ox + self.x//29
            Y   = oy + self.y//29
            X = int(X)
            Y = int(Y)
            thing = maze.get_cell(X, Y)
            if thing and thing.soild:
               print("hi")
               if thing.isHit(self):
                  self.x -= movex
                  self.y -= movey


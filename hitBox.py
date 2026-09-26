import pygame
import math

class hitBox:
   def __init__(self,sprite,hitBoxList):
      self.hitBoxList = hitBoxList
      self.sprite     = sprite

   def isHitSide(self,other,screen,rect = False):

      moveList = [ [ [0, 0],
                     [self.sprite.velocityY, other.sprite.velocityY]
                     ,"y"],

                     [ [self.sprite.velocityX, other.sprite.velocityX],
                     [0,0],
                     "x"]
                   ]


      for move in moveList:

         for hitBox in self.hitBoxList:
            for hitBoxO in other.hitBoxList:
             
               playerX = self.sprite.x + move[0][0] + hitBox[0]
               playerY = self.sprite.y + move[1][0] + hitBox[1]

               otherX  = other.sprite.x + move[0][1] + hitBoxO[0]
               otherY  = other.sprite.y + move[1][1] + hitBoxO[1]

               if rect:
                  x,y = screen.convertWTS(otherX,otherY)
                  pygame.draw.rect(screen.screen,(0,0,255),pygame.Rect(x,y,hitBoxO[2],hitBoxO[3]),2)
         
               if self.isHitXYXY(playerX,playerY,hitBox[2],hitBox[3],otherX,otherY,hitBoxO[2],hitBoxO[3]):
                  return move[2]

   def isHitXY(self,playerX,playerY,playerW,playerH,screen = 0,offsetX = 0,offsetY = 0):


      playerX += offsetX
      playerY += offsetY

      for hitBox in self.hitBoxList:
         if not screen == 0:
            x,y = screen.convertWTS(playerX,playerY)
            pygame.draw.rect(screen.screen,(250,0,0),pygame.Rect(x,y,playerW,playerH),2)
         x = self.sprite.x + hitBox[0]
         y = self.sprite.y + hitBox[1]
            
         if self.isHitXYXY(x,y,hitBox[2],hitBox[3],playerX,playerY,playerW,playerH):
            return True

      return False



   def isHitXYXY(self,playerX,playerY,playerW,playerH, otherX,otherY,otherW,otherH):

      top_x = playerX + playerW
      top_y = playerY + playerH

      other_top_x = otherX + otherW
      other_top_y = otherY + otherH

      return(otherX < top_x) and (other_top_x > playerX) and \
            (otherY < top_y) and (other_top_y > playerY)

   def isHit(self, other):

      if self == other:
         return False
      
      for hitBox in self.hitBoxList:
         for hitBoxO in other.hitBoxList:
            x = self.sprite.x + hitBox[0]
            y = self.sprite.y + hitBox[1]
            
            xO = other.sprite.x + hitBoxO[0]
            yO = other.sprite.y + hitBoxO[1]
            
            if self.isHitXYXY(x,y,hitBox[2],hitBox[3],xO,yO,hitBox[2],hitBox[3]):
              return True

      return False

   def checkMove(self,place,screen):
      for y in range(-2, 3):
         for x in range(-2, 3):
            X   = x + self.sprite.x//58
            Y   = y + self.sprite.y//58
            key = place.genKeyC(X, Y)

            if key in place.map_dic:
               thing = place.map_dic2[key]
               if thing.soild:
                  side = self.isHitSide(thing.hitBox,screen)
                  if side == "x":
                     self.sprite.velocityX = -self.sprite.velocityX*thing.bounce
                     return
                  if side == "y":
                     self.sprite.velocityY = -self.sprite.velocityY*thing.bounce
                     return

   def checkMoveTF(self,place,screen):
      for y in range(-2, 3):
         for x in range(-2, 3):
            X   = x + self.sprite.x//58
            Y   = y + self.sprite.y//58
            key = place.genKeyC(X, Y)

            if key in place.map_dic:
               thing = place.map_dic2[key]
               if thing.soild:
                  side = self.isHitSide(thing.hitBox,screen)
                  if side == "x":
                     self.sprite.velocityX = -self.sprite.velocityX*thing.bounce
                     return True
                  if side == "y":
                     self.sprite.velocityY = -self.sprite.velocityY*thing.bounce
                     return True
      return False

   def checkMoveM(self,maze,screen):
    #  self.velocityX *= 0.95
     # self.velocityY *= 0.95
      for oy in range(-2, 3):
         for ox in range(-2, 3):
            X   = ox + self.sprite.x//29
            Y   = oy + self.sprite.y//29
            X = int(X)
            Y = int(Y)
            thing = maze.get_cell(X, Y)
            if thing and thing.soild:
               side = self.isHitSide(thing.hitBox,screen)
               if side == "x":
                  self.sprite.velocityX = -self.sprite.velocityX*thing.bounce
                  return
               if side == "y":
                  self.sprite.velocityY = -self.sprite.velocityY*thing.bounce
                  return

   def checkMoveE(self,enemyList,screen):
      for i in range(len(enemyList)):

         selfVelocityX = self.sprite.velocityX
         selfVelocityY = self.sprite.velocityY

         side = self.isHitSide(enemyList[i].hitBox,screen)
         if side == "x":
            self.sprite.velocityX  = enemyList[i].velocityX
            enemyList[i].velocityX = selfVelocityX
            return
         if side == "y":
            self.sprite.velocityY  = enemyList[i].velocityY
            enemyList[i].velocityY = selfVelocityY
            return

   def LOS(self,radius,target,place,screen = 0,maze = False):
      return self.LOSWH(radius,target.hitBox,place,self.sprite.w,self.sprite.h,screen,maze)

   def LOSWH(self,radius,target,place,w,h,screen = 0,maze = False):
      distanceX      = self.sprite.x - target.sprite.x
      distanceY      = self.sprite.y - target.sprite.y
      totalDistance  = abs(distanceX) + abs(distanceY)
      totalDistanceC = abs(distanceX)**2 + abs(distanceY)**2

      if totalDistanceC >= (radius*58)**2:
         return False
      if totalDistance == 0:
         return True

      travelX = (20/totalDistance)*distanceX
      travelY = (20/totalDistance)*distanceY
      posX    = self.sprite.x
      posY    = self.sprite.y

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

                  if thing.hitBox.isHitXY(posX,posY,w,h,screen) and thing.soild:
                     return False
         else:
            for y in range(-2, 3):
               for x in range(-2, 3):
                  X   = x + posX//58
                  Y   = y + posY//58
                  key = place.genKeyC(X, Y)
                  if not key in place.map_dic2:
                     return False
                  thing = place.map_dic2[key]

                  if thing.hitBox.isHitXY(posX,posY,w,h,screen) and thing.soild and not thing.hitBox == target:
                     return False
      return True


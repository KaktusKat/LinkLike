from enemy import enemy
from ball  import ball
import random
import math
import pygame

class corruptedEnemy(enemy):
   def __init__(self,image,x,y,w,h,ha,big = False):
      super().__init__(image,x,y,w,h,ha,big)
      self.corruption = 2
      self.a          = -10
      self.lastmove   = [0,0]
      self.Kback      = 0
      self.attack     = 0
      self.Acooldown  = 0
      self.wait       = 0
      self.sign       = False
      self.attacking  = False
      self.timer      = 0


   def update(self,player,screen,place,ballList):
      if len(ballList) > 0:
         delList = []
         for balls in ballList:
             if balls.isHit(self) and balls.reflected:
                self.ha -= 1
                delList.append(balls)
         for balls in delList:
             ballList.remove(balls)
      if player.wep == 3 and player.tool[player.wep].attacking:        # check if it is a spear
         Xmove = 0
         Ymove = 0
         tool  = player.tool[player.wep]
         if ((-tool.angle)*180/math.pi < 90 and (-tool.angle)*180/math.pi > 0) or ((-tool.angle)*180/math.pi > -90 and (-tool.angle)*180/math.pi < 0):
            Xmove += tool.Rwepon.get_width()/2
         if (-tool.angle)*180/math.pi < 0:
            Ymove += tool.Rwepon.get_height()/2
         player.tool[player.wep].x = (tool.dX-tool.Rwepon.get_width()/2)+Xmove
         player.tool[player.wep].y = (tool.dY-tool.Rwepon.get_height()/2)+Ymove
         player.tool[player.wep].w = 75
         player.tool[player.wep].h = 75

      hit = False
      if self.ha <= 0:
         return

      if (self.isHit(player.tool[player.wep]) and player.tool[player.wep].attacking) or (self.a < 0 and self.a > -10):
         x = self.x
         y = self.y
         self.x = self.x+player.tool[player.wep].kback*math.cos(player.tool[player.wep].angle)
         self.y = self.y+player.tool[player.wep].kback*math.sin(player.tool[player.wep].angle)
         self.checkMove(0,self.y-y,place)
         self.checkMove(self.x-x,0,place)
         self.a += 1

      if self.a == 0:
         self.a = -10
#         if self.corruption > 0:
 #           self.corruption -= 1
  #          img           = pygame.image.load("halfCorruptedBlob.png")
   #         img           = pygame.transform.scale(img,(w,h))
    #        self.image[0] = img
     #    else: 
      #      self.ha -= 1

      if self.x < player.x:
         if abs(self.x-player.x) <= 150:
            self.x -= 1
            self.lastmove[0] = -1
            if self.checkMoveTF(-1,0,place):
               self.image_index = 1
               self.x          -= 1
         else:
            self.x += 1
            self.lastmove[0] = 1
            if self.checkMoveTF(1,0,place):
               self.image_index = 1
               self.x          +=1
      else:
         if abs(self.x-player.x) <= 150:
            self.x += 1
            self.lastmove[0] = 1
            if self.checkMoveTF(1,0,place):
               self.image_index = 1
               self.x          +=1
         else:
            self.x -= 1
            self.lastmove[0] = -1
            if self.checkMoveTF(1,0,place):
               self.image_index = 1
               self.x          -=1

      if self.y < player.y:
         if abs(self.y-player.y) <= 150:
            self.y -= 1
            self.lastmove[1] = -1
            if self.checkMoveTF(0,-1,place):
               self.image_index = 1
               self.y          -= 1
         else:
            self.y += 1
            self.lastmove[1] = 1
            if self.checkMoveTF(0,-1,place):
               self.image_index = 1
               self.y          += 1
      else:
         if abs(self.y-player.y) <= 150:
            self.y += 1
            self.lastmove[1] = 1
            if self.checkMoveTF(0,-1,place):
               self.image_index = 1
               self.y          += 1
         else:
            self.y -= 1
            self.lastmove[1] = -1
            if self.checkMoveTF(0,-1,place):
               self.image_index = 1
               self.y          -= 1

      if random.randint(0,200) == 1 and self.image_index == 0:
         ballList.append(ball(["corruptBall.png"],self.x,self.y,30,30,1,self))

      self.draw(screen)
      self.image_index = 0



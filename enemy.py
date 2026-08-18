from sprite import sprite
import math
import pygame
import time

class enemy(sprite):
   def __init__(self,image,x,y,w,h,images,ha,big = False):
      super().__init__(image,x,y,w,h,images)
      self.a         = -10
      self.ha        = ha
      self.big       = big
      self.lastmove  = [0,0]
      self.Kback     = 0
      self.attack    = 0
      self.Acooldown = 0
      self.wait      = 0
      self.sign      = False  
      self.attacking = False
      self.timer     = 0
      self.iframes   = False
      self.iFrames   = False
 
   def update(self,player,move,enemy_list,keys,place,screen,weaponList):
      self.image_index = 0
      if self.ha <= 0:
         enemy_list.remove(self)
         return

      if self.a == 0:
         self.a = -10
         self.ha -= 1

      if weaponList[player.tool[player.wep]].attacking == False:
         self.iframes = False

      if self.isHitXY(self.x+self.velocityX,self.y+self.velocityY,self.w,self.h,player) and self.attacking and not player.iFrames:
         player.health     -= 1
         player.hit         = True
         player.image_index = 1
         self.attack        = 0
         self.attacking     = False

      else:
         self.lastmove = [0,0]

      if self.Kback == 0:
         self.lastmove = [0,0]

      if self.a < 0 and self.a > -10:
         pass

      if self.x < player.x:
         self.velocityX  += 0.1
         self.lastmove[0] = 1 
      else:
         self.velocityX -= 0.1
         self.lastmove[0] = -1

      if self.y < player.y:
         self.velocityY += 0.1
         self.lastmove[1] = 1
      else:
         self.velocityY -= 0.1
         self.lastmove[1] = -1

      

      if (abs(self.x - player.x) <= 100 or abs(self.y - player.y) <= 100) and self.Acooldown < 0:
         self.attack = 10
         self.image_index = 1
         if not self.sign:
            self.wait = 70
            self.sign = True

      if self.attack > 0 and self.wait < 0:
         self.attacking   = True
         self.velocityX  += self.lastmove[0]*3
         self.velocityY  += self.lastmove[1]*3
         self.attack     -= 1
         self.Acooldown   = 200
         self.image_index = 0
         self.sign = False
      else:
         self.attacking = False

      if (self.isHit(weaponList[player.tool[player.wep]]) and weaponList[player.tool[player.wep]].attacking) and not self.iframes:
         x    = self.x
         y    = self.y
         tool = weaponList[player.tool[player.wep]]
         self.velocityX  += tool.kback*math.cos(tool.frameList[tool.frameIndex].angle)
         self.velocityY  += tool.kback*math.sin(tool.frameList[tool.frameIndex].angle)
         self.a          += 1
         self.image_index = 2
         self.iFrames     = True
         self.iframes     = True
         self.ha         -= weaponList[player.tool[player.wep]].damage
      
      self.checkMove(place,screen)
      self.Acooldown -= 1
      self.wait -= 1 
      self.timer -= 1

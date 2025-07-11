from sprite import sprite
import math
import pygame

class enemy(sprite):
   def __init__(self,image,x,y,w,h,ha,big = False):
      super().__init__(image,x,y,w,h)
      self.a   = -10
      self.ha  = ha
      self.big = big

   def update(self,player,move,enemy_list,keys,place):
      if self.ha == 0:
         enemy_list.remove(self)
         return
      if self.isHit(player.tool[player.wep]) or (self.a < 0 and self.a > -10) and player.tool[player.wep].attacking:
         x = self.x
         y = self.y
         self.x = self.x+player.tool[player.wep].kback*math.cos(player.tool[player.wep].angle)
         self.y = self.y+player.tool[player.wep].kback*math.sin(player.tool[player.wep].angle)
         self.checkMove(0,self.y-y,place)
         self.checkMove(self.x-x,0,place)
         self.a += 1
      if self.a == 0:
         self.a = -10
         self.ha -= 1
      self.x += 1
      self.y += 1
      if self.isHit(player):
         self.x -= 1
         self.y -= 1
         return
      self.x -= 2
      self.y -= 2
      if self.isHit(player):
         self.x += 1
         self.y += 1
         return
      if self.a < 0 and self.a > -10:
         return
      if not move:
         self.x += 1
         self.y += 1
         return
      if self.x < player.x:
         self.x += 1
         self.checkMove(1,0,place)
      else:
         self.x -= 1
         self.checkMove(-1,0,place)
      if self.y < player.y:
         self.y += 1
         self.checkMove(0,1,place)
      else:
         self.y -= 1
         self.checkMove(0,-1,place)
      self.x += 1
      self.y += 1
      if keys[pygame.K_w]:
         self.y += 1.5
         self.checkMove(0,1.5,place)
      if keys[pygame.K_s]:
         self.y -= 1.5
         self.checkMove(0,-1.5,place)
      if keys[pygame.K_d]:
         self.x -= 1.5
         self.checkMove(-1.5,0,place)
      if keys[pygame.K_a]:
         self.x += 1.5
         self.checkMove(1.5,0,place)

  

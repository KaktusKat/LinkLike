from sprite import sprite
import math
import pygame
import random
import time

class enemy(sprite):
   def __init__(self,image,x,y,w,h,images,ha,big = False):
      super().__init__(image,x,y,w,h,images)
      self.a         = -10
      self.ha        = ha
      self.big       = big
      self.lastmove  = [0,0]
      self.Kback     = 0
      self.attackT   = 300
      self.Acooldown = 0
      self.wait      = 0
      self.sign      = False  
      self.attacking = False
      self.timer     = 0
      self.iframes   = False
      self.iFrames   = False
      self.chasing   = False
 
   def update(self,player,move,enemy_list,keys,place,screen,weaponList):
#      self.image_index = 0
      self.attackT += 1
      if self.ha <= 0:
         enemy_list.remove(self)
         return

      if self.a == 0:
         self.a = -10
         self.ha -= 1

      if weaponList[player.tool[player.wep]].attacking == False:
         self.iframes = False

      if self.isHitXY(self.x+self.velocityX,self.y+self.velocityY,self.w+self.velocityX,self.h+self.velocityY,player) and self.attacking and not player.iFrames:
         player.health     -= 1
         player.hit         = True
         player.image_index = 1
         self.attackT       = 300
         self.attacking     = False

      else:
         self.lastmove = [0,0]

      if self.Kback == 0:
         self.lastmove = [0,0]

      if self.a < 0 and self.a > -10:
         pass

      if self.chasing:
         self.chase(player,screen,place)
      else:
         self.idle(player,screen,place)

      if self.animate > 0:
         self.move(0,2)
         if self.image_index == 1 and self.attackT > 100:
            self.y         -= 20
         elif self.attackT > 100:
            self.y         += 20
         self.animate = -10

      if self.LOS(8,player,place) and self.attackT > 300 and random.randint(0,100) == 1:
         self.attackT = 0
         self.attack(player)
      if self.attackT < 100:
         self.attack(player)

      if (self.isHit(weaponList[player.tool[player.wep]]) and weaponList[player.tool[player.wep]].attacking) and not self.iframes:
         x    = self.x
         y    = self.y
         tool = weaponList[player.tool[player.wep]]
         self.velocityX  += tool.kback*math.cos(tool.frameList[tool.frameIndex].angle)
         self.velocityY  += tool.kback*math.sin(tool.frameList[tool.frameIndex].angle)
         self.a          += 1
         self.image_index = 3
         self.iFrames     = True
         self.iframes     = True
         self.ha         -= weaponList[player.tool[player.wep]].damage
      
      self.checkMove(place,screen)
      self.Acooldown -= 1
      self.wait -= 1 
      self.timer -= 1

   def idle(self,player,screen,place):
      self.animate    = 0
      self.circle(3.5,screen,place,player)
      if self.LOS(8,player,place):
         self.chasing = True
      for tile in self.circleTiles:
         if tile in player.circleTiles:
            if player.LOS(8,tile,place):
               self.chasing = True

   def chase(self,player,screen,place):
      if self.LOS(8,player,place):
         distanceX       = self.x - player.x
         distanceY       = self.y - player.y
         totalDistance   = abs(distanceX) + abs(distanceY)
         self.velocityX -= (0.1/totalDistance)*distanceX
         self.velocityY -= (0.1/totalDistance)*distanceY
         self.animate   += 1
         return
      else:
         self.circle(3.5,screen,place,player)
         for tile in self.circleTiles:
            if tile in player.circleTiles:
               if player.LOS(8,tile,place) and self.LOS(8,tile,place):
 #                 x,y = screen.convertWTS(tile.x,tile.y)
#                  pygame.draw.rect(screen.screen,(250,250,250),pygame.Rect(x,y,58,58),2)
                  distanceX       = self.x - tile.x
                  distanceY       = self.y - tile.y
                  totalDistance   = abs(distanceX) + abs(distanceY)
                  self.animate   += 1
                  self.velocityX -= (0.2/totalDistance)*distanceX
                  self.velocityY -= (0.2/totalDistance)*distanceY
                  return
      self.chasing = False
      return

   def attack(self,player):
      if self.attackT < 70:
         self.image_index = 2
         if self.attackT == 30:
            self.distanceX       = self.x - player.x
            self.distanceY       = self.y - player.y
            self.totalDistance   = abs(self.distanceX) + abs(self.distanceY)
         if self.iframes:
            self.attackT     = 300
            self.attacking   = False
            self.image_index = 0
      elif self.attackT < 80:
          self.attacking = True
          self.image_index = 0
          if self.attackT == 71:
             self.velocityX -= (12/self.totalDistance)*self.distanceX
             self.velocityY -= (12/self.totalDistance)*self.distanceY

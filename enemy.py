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
      self.chasing   = False
 
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

      if self.chasing:
         self.chase(player,screen,place)
      else:
         self.idle(player,screen,place)
      

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

   def idle(self,player,screen,place):
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
         return
      else:
         self.circle(3.5,screen,place,player)
         for tile in self.circleTiles:
            if tile in player.circleTiles:
               if player.LOS(8,tile,place) and self.LOS(8,tile,place):
#                  x,y = screen.convertWTS(tile.x,tile.y)
 #                 pygame.draw.rect(screen.screen,(250,250,250),pygame.Rect(x,y,58,58),2)
                  distanceX       = self.x - tile.x
                  distanceY       = self.y - tile.y
                  totalDistance   = distanceX + distanceY
                  self.velocityX -= (0.1/totalDistance)*distanceX
                  self.velocityY -= (0.1/totalDistance)*distanceY
                  return
      self.chasing = False
      return


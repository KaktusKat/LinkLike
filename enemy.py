from sprite import sprite
import math
import pygame

class enemy(sprite):
   def __init__(self,image,x,y,w,h,ha,big = False):
      super().__init__(image,x,y,w,h)
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
 
   def update(self,player,move,enemy_list,keys,place,screen):
      if player.tool[player.wep].name == "spear" and player.tool[player.wep].attacking:        # check if it is a spear
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
      if self.ha == 0:
         enemy_list.remove(self)
         return
      if (self.isHit(player.tool[player.wep]) and player.tool[player.wep].attacking) and not self.iframes:
         x = self.x
         y = self.y
         self.velocityX += player.tool[player.wep].kback*math.cos(player.tool[player.wep].angle)
         self.velocityY += player.tool[player.wep].kback*math.sin(player.tool[player.wep].angle)
         self.a      += 1
         self.iframes = True

      if self.a == 0:
         self.a = -10
         self.ha -= 1

      if player.tool[player.wep].attacking == False:
         self.iframes = False

      if self.isHit(player.sheild) and self.attacking:
         self.ha    -= 3
         self.attack = -1

      if self.isHit(player) and self.attacking and self.timer < 0:
         player.health -= 1
         self.timer = 20

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
         self.velocityX  += self.lastmove[0]*2
         self.velocityY  += self.lastmove[1]*2
         self.attack     -= 1
         self.Acooldown   = 200
         self.image_index = 0
         self.sign = False
      else:
         self.attacking = False

      self.checkMove(self.velocityX,self.velocityY,place)
      self.x += self.velocityX
      self.y += self.velocityY
      self.Acooldown -= 1
      self.wait -= 1 
      self.timer -= 1

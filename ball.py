from sprite import sprite
import random
import math

class ball(sprite):
   def __init__(self,image,x,y,w,h,speed,caster):
      super().__init__(image,x,y,w,h)
      self.speed     = speed
      self.reflected = False
      self.caster    = caster

   def update(self,player,screen):
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

      if self.isHit(player.tool[player.wep]) and player.tool[player.wep].attacking:
         self.reflected = True

      if self.reflected:
         if self.x < self.caster.x:
            self.x += self.speed
         else:
           self.x -= self.speed
         if self.y < self.caster.y:
            self.y += self.speed
         else:
           self.y -= self.speed
    
      if not self.reflected:
         if self.x < player.x:
           self.x += self.speed
         else:
           self.x -= self.speed
         if self.y < player.y:
           self.y += self.speed
         else:
           self.y -= self.speed

      self.draw(screen)



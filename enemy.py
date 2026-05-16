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
      if player.wep == 3 and player.tool[player.wep].attacking:        # check if it is a spear
         Xmove = 0
         Ymove = 0
         tool  = player.tool[player.wep]
         if ((-tool.angle)*180/math.pi < 90 and (-tool.angle)*180/math.pi > 0) or ((-tool.angle)*180/math.pi > -90 and (-tool.angle)*180/math.pi < 0):
            Xmove += tool.Rwepon.get_width()/2
         if (-tool.angle)*180/math.pi < 0:
            Ymove += tool.Rwepon.get_height()/2
         pygame.draw.rect(screen.screen,(0,250,0),pygame.Rect(((tool.dX-tool.Rwepon.get_width()/2)-player.x+290)+Xmove,((tool.dY-tool.Rwepon.get_height()/2)-player.y+290)+Ymove,75,75),2)
         player.tool[player.wep].x = (tool.dX-tool.Rwepon.get_width()/2)+Xmove
         player.tool[player.wep].y = (tool.dY-tool.Rwepon.get_height()/2)+Ymove
         player.tool[player.wep].w = 75
         player.tool[player.wep].h = 75
      hit = False
      if self.ha == 0:
         enemy_list.remove(self)
         return
      if (self.isHit(player.tool[player.wep],screen,True,player) and player.tool[player.wep].attacking) or (self.a < 0 and self.a > -10):
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

      if self.isHit(player.sheild) and self.attacking:
         self.ha    -= 3
         self.attack = -1

      if self.isHit(player) and self.attacking and self.timer < 0:
         self.x += 1
         self.y += 1
         player.health -= 1
         self.timer = 20

      else:
         self.lastmove = [0,0]

      if self.Kback == 0:
         self.lastmove = [0,0]

      if self.a < 0 and self.a > -10:
         return

      if not move:
         self.x += 1
         self.y += 1
         return

      if self.x < player.x:
         self.x += 1
         self.lastmove[0] = 1 
         self.checkMove(1,0,place)
      else:
         self.x -= 1
         self.lastmove[0] = -1
         self.checkMove(-1,0,place)

      if self.y < player.y:
         self.y += 1
         self.lastmove[1] = 1
         self.checkMove(0,1,place)
      else:
         self.y -= 1
         self.lastmove[1] = -1
         self.checkMove(0,-1,place)

      self.x += 1
      self.y += 1

      if (abs(self.x - player.x) <= 100 or abs(self.y - player.y) <= 100) and self.Acooldown < 0:
         self.attack = 10
         self.image_index = 1
         if not self.sign:
            self.wait = 70
            self.sign = True

      if self.attack > 0 and self.wait < 0:
         self.attacking = True
         self.x        += self.lastmove[0]*11
         self.y        += self.lastmove[1]*11
         self.attack   -= 1
         self.Acooldown = 200
         self.image_index = 0
         self.sign = False
      else:
         self.attacking = False

#      if keys[pygame.K_w]:
 #        self.y += 0.5
  #       self.checkMove(0,1.5,place)

#      if keys[pygame.K_s]:
 #        self.y -= 0.5
  #       self.checkMove(0,-1.5,place)

#      if keys[pygame.K_d]:
 #        self.x -= 0.5
  #       self.checkMove(-1.5,0,place)

#      if keys[pygame.K_a]:
 #        self.x += 0.5
  #       self.checkMove(1.5,0,place)

      self.Acooldown -= 1
      self.wait -= 1 
      self.timer -= 1

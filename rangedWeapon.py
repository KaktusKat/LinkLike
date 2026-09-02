import pygame
import copy
import math
from weapon import weapon

class rangedWeapon(weapon):
   def __init__(self,Aspeed,damage,Kback,projectile,frame):
      super().__init__(Aspeed,damage,Kback)
      self.projectile = projectile
      self.frame      = frame

   def attack(self,screen,user,sound,projectileList):
      
      self.rotateImg    = screen.images[self.projectile.image[0]]

      self.AspeedTimer += 1

      Mpress = pygame.mouse.get_pressed()

      if self.AspeedTimer == 2:
         if self.attackTimer > self.Aspeed and self.projectile.item.amount >= 1:
         
            self.projectile.item.amount -= 1
            newProjectile = copy.deepcopy(self.projectile)
            newProjectile.velocityX  += (self.kback*math.cos(self.frame.KBangle))
            newProjectile.velocityY  += (self.kback*math.sin(self.frame.KBangle))
            newProjectile.x           = user.x + user.w/2
            newProjectile.y           = user.y + user.h/2
            newProjectile.angle       = (180*self.frame.KBangle)/math.pi
            projectileList.append(newProjectile)
            self.frame.draw(screen,user)

         self.attackTimer    = 0
         self.frame.numRound = 0

      if Mpress[0]:
        self.frame.attack(user,screen)
        self.frame.draw(screen,user)
        self.AspeedTimer  = 0
        self.attackTimer += 1
        self.frame.image_index  = 0
        if self.attackTimer > self.Aspeed and self.projectile.item.amount >= 1:
           self.frame.image_index = len(self.frame.image)-1


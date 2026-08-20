from weapon import weapon
import math
import pygame

class meleeWeapon(weapon):
   def __init__(self,Aspeed,damage,kBack,frameList,comboSpeed):
      super().__init__(Aspeed,damage,kBack)
      self.frameList   = frameList
      self.frameIndex  = 0
      self.comboTimer  = 0
      self.comboSpeed  = comboSpeed

   def attack(self,screen,user):

      self.comboTimer  += 1
      self.AspeedTimer += 1
      self.attackTimer += 1

      Mpress = pygame.mouse.get_pressed()

      if self.attackTimer < 30:
  
         if self.attackTimer == 2:

            frame            = self.frameList[self.frameIndex]
            user.velocityX  -= (self.kback*math.cos(frame.angle+frame.slashMove*4))/2.5
            user.velocityY  -= (self.kback*math.sin(frame.angle+frame.slashMove*4))/2.5
 
         self.frameList[self.frameIndex].draw(screen,user)
         self.x = self.frameList[self.frameIndex].x
         self.y = self.frameList[self.frameIndex].y
         self.w = self.frameList[self.frameIndex].w
         self.h = self.frameList[self.frameIndex].h
      else:
         self.attacking = False

      if not self.AspeedTimer > self.Aspeed:
         return

      if Mpress[0]:

         if self.comboTimer < self.comboSpeed and self.frameIndex < len(self.frameList)-1:
            self.frameIndex += 1
         else:
            self.frameIndex = 0

         self.frameList[self.frameIndex].attack(user,screen)
         self.frameList[self.frameIndex].draw(screen,user)

         self.comboTimer  = 0
         self.AspeedTimer = 0
         self.attackTimer = 0
         self.attacking   = True



import math
import pygame
from meleeWeapon import meleeWeapon

class syring(meleeWeapon):
   def __init__(self,Aspeed,damage,kBack,frameList,comboSpeed,image,images,item):
      super().__init__(Aspeed,damage,kBack,frameList,comboSpeed,image,images)
      self.item = item.name

   def attack(self,screen,user,sound,useless,itemDict):
      item = itemDict[self.item]

      self.comboTimer  += 1
      self.AspeedTimer += 1
      self.attackTimer += 1

      Mpress = pygame.mouse.get_pressed()

      if self.attackTimer < 30:

         if self.attackTimer == 5:
           self.attacking = False

         if self.hit:

            self.hit = False
            item.amount     += 1
            frame            = self.frameList[self.frameIndex]
            user.velocityX  -= (self.kback*math.cos(frame.KBangle))/2.5
            user.velocityY  -= (self.kback*math.sin(frame.KBangle))/2.5

         self.frameList[self.frameIndex].draw(screen,user)
         self.x      = self.frameList[self.frameIndex].x
         self.y      = self.frameList[self.frameIndex].y
         self.w      = self.frameList[self.frameIndex].w
         self.h      = self.frameList[self.frameIndex].h
         self.hitBox = self.frameList[self.frameIndex].hitBox
         x,y         = screen.convertWTS(self.x,self.y)

      else:
        pass

      if not self.AspeedTimer > self.Aspeed:
         return

      if Mpress[0]:

         if self.comboTimer < self.comboSpeed and self.frameIndex < len(self.frameList)-1:
            self.frameIndex += 1
         else:
            self.frameIndex = 0

         self.frameList[self.frameIndex].attack(user,screen)
         self.frameList[self.frameIndex].draw(screen,user)

         self.x      = self.frameList[self.frameIndex].x
         self.y      = self.frameList[self.frameIndex].y
         self.w      = self.frameList[self.frameIndex].w
         self.h      = self.frameList[self.frameIndex].h
         self.hitBox = self.frameList[self.frameIndex].hitBox

         self.comboTimer  = 0
         self.AspeedTimer = 0
         self.attackTimer = 0
         self.attacking   = True

                                                                                                                                               



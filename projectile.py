import pygame
from sprite import sprite

class projectile(sprite):
   def __init__(self,img,x,y,w,h,images,item,damage,hitNoise,sound,Range,bounce,offset = 0):
      super().__init__(img,x,y,w,h,images)
      self.damage   = damage
      self.item     = item
      self.bounce   = bounce
      self.range    = Range
      self.offset   = offset
      self.hitNoise = sound.loadS(hitNoise)

   def update(self,screen,sound,enemyList,projectileList,place):
      self.range -= abs(self.velocityX)+abs(self.velocityY)
      self.x     += self.velocityX
      self.y     += self.velocityY
      for enemy in enemyList:
         if self.isHit(enemy):
            enemy.ha     -= self.damage
            enemy.iFrames = True
            enemy.iframes = self.damage
            sound.playS(self.hitNoise)
            self.range    = 0
      if self.checkMoveTF(place,screen):
         if not self.bounce:
            self.range = 0
         else:
            pass             #TODO
      if self.range <= 0:
         sound.playS(self.hitNoise)
         projectileList.remove(self)

   def draw(self, screen):
      img = pygame.transform.rotate(screen.images[self.image[self.image_index]],-self.angle-self.offset)
      if self.flipS:
         img = pygame.transform.flip(img,True,False)
      if self.flip:
         img = pygame.transform.flip(img,False,True)
      screen.blit(img, self.x, self.y)


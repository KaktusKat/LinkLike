import pygame
import math
from sprite import sprite

class tool(sprite):
   def __init__(self,image,x,y,w,h,d,Aspeed,kback=20,ratio = 1):
      super().__init__(image,x,y,w*ratio,h*ratio)
      self.distance = d
      self.Aspeed   = Aspeed
      self.timer    = 0
      self.t        = Aspeed
      self.dX       = 1
      self.dY       = 1
      self.kback    = kback
      self.angle    = 0

   def attack(self,user,screen):
      if self.t < self.Aspeed:
         return
      userx,usery = screen.convict(user.x,user.y)
      u_y         = usery+user.h/2
      u_x         = userx+user.w/2
      flip        = screen.width/2
      Mpos        = pygame.mouse.get_pos()
      self.angle  = math.atan2(Mpos[1]-u_y,Mpos[0]-u_x)
      angle        = ((180*self.angle)/math.pi)
      self.Rwepon = pygame.transform.rotate(self.image[0],-angle)
      self.timer  = 30

   def use(self,screen,user):
      self.t += 1
      if self.timer > 0:
         self.x = self.dX-self.image[0].get_width()/2
         self.y = self.dY-self.image[0].get_height()/2
         self.draw(screen,user)
         self.timer -= 1
         self.t      = 0
         return

   def draw(self,screen,user):
      u_y     = user.y+user.h/2
      u_x     = user.x+user.w/2
      self.dX = u_x+self.distance*math.cos(self.angle)
      self.dY = u_y+self.distance*math.sin(self.angle)
      img = self.Rwepon
      if self.flip:
         self.x += 10 
         img = pygame.transform.flip(img,True,False)
      screen.blit(img, self.dX-img.get_width()/2, self.dY-img.get_height()/2)


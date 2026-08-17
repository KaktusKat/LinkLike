import pygame
import math
from sprite import sprite

class frame(sprite):
   def __init__(self,image,w,h,images,d,numMove,ratio = 1,dx = 1,dy = 1,x = -100,y = -100):
      super().__init__(image,x,y,w*ratio,h*ratio,images)
      self.distance    = d
      self.dSave       = d
      self.dX          = dx
      self.dY          = dy
      self.angle       = 0
      self.Rwepon      = self.image[0]
      self.numMove     = numMove

   def attack(self,user,screen):
      userx,usery = screen.convertWTS(user.x,user.y)
      u_y         = usery+user.h/2
      u_x         = userx+user.w/2
      flip        = screen.width/2
      Mpos        = pygame.mouse.get_pos()
      self.angle  = math.atan2(Mpos[1]-u_y,Mpos[0]-u_x)
      angle       = ((180*self.angle)/math.pi)
      self.Rwepon = -angle

   def use(self,screen,user):
      self.x         = self.dX-self.image[0].get_width()/2
      self.y         = self.dY-self.image[0].get_height()/2

   def draw(self,screen,user):
      self.use(screen,user)
      u_y     = user.y+user.h/2
      u_x     = user.x+user.w/2
      self.dX = u_x+self.distance*math.cos(self.angle)
      self.dY = u_y+self.distance*math.sin(self.angle)
      img = pygame.transform.rotate(screen.images[self.image[self.image_index]],self.Rwepon)
      screen.blit(img, self.dX-img.get_width()/2, self.dY-img.get_height()/2)


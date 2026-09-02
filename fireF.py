from frame import frame
import pygame
import math

class fireF(frame):
   def __init__(self,img,w,h,images,d,numMove,lenImage,ratio = 1,dx = 1,dy = 1,x = -100, y = -100):
      super().__init__(img,w,h,images,d,numMove,ratio,dx,dy,x,y)
      self.lenImage   = lenImage
      self.numRound   = 0

   def attack(self,user,screen):
      userx,usery   = screen.convertWTS(user.x,user.y)
      u_y           = usery+user.h/2
      u_x           = userx+user.w/2
      flip          = screen.width/2
      Mpos          = pygame.mouse.get_pos()
      self.KBangle  = math.atan2(Mpos[1]-u_y,Mpos[0]-u_x)
      self.angle    = math.atan2(Mpos[1]-u_y,Mpos[0]-u_x)
      angle         = ((180*self.angle)/math.pi)
      self.Rwepon   = -angle


   def use(self,screen,user):
      self.numRound   += 1
      if self.numRound >= self.lenImage and self.image_index == 0:
         self.image_index = 1
      self.x         = self.dX-screen.images[self.image[0]].get_width()/2
      self.y         = self.dY-screen.images[self.image[0]].get_height()/2

   def draw(self,screen,user):
      self.use(screen,user)
      u_y     = user.y+user.h/2
      u_x     = user.x+user.w/2
      self.dX = u_x+self.distance*math.cos(self.angle)
      self.dY = u_y+self.distance*math.sin(self.angle)
      img  = pygame.transform.rotate(screen.images[self.image[self.image_index]],self.Rwepon)
      screen.blit(img, self.dX-img.get_width()/2, self.dY-img.get_height()/2)
                                                                 

import pygame
import math
import time
from frame import frame

class slashF(frame):
   def __init__(self,image,w,h,images,d,slashMove,numMove,ratio = 1,dx = 1,dy = 1,x = -100,y = -100):
      super().__init__(image,w,h,images,d,numMove,ratio,dx,dy,x,y)
      self.slashMove  = slashMove
      self.slashMoved = -slashMove
      self.MposSaved  = 0
      self.fliped     = False

   def attack(self,user,screen):
      userx,usery = screen.convertWTS(user.x,user.y)
      u_y         = usery+user.h/2
      u_x         = userx+user.w/2
      flip        = screen.width/2
      if self.num == 1:
         Mpos          = pygame.mouse.get_pos()
         self.MposSave = Mpos
      else:
         Mpos = self.MposSave
      self.angle  = math.atan2(Mpos[1]-u_y,Mpos[0]-u_x)
      self.angle += self.slashMoved-self.slashMove*5
      angle  = ((180*self.angle)/math.pi)
      self.Rwepon = -angle
       

   def use(self,screen,user):
      self.slashMoved += self.slashMove
      self.num         = int(self.slashMoved/self.slashMove)
      self.image_index = 0
      if self.num >= self.numMove:
         self.image_index = 1
      if self.num <= self.numMove:
         self.attack(user,screen)
      if self.num == 29:
         self.slashMoved = -self.slashMove
      self.x           = self.dX-screen.images[self.image[0]].get_width()/2
      self.y           = self.dY-screen.images[self.image[0]].get_height()/2


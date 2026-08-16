import math
from frame import frame

class stabF(frame):
   def __init__(self,image,w,h,d,stabMove,numMove,ratio = 1,dx = 1,dy = 1,x = -100,y = -100):
      super().__init__(image,w,h,d,numMove,ratio,dx,dy,x,y)
      self.stabMove = stabMove
      self.dSave    = d

   def use(self,screen,user):
      self.num += 1
      if self.num <= self.numMove:
         self.distance += self.stabMove
      self.x         = self.dX-self.image[0].get_width()/2
      self.y         = self.dY-self.image[0].get_height()/2

   def draw(self,screen,user):
      self.use(screen,user)
      u_y     = user.y+user.h/2
      u_x     = user.x+user.w/2
      self.dX = u_x+self.distance*math.cos(self.angle)
      self.dY = u_y+self.distance*math.sin(self.angle)
      img = self.Rwepon
      if self.flip:
         self.x += 10
         img = pygame.transform.flip(img,True,False)
      screen.blit(img, self.dX-img.get_width()/2, self.dY-img.get_height()/2)
      if self.num == 30:
         self.num = 0
         self.distance = self.dSave

import pygame

class sprite:
   def __init__(self, img, posX, posY, w, h, count = 1):
      self.x      = posX
      self.y      = posY
      self.image  = []
      for i in range(len(img)):
         image = pygame.image.load(img[i])
         self.image.append(pygame.transform.scale(image,(w,h)))
      self.h      = h
      self.w      = w
      self.flip   = False
      self.num    = count
      self.image_index = 0

   def move(self):
      self.image_index += 1
      if self.image_index == len(self.image):
          self.image_index = 0

   def draw(self, screen):
      img = self.image[self.image_index]
      if self.flip:
         img = pygame.transform.flip(img,False,True)
      screen.blit(img,(self.x,self.y))

   def isHit(self, other, player = False):

      if self == other:
         return False

      top_x = self.x + self.w
      top_y = self.y + self.h

      if not player:
         other_top_x = other.x + other.w
         other_top_y = other.y + other.h
      else:
         other_top_x = other.xPos + other.w
         other_top_y = other.yPos + other.h

      if (top_x > other.x and top_x < other_top_x) or \
         (self.x > other.x and self.x < other_top_x):
         if (top_y > other.y and top_y < other_top_y) or \
            (self.y > other.y and self.y < other_top_y):
            return True
      return False 

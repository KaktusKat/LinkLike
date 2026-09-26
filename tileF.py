from tileO import tileO

class tileF(tileO):
   def __init__(self,img,posX,posY,w,h,images,hitBoxL,solid,biomes = []):
      super().__init__(img,posX,posY,w,h,images,hitBoxL,solid,biomes)
      self.fenceDraw = []

   def draw(self,screen):
      img = screen.images[self.image[self.image_index]]
      if self.flipS:
         img = pygame.transform.flip(img,True,False)
      if self.flip:
         img = pygame.transform.flip(img,False,True)
      screen.blit(img, self.x, self.y)

      for draw in self.fenceDraw:
         screen.blit(screen.images["images/"+draw[0]], self.x+draw[1], self.y+draw[2])
      

import pygame

class weapon:
   def __init__(self,Aspeed,damage,kback,image,images):
      self.Aspeed      = Aspeed
      self.image          = "images/"+image
      img                 = pygame.image.load(self.image)
      images[self.image]  = pygame.transform.scale(img,(75,75))
      self.select         = "images/select.png"
      img                 = pygame.image.load(self.select)
      images[self.select] = pygame.transform.scale(img,(75,75))
      self.damage      = damage
      self.kback       = kback
      self.AspeedTimer = 0
      self.attacking   = False
      self.attackTimer = 30
      self.x           = 0
      self.y           = 0
      self.w           = 0
      self.h           = 0

   def draw(self,screen):
      screen.screen.blit(screen.images[self.select],(110,10))
      screen.screen.blit(screen.images[self.image],(110,10))

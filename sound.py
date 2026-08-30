import pygame

class sound:
   def __init__(self):
      self.soundDict = {}

   def loadM(self,sound):
      pygame.mixer.music.load("sounds/"+sound)
      pygame.mixer.music.play(100000000)

   def loadS(self,sound):
      noise = pygame.mixer.Sound("sounds/"+sound)
      self.soundDict[sound] = noise
      return sound

   def playS(self,sound):
      pygame.mixer.Sound.play(self.soundDict[sound])

   def playM(self):
      pygame.mixer.music.play(-1)


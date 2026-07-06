import pygame
import random
from tile import tile
from enemy import enemy
import numpy as np

class place:

   def __init__(self,biomes,wood,rock,flint):
       self.map_dic      = {}
       self.map_dic2     = {}
       self.wood         = wood
       self.rock         = rock
       self.flint        = flint
       self.images       = {}
       self.prob         = {}
       for biome in biomes:
          self.images[biome.name] = biome.images
          self.prob[biome.name]   = biome.prob

   def genKeyC(self, cell_x, cell_y):
       return cell_x + cell_y * 100000

   def genKeyP(self, x, y):
       return self.genKeyC(x // 58, y // 58)
    
   def create(self, screen, player, enemy_list,tool1,tool2,tool3,keys,invet,biomeList):

      Mpos   = pygame.mouse.get_pos()

      TREE   = 0
      ENEMY  = 1
      ROCK   = 2
      EMPTY  = 3

      for x in range(-6, 6):
         for y in range(-6, 6):
            

            map_x = x + player.x // 58
            map_y = y + player.y // 58
            key   = self.genKeyC(map_x, map_y)

            xPos = player.x + x * 58 - (player.x % 58)
            yPos = player.y + y * 58 - (player.y % 58)

            if key in self.map_dic:
               if not self.map_dic[key].justMade:
                  if len(self.map_dic[key].toolList) > 0:
                     for tool in self.map_dic[key].toolList:
                        if self.map_dic[key].isHit(tool[0]) and tool[0].attacking and not self.map_dic[key].iframes:
                           self.map_dic[key].health += 1
                           self.map_dic[key].iframes = True
                           self.map_dic[key].toolHit = tool[0]
                           if self.map_dic[key].health == tool[1]: 
                              imageValues                    = random.choice(self.map_dic[key].change)
                              self.map_dic[key].image        = imageValues.image.copy()
                              self.map_dic[key].soild        = imageValues.soild
                              self.map_dic[key].breakable    = imageValues.breakable
                              self.map_dic[key].portal       = imageValues.portal
                              self.map_dic[key].toolList     = []
                              self.map_dic[key].item.amount += 1
                  
                  if self.map_dic[key].iframes and not self.map_dic[key].toolHit.attacking:
                     self.map_dic[key].iframes = False

                  self.map_dic[key].draw(screen)

               imaged = True
               if self.map_dic[key].justMade:
                  imaged = False
            else:
               imaged = False
            if not imaged:
               for keyX in range(-7,7):
                  for keyY in range(-7,7):
                     map_x = keyX + player.x // 58
                     map_y = keyY + player.y // 58
                     key2  = self.genKeyC(map_x, map_y)
                     xpos = player.x + keyX * 58 - (player.x % 58)
                     ypos = player.y + keyY * 58 - (player.y % 58)
                     if not key2 in self.map_dic:
                        self.map_dic[key2] = tile(["grass.png"],xpos,ypos,58,58,False,biomeList,justMade = True)
               for keyX in range(-6,6):
                  for keyY in range(-6,6):
                     map_x = keyX + player.x // 58
                     map_y = keyY + player.y // 58
                     key2  = self.genKeyC(map_x, map_y)
                     self.map_dic[key2].near(self.map_dic,self)
                     self.map_dic[key2].probabilaty()
               highest = 0
               highestTest = 0
               change = 0
               gotIn  = False
               for keyX2 in range(-6,6):
                  for keyY2 in range(-6,6):
                     map_x = keyX2 + player.x // 58
                     map_y = keyY2 + player.y // 58
                     key3  = self.genKeyC(map_x, map_y)
                     if self.map_dic[key3].maxProb > highestTest and self.map_dic[key3].biome == 0:
                        highest     = self.map_dic[key3].prob
                        highestTest = self.map_dic[key3].maxProb
                        change      = self.map_dic[key3]
                        gotIn       = True
               if not change == 0:
                  b = np.random.choice(change.biomes,p = list(dict.values(highest)))
                  change.biome     = b.name
                  imageValues      = np.random.choice(self.images[change.biome],p = self.prob[change.biome])
                  change.image     = imageValues.image.copy()
                  change.soild     = imageValues.soild
                  change.breakable = imageValues.breakable
                  change.toolList  = imageValues.toolList.copy()
                  change.item      = imageValues.item
                  change.change    = imageValues.change.copy()
                  change.justMade  = False
                  change.health    = 0
                  change.draw(screen)

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
       self.connectors   = {}
       for biome in biomes:
          self.connectors[biome.name] = biome.connectors
          self.images[biome.name]     = biome.images
          self.prob[biome.name]       = biome.prob

   def genKeyC(self, cell_x, cell_y):
       return cell_x + cell_y * 100000

   def genKeyP(self, x, y):
       return self.genKeyC(x // 58, y // 58)
    
   def create(self, screen, player, enemy_list,tool1,tool2,tool3,keys,invet,biomeList,biomeDict,weaponList,sound):

      Mpos   = pygame.mouse.get_pos()

      TREE   = 0
      ENEMY  = 1
      ROCK   = 2
      EMPTY  = 3

      for x in range(-7, 7):
         for y in range(-7, 7):
            

            map_x = x + player.x // 58
            map_y = y + player.y // 58
            key   = self.genKeyC(map_x, map_y)

            xPos = player.x + x * 58 - (player.x % 58)
            yPos = player.y + y * 58 - (player.y % 58)

            if key in self.map_dic:
               if not self.map_dic[key].justMade:
                  if len(self.map_dic[key].toolList) > 0:
                     for tool in self.map_dic[key].toolList:
                        if self.map_dic[key].isHit(weaponList[tool[0]]) and weaponList[tool[0]].attacking and not self.map_dic[key].iframes:
                           self.map_dic[key].health += 1
                           sound.playS(self.map_dic[key].noise)
                           weaponList[tool[0]].hit   = True
                           self.map_dic[key].iframes = True
                           if len(tool) == 4:
                              tool[2].amount += tool[3]
                           self.map_dic[key].toolHit = tool[0]
                           if self.map_dic[key].health >= tool[1]: 
                              imageValues                    = random.choice(self.map_dic[key].change)
                              self.map_dic[key].image        = imageValues.image.copy()
                              self.map_dic[key].soild        = imageValues.soild
                              self.map_dic[key].breakable    = imageValues.breakable
                              self.map_dic[key].portal       = imageValues.portal
                              self.map_dic[key].toolList     = []
                              self.map_dic[key].item.amount += 1
                  
                  if self.map_dic[key].iframes and not weaponList[self.map_dic[key].toolHit].attacking:
                     self.map_dic[key].iframes = False

                  possibaleC = []
                  if not self.map_dic[key].connector:
                     self.map_dic[key].near(self.map_dic,self)
                     if not self.map_dic[key].biomeNear[self.map_dic[key].biome] == 4-self.map_dic[key].emptyNear:
                        for biome in self.map_dic[key].biomeNear:
                           if not biome == self.map_dic[key].biome:
                             for connector in biomeDict[self.map_dic[key].biome].connectors:
                                if connector in biomeDict[biome].connectors:
                                   possibaleC.append(connector)

                  if len(possibaleC) > 0:
                     ImageValues                 = np.random.choice(possibaleC)
                     self.map_dic[key].soild     = ImageValues.soild
                     self.map_dic[key].h         = ImageValues.h
                     self.map_dic[key].w         = ImageValues.w
                     self.map_dic[key].image     = ImageValues.image.copy()
                     self.map_dic[key].toolList  = ImageValues.toolList.copy()
                     self.map_dic[key].item      = ImageValues.item
                     self.map_dic[key].change    = ImageValues.change.copy()

                  self.map_dic[key].connector = True
                  self.map_dic[key].draw(screen)
                     

               imaged = True
               if self.map_dic[key].justMade:
                  imaged = False
            else:
               imaged = False
            if not imaged:
               for keyX in range(-9,9):
                  for keyY in range(-9,9):
                     map_x = keyX + player.x // 58
                     map_y = keyY + player.y // 58
                     key2  = self.genKeyC(map_x, map_y)
                     xpos = player.x + keyX * 58 - (player.x % 58)
                     ypos = player.y + keyY * 58 - (player.y % 58)
                     if not key2 in self.map_dic:
                        self.map_dic[key2] = tile(["grass.png"],xpos,ypos,58,58,screen.images,False,biomeList,justMade = True)
               for keyX in range(-8,8):
                  for keyY in range(-8,8):
                     map_x = keyX + player.x // 58
                     map_y = keyY + player.y // 58
                     key2  = self.genKeyC(map_x, map_y)
                     self.map_dic[key2].near(self.map_dic,self)
                     self.map_dic[key2].probabilaty()
               highest = 0
               highestTest = 0
               change = 0
               for keyX2 in range(-8,8):
                  for keyY2 in range(-8,8):
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
                  change.w         = imageValues.w
                  change.h         = imageValues.h
                  change.soild     = imageValues.soild
                  change.breakable = imageValues.breakable
                  change.toolList  = imageValues.toolList.copy()
                  change.item      = imageValues.item
                  change.change    = imageValues.change.copy()
                  change.justMade  = False
                  change.health    = 0
                  change.noise     = imageValues.noise
                  if random.randint(0,200) == 1 and not change.soild:
                     e = enemy(["blob.png","blobM.png","blobAttacking.png","blobHurt.png"],change.x,change.y,60,54,screen.images,sound,"enemyHit.wav",12)
                     enemy_list.append(e)


import pygame
import copy
import random
from datetime import datetime
from tileO import tileO
from enemy import enemy
import numpy as np

class place:

   def __init__(self,biomes,wood,rock,flint):
       self.map_dic      = {}
       self.map_dic2     = {}
       self.time         = 0
       self.darkness     = 0
       self.daySpeed     = 10000
       self.wood         = wood
       self.rock         = rock
       self.flint        = flint
       self.structList   = []
       self.structPDict  = {}
       self.images1      = {}
       self.images2      = {}
       self.prob1        = {}
       self.prob2        = {}
       self.structDict   = {}
       for biome in biomes:
          self.structDict[biome.name]  = biome.strutures
          self.structPDict[biome.name] = biome.probS
          self.images1[biome.name]     = biome.images1
          self.images2[biome.name]     = biome.images2
          self.prob1[biome.name]       = biome.prob1
          self.prob2[biome.name]       = biome.prob2

   def genKeyC(self, cell_x, cell_y):
       return cell_x + cell_y * 100000

   def genKeyP(self, x, y):
       return self.genKeyC(x // 58, y // 58)
    
   def create(self, screen, player, enemy_list,tool1,tool2,tool3,keys,invet,biomeList,biomeDict,weaponList,perlinNoiseL,sound,slime):

      self.time += 1
      time = self.time % self.daySpeed
      print(time)

      if time > self.daySpeed / 2 - 160 and time < self.daySpeed / 2 + 160:
        self.darkness += 0.5
      
      if time > self.daySpeed - 320:
        self.darkness -= 0.5

      Mpos   = pygame.mouse.get_pos()

      timesIn = 0

      for x in range(-7, 7):
         for y in range(-7, 7):
            

            map_x = x + player.x // 58
            map_y = y + player.y // 58
            key   = self.genKeyC(map_x, map_y)

            xPos = player.x + x * 58 - (player.x % 58)
            yPos = player.y + y * 58 - (player.y % 58)


            if key in self.map_dic:
               if not self.map_dic2[key].justMade and (not self.map_dic[key].biome == 0 or True):
                  timesIn += 1
                  

                  if self.map_dic2[key].iframes and not weaponList[self.map_dic2[key].toolHit].attacking:
                     self.map_dic2[key].iframes = False

                  possibaleC = []

                  self.map_dic[key].connector = True
                  self.map_dic[key].draw(screen)
                  self.map_dic2[key].draw(screen)
                     
                  if len(self.map_dic2[key].toolList) > 0:
                     for tool in self.map_dic2[key].toolList:
                        if self.map_dic2[key].hitBox.isHit(weaponList[tool[0]].hitBox) and weaponList[tool[0]].attacking and not self.map_dic2[key].iframes:
                           self.map_dic2[key].health += 1
                           sound.playS(self.map_dic2[key].noise)
                           weaponList[tool[0]].hit   = True
                           self.map_dic2[key].iframes = True
                           if len(tool) == 4:
                              tool[2].amount += tool[3]
                           self.map_dic2[key].toolHit = tool[0]
                           if self.map_dic2[key].health >= tool[1]:
                              self.map_dic2[key].item.amount += 1
                              self.map_dic2[key].soild        = False
                              self.map_dic2[key].connectS     = {-1:False,1:False}
                              self.map_dic2[key].connectU     = {-1:False,1:False}
                              if self.map_dic2[key] in player.placeList[player.placeIndex].objectList:
                                 player.placeList[player.placeIndex].objectList.remove(self.map_dic2[key])
                                 player.placeList[player.placeIndex].unloadN(self.map_dic2[key],self)
                              self.map_dic2[key].change[0].makeTile(self.map_dic2[key])
                              

         for x in range(-20,21):
            for y in range(-20,21):
               xK  = x + player.x // 58
               yK  = y + player.y // 58
               key = self.genKeyC(xK,yK)
               value = []
               if (x < -10 or x > 10) and (y < -10 or y > 10) and len(enemy_list) < 10 and time > self.daySpeed / 2:
                 if random.randint(0,1000) == 1:
                    self.spawnEnemy(xK*58,yK*58,screen.images,sound,slime,enemy_list)
               if not key in self.map_dic:
                  self.map_dic[key]  = tileO(["grass2.png"],xK*58,yK*58,58,58,screen.images,[[0,0,58,58]],False,biomeList,justMade = False)
                  self.map_dic2[key] = tileO(["tree.png"],xK*58,yK*58,58,58,screen.images,[[0,0,58,58]],False,biomeList,justMade = False)
                  self.makeTile(key,screen,biomeList,perlinNoiseL)
                  self.structPlace(screen,xK*58,yK*58,perlinNoiseL,biomeList,self.map_dic[key].biome)

   def makeTile(self,key,images,biomeList,perlinNoiseL):
      value = []
      for perlinNoise in perlinNoiseL:
         value.append(perlinNoise.value(self.map_dic[key].x/58,self.map_dic[key].y/58))
         for biome in biomeList:
             biomeC = True
             for i in range(len(biome.maxMin)):
                if not (value[i] <= biome.maxMin[i][0] and value[i] >= biome.maxMin[i][1]):
                   biomeC = False
             if biomeC:
                self.change(key,biome,images,biomeList)

   def change(self,key,biome,images,biomeList):
       change1 = self.map_dic[key]
       change2 = self.map_dic2[key]
       self.map_dic[key].biome     = biome.name
       self.map_dic[key].justMade  = False
       imageValues                 = np.random.choice(self.images1[self.map_dic[key].biome],p = self.prob1[self.map_dic[key].biome])   
       imageValues2                = np.random.choice(self.images2[self.map_dic[key].biome],p = self.prob2[self.map_dic[key].biome])
       change1.image             = imageValues.image.copy()
       change1.w                 = imageValues.w
       change1.h                 = imageValues.h
       change1.soild             = imageValues.soild
       change1.breakable         = imageValues.breakable
       change1.toolList          = imageValues.toolList.copy()
       change1.item              = imageValues.item
       change1.change            = imageValues.change.copy()
       change1.justMade          = False
       change1.hitBox.hitBoxList = imageValues.hitBoxL
       change1.health            = 0
       change1.noise             = imageValues.noise
       if not change2.made:
          change2.hitBox.hitBoxList = imageValues2.hitBoxL
          change2.bounce            = imageValues2.bounce
          change2.image             = imageValues2.image.copy()
          change2.w                 = imageValues2.w
          change2.h                 = imageValues2.h
          change2.change            = imageValues2.change.copy()
          change2.soild             = imageValues2.soild
          change2.breakable         = imageValues2.breakable
          change2.toolList          = imageValues2.toolList.copy()
          change2.item              = imageValues2.item
          change2.health            = 0
          change2.noise             = imageValues2.noise
          change2.justMade          = False

   def spawnEnemy(self,x,y,images,sound,item,enemy_list):
       e = enemy(["blob.png","blobM.png","blobAttacking.png","blobHurt.png"],x,y,60,54,images,[[0,0,60,54]],sound,"enemyHit.wav",12,item)
       enemy_list.append(e)
       
   def structPlace(self,screen,x,y,perlinNoiseL,biomeList,biome):
       struct = np.random.choice(self.structDict[biome],p = self.structPDict[biome])
       struct.place(screen.images,self,x,y,biomeList,0,perlinNoiseL)

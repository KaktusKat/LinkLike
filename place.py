import pygame
import random
from tile import tile
from enemy import enemy

class place:

   def __init__(self,map_list):
       self.map_dic  = map_list
       self.treesCut = 0

   def genKeyC(self, cell_x, cell_y):
       return cell_x + cell_y * 100000

   def genKeyP(self, x, y):
       return self.genKeyC(x // 58, y // 58)
    
   def create(self, screen, player, enemy_list,tool,keys,invet):

      Mpos   = pygame.mouse.get_pos()

      TREE   = 0
      ENEMY  = 1
      EMPTY  = 2

      for x in range(-5, 5):
         for y in range(-5, 5):
            

            map_x = x + player.x // 58
            map_y = y + player.y // 58
            key   = self.genKeyC(map_x, map_y)

            xPos = player.x + x * 58 - (player.x % 58)
            yPos = player.y + y * 58 - (player.y % 58)

            if key in self.map_dic:
               if tool.attacking:
                  if self.map_dic[key].isHit(tool) and self.map_dic[key].soild: 
                     grass = pygame.image.load("stump.png")
                     self.map_dic[key].image[0] = pygame.transform.scale(grass,(58,58))
                     self.map_dic[key].soild    = False
                     self.treesCut += 1
               self.map_dic[key].draw(screen)

            else:
               self.map_dic[key] = random.randint(0, 2)
               if self.map_dic[key] == TREE:
                  t = tile(["tree.png"],xPos,yPos,58,58, soild = True)
                  if xPos == 0 and yPos == 0: 
                     t = tile(["grass.png"],xPos,yPos,58,58, soild = True)
                  self.map_dic[key] = t
                  self.map_dic[key].draw(screen)

               elif self.map_dic[key] == ENEMY:
                  if random.randint(0, 20) == 1:
                     e = enemy(["blob.png"],xPos,yPos,60,54,20)
                     enemy_list.append(e)
                     self.map_dic[key] = EMPTY
                  else:
                     self.map_dic[key] = EMPTY
               if self.map_dic[key] == EMPTY or (xPos == 0 and yPos == 0):
                     t = tile(["grass2.png"],xPos,yPos,58,58, soild = False)
                     if random.randint(0,2) == 2:
                        t = tile(["flower.png"],xPos,yPos,58,58, soild = False)
                     if random.randint(0,2) == 1:
                        t = tile(["grass.png"],xPos,yPos,58,58, soild = False)
                     self.map_dic[key] = t
                     self.map_dic[key].draw(screen)
              

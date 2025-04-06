import pygame
import random
from tile import tile
from enemy import enemy

class place:

   def __init__(self,map_list):
       self.map_dic = map_list

   def genKeyC(self, cell_x, cell_y):
       return cell_x + cell_y * 100000

   def genKeyP(self, x, y):
       return self.genKeyC(x // 50, y // 50)
    
   def create(self, screen, player, enemy_list):

      TREE   = 0
      ENEMY  = 1
      EMPTY  = 2

      for x in range(-5, 5):
         for y in range(-5, 5):
            
            map_x = x + player.x // 50
            map_y = y + player.y // 50
            key   = self.genKeyC(map_x, map_y)

            xPos = player.xPos + x * 50 - (player.x % 50)
            yPos = player.yPos + y * 50 - (player.y % 50)

            if key in self.map_dic:
               #self.map_dic[key].y = yPos
               #self.map_dic[key].x = xPos
               self.map_dic[key].draw(screen)

            else:
               self.map_dic[key] = random.randint(0, 2)
               if self.map_dic[key] == TREE:
                  t = tile(["tree.png"],xPos,yPos,50,50, stuff = "tree")
                  self.map_dic[key] = t
                  self.map_dic[key].draw(screen)

               elif self.map_dic[key] == ENEMY:
                  if random.randint(0, 20) == 1:
                     e = enemy(["blob.png"],xPos,yPos,60,54,20)
                     enemy_list.append(e)
                     self.map_dic[key] = EMPTY
                  else:
                     self.map_dic[key] = EMPTY
               if self.map_dic[key] == EMPTY:
                     t = tile(["grass.png"],xPos,yPos,50,50, stuff = "grass")
                     self.map_dic[key] = t
                     self.map_dic[key].draw(screen)
              

#!/usr/bin/env python3

import random
import pygame
from sprite         import sprite
from player         import player
from tool           import tool
from enemy          import enemy
from place          import place 
from screen         import screen
from invetory       import invetory
from maze           import Maze  
from corruptedEnemy import corruptedEnemy
from biome          import biome
from tileValues     import tileValues

width  = 580
height = 580

pygame.init()

screen = screen(width, height)

pygame.display.set_caption("linkLike")
clock = pygame.time.Clock()
keys  = []
Ex    = 50
Ey    = 50
a     = 0
noHit = True
die   = False
wepon = []
wep   = 1
first = True

ballList = []

grass      = tileValues(["grass.png"],False,True,58,58)
grass2     = tileValues(["grass2.png"],False,True,58,58)
flower     = tileValues(["flower.png"],False,True,58,58)
tree       = tileValues(["tree.png"],True,True,58,58)
rock       = tileValues(["rock.png","grass2.png","portal.png"],True,False,58,58)
sand       = tileValues(["sand.png"],False,True,58,58)
sand2      = tileValues(["sand2.png"],False,True,58,58)
sand3      = tileValues(["sand3.png"],False,True,58,58)
sandRocks  = tileValues(["sandRocks.png","sand2.png","sandportal.png"],True,False,58,58)

forest    = biome("forest",20,1,[[grass,0.2375],[grass2,0.2375],[flower,0.2375],[tree,0.2375],[rock,0.05]])
sand      = biome("sand",20,1,[[sand,0.3125],[sand2,0.3125],[sand3,0.3125],[sandRocks,0.0625]])
biomeList = [forest,sand]
invet      = invetory(0,"wood.png")
place      = place(biomeList)
spear      = tool(["spear.png"],-111,-111,180,30,90,50,5,1)
sheild     = tool(["sheild.png"],-100,-100,300,110,30,1,ratio = 0.5)
pickaxe    = tool(["pickaxe.png"],-110,-100,124,199,25,30,1)
war_hammar = tool(["battle_axe.png"],-100,-100,98,150,25,80,2.5)
battle_axe = tool(["battle_axe.png"],-100,-100,47,55,25,80,2.5)
axe        = tool(["axe.png"],-100,-100,57,79,1,2,45)
sword      = tool(["sword.png"],-111,-111,53,15,60,30,5,2.5)
wepon += [war_hammar,sword,pickaxe]
gob        = player(["gob.png","gobmove.png"],0,0,54,48,wepon,10,sheild,spear)
maze       = Maze(20,20)
test       = corruptedEnemy(["corruptedBlob.png","teleportCorrupt.png"],0,0,60,54,5)

enemy_list = []
for i in range(2):
   e = enemy(["blob.png","blobAttacking.png"],Ex,Ey,60,54,20)
   enemy_list.append(e)
   Ex = random.randint(0,450)
   Ey = random.randint(0,450)

running = True
while running:
   #hammer = pygame.image.load("war_hammar.png")
   #screen.blit(hammer,(100,100))
   a += 1   
   keys = pygame.key.get_pressed()

   screen.clear(gob.x, gob.y)
   if gob.inPortal(place):
      enemy_list = []
      maze.draw(screen,pickaxe)
      if first:
         maze.craftSpawn()
         first = False
   else:
      place.create(screen,gob,enemy_list,war_hammar,pickaxe,keys,invet,biomeList)

   gob.update(keys,screen,place,maze,invet,ballList)
   gob.weponChange(keys)
   gob.draw(screen)
   test.update(gob,screen,place,ballList)
   invet.open(screen,keys,gob,place,maze)
   invet.make(place,screen,gob)

   if len(ballList) > 0:
      for ball in ballList:
          ball.update(gob,screen)

   for enmy in enemy_list:
      for i in enemy_list:
         enmy.x += 1
         enmy.y += 1
         if enmy.isHit(i) and noHit:
            noHit = False
         enmy.x -= 2
         enmy.y -= 2
         if enmy.isHit(i) and noHit:
            noHit = False
         enmy.x += 1
         enmy.y += 1
      if  not noHit and not enmy.ha == 0 and not enmy.big:
         enmy.ha = 0
         i.ha = 0
         e = enemy(["blob.png","blobAttacking.png"],random.randint(0,500),random.randint(0,500),100,60,40,True)
         enemy_list.append(e)
      enmy.update(gob,noHit,enemy_list,keys,place,screen)
      noHit = True
      enmy.draw(screen)

   for event in pygame.event.get():
      if event.type == pygame.QUIT or gob.health <= 0:
         running = False
   if gob.health <= 0:
      running = False
   pygame.display.update()
   clock.tick(80)
pygame.quit()
     

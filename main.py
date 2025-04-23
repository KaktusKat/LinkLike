#!/usr/bin/env python3

import random
import pygame
from sprite import sprite
from player import player
from tool   import tool
from enemy  import enemy
from place import place 
from screen import screen

width  = 510
height = 510

pygame.init()

screen = screen(width, height)

pygame.display.set_caption("linkLike")
clock = pygame.time.Clock()
keys  = []
Ex    = 50
Ey    = 50
a     = 0
noHit = True
die = False
wepon = []
wep = 1
dic = {}

place      = place(dic)
war_hammar = tool(["battle_axe.png"],-100,-100,98,150,25,80,2.5)
battle_axe = tool(["battle_axe.png"],-100,-100,47,55,25,80,2.5)
axe        = tool(["axe.png"],-100,-100,57,79,1,2,45)
sword      = tool(["sword.png"],-111,-111,53,15,60,30,5,2.5)
wepon += [war_hammar,sword]
gob        = player(["gob.png","gobmove.png"],0,0,54,48,wepon)


enemy_list = []
for i in range(2):
   e = enemy(["blob.png"],Ex,Ey,60,54,20)
   enemy_list.append(e)
   Ex = random.randint(0,450)
   Ey = random.randint(0,450)

running = True
while running:
   hammer = pygame.image.load("war_hammar.png")
   #screen.blit(hammer,(100,100))
   a += 1   
   keys = pygame.key.get_pressed()

   screen.clear(gob.x, gob.y)
   place.create(screen,gob,enemy_list)

   gob.update(keys,screen,place)
   gob.weponChange(keys)
   gob.draw(screen)

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
         e = enemy(["blob.png"],random.randint(0,500),random.randint(0,500),100,60,40,True)
         enemy_list.append(e)
      enmy.update(gob,noHit,enemy_list,keys,place)
      noHit = True
      enmy.draw(screen)

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
   pygame.display.update()
   clock.tick(80)
pygame.quit()
     

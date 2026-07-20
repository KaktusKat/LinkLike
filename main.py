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
from cave           import Cave
from corruptedEnemy import corruptedEnemy
from biome          import biome
from item           import item
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
tileList = {}

spear      = tool(["spear.png"],-111,-111,180,30,90,50,5,1,name = "spear")
sheild     = tool(["sheild.png"],-100,-100,300,110,30,1,ratio = 0.5)
pickaxe    = tool(["pickaxe.png"],-110,-100,124,199,25,50,1)
fist       = tool(["fist.png"],-110,-100,50,100,50,30,1)
war_hammar = tool(["battle_axe.png"],-100,-100,98,150,25,80,2.5)
battle_axe = tool(["battle_axe.png"],-100,-100,47,55,25,80,2.5)
axe        = tool(["axe.png"],-100,-100,57,79,1,2,45)
sword      = tool(["sword.png"],-111,-111,53,15,60,30,5,2.5)
hammer     = tool(["hammer.png"],-100,-100,120,120,25,50,20)

rocks       = item(200,260,50,50,"rock","rock_invent.png",1)
flints      = item(300,200,50,50,"flint","flintInvent.png",1)
wood        = item(200,200,50,50,"wood","wood.png",1)
iron        = item(380,200,50,50,"iron","iron_invent.png",1)
empty       = item(-100,-100,0,0,"empty","wood.png",1)
refinedIron = item(200,320,50,50,"refinedIron","refinedIron.png",1)
sheildI     = item(200,200,50,50,"sheildI","sheildInvent.png",2)
spearI      = item(200,260,50,50,"spearI","spearInvent.png",2)
swordI      = item(300,200,50,50,"swordI","swordInvent.png",2)
pickaxeI    = item(380,200,50,50,"pickaxeI","pickaxeInvent.png",2)
axeI        = item(200,320,50,50,"axeI","axeInvent.png",2)
hammerI     = item(300,320,50,50,"hammerI","hammerInvent.png",2)
itemList    = [wood,rocks,iron,refinedIron,flints,sheildI,spearI,swordI,pickaxeI,axeI,hammerI]

grass      = tileValues(["grass.png"],False,True,58,58)
grass2     = tileValues(["grass2.png"],False,True,58,58)
flower     = tileValues(["flower.png"],False,True,58,58)
flint      = tileValues(["flints.png"],False,True,58,58,[[fist,1]],flints,[grass2])
stump      = tileValues(["stump.png"],False,True,58,58)
tree       = tileValues(["tree.png"],True,True,58,58,[[fist,4],[war_hammar,1]],wood,[stump])
portal     = tileValues(["portal.png"],False,True,58,58,portal = True)
rock       = tileValues(["rock.png"],True,False,58,58,[[pickaxe,1]],rocks,[grass2,portal])
sand       = tileValues(["sand.png"],False,True,58,58)
sand2      = tileValues(["sand2.png"],False,True,58,58)
sand3      = tileValues(["sand3.png"],False,True,58,58)
catus      = tileValues(["catus.png"],True,True,58,58)
sandPortal = tileValues(["sandportal.png"],False,True,58,58,portal = True)
sandRocks  = tileValues(["sandRocks.png"],True,False,58,58,[[pickaxe,1]],rocks,[sandPortal,sand2])

forest    = biome("forest",20,1,[[grass,1],[grass2,1],[flower,1],[flint,0.25],[tree,1],[rock,0.25]])
sand      = biome("sand",20,1,[[sand,1],[sand2,1],[sand3,1],[sandRocks,0.25]])
biomeList = [forest,sand]
invet     = invetory(0,"wood.png",itemList,empty)
place     = place(biomeList,wood,rocks,flints)
wepon    += [fist]
gob       = player(["gob.png","gobmove.png"],0,0,50,44,wepon,10,sheild,spear)
cave      = Cave(["caveBackground.png","caveBlock.png","ironOre.png"])
#test       = corruptedEnemy(["corruptedBlob.png","teleportCorrupt.png"],0,0,60,54,5)

sheildR    = [[["rock","wood","empty"],["rock","refinedIron","wood"],["rock","wood","empty"]],[sheildI,1],[gob.sheildC,sheild]]
spearR     = [[["empty","empty","empty"],["refinedIron","wood","wood"],["empty","empty","empty"]],[spearI,1],[gob.tool,spear]]
swordR     = [[["empty","empty","empty"],["flint","flint","wood"],["empty","empty","empty"]],[swordI,1],[gob.tool,sword]]
pickaxeR   = [[["flint","empty","empty"],["flint","wood","wood"],["flint","empty","empty"]],[pickaxeI,1],[gob.tool,pickaxe]]
axeR       = [[["flint","flint","empty"],["flint","wood","wood"],["empty","empty","empty"]],[axeI,1],[gob.tool,war_hammar]]
hammerR    = [[["flint","flint","empty"],["flint","wood","wood"],["flint","flint","empty"]],[hammerI,1],[gob.tool,hammer]]
refineR    = [[["iron","iron","empty"],["iron","iron","empty"],["empty","empty","empty"]],[refinedIron,1]]
craftRList = [sheildR,spearR,refineR,swordR,axeR,pickaxeR,hammerR]

enemy_list = []
for i in range(1):
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
      cave.update(screen,gob,pickaxe,iron)
   else:
      place.create(screen,gob,enemy_list,war_hammar,pickaxe,fist,keys,invet,biomeList)

   gob.update(keys,screen,place,cave,invet,ballList,enemy_list)
   gob.weponChange(keys)
   gob.draw(screen)
 #  test.update(gob,screen,place,ballList)
   invet.open(screen,keys,gob,place,cave,craftRList)
   invet.make(place,screen,gob)

   if len(ballList) > 0:
      for ball in ballList:
          ball.update(gob,screen)

   for enmy in enemy_list:
      for i in enemy_list:
    #     enmy.x += 1
     #    enmy.y += 1
         if enmy.isHit(i) and noHit:
            noHit = False
  #       enmy.x -= 2
   #      enmy.y -= 2
         if enmy.isHit(i) and noHit:
            noHit = False
#         enmy.x += 1
 #        enmy.y += 1
      if  not noHit and not enmy.ha == 0 and not enmy.big:
         enmy.ha = 0
         i.ha = 0
         e = enemy(["blob.png","blobAttacking.png"],random.randint(0,500),random.randint(0,500),100,60,40,True)
         enemy_list.append(e)
      enmy.update(gob,noHit,enemy_list,keys,place,screen)
      noHit = True
      enmy.draw(screen)

   gob.checkMoveE(enemy_list)
 
   gob.x += gob.velocityX
   gob.y += gob.velocityY

   for enemy in enemy_list:
       enemy.x += enemy.velocityX
       enemy.y += enemy.velocityY

   for event in pygame.event.get():
      if event.type == pygame.QUIT or gob.health <= 0:
         running = False
   if gob.health <= 0:
      running = False
   pygame.display.update()
   clock.tick(80)
pygame.quit()
     

#!/usr/bin/env python3

import pickle
import random
import pygame
import time
import sys
import copy
from sprite         import sprite
from player         import player
from slashF         import slashF
from stabF          import stabF
from meleeWeapon    import meleeWeapon
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

sys.setrecursionlimit(30000)

pygame.init()

screen = screen(width, height)

pygame.display.set_caption("linkLike")
clock = pygame.time.Clock()
keys     = []
Ex       = 50
Ey       = 50
a        = 0
noHit    = True
die      = False
wepon    = []
wep      = 1
first    = True
b        = 0
enemyHit = 0
load     = input("do you want to reload?")

ballList = []
tileList = {}

spear1     = stabF(["spear.png"],122,22,screen.images,20,10,4)
spear      = meleeWeapon(50,1.5,5,[spear1],50)

pickaxe1   = slashF(["pickaxeSwing.png","pickaxe.png"],124,199,screen.images,25,0.6,5)
pickaxe    = meleeWeapon(80,0.5,5,[pickaxe1],30)

fist1      = stabF(["fist.png"],50,100,screen.images,20,5,5)
fist       = meleeWeapon(40,0.2,5,[fist1],30)

axe1       = slashF(["battle_axeSwing.png","battle_axe.png"],98,150,screen.images,25,0.6,5)
war_hammar = meleeWeapon(80,1,5,[axe1],100)

sword1     = slashF(["swordSwing1.png","sword1.png"],136,180,screen.images,50,0.6,5)
sword2     = slashF(["swordSwing2.png","sword2.png"],136,180,screen.images,50,-0.6,5)
sword3     = stabF(["sword3.png"],160,30,screen.images,50,5,5)
sword      = meleeWeapon(50,1,5,[sword1,sword2,sword3],70)
 
hammer1    = slashF(["hammerSwing.png","hammer.png"],120,120,screen.images,25,0.6,5)
hammer     = meleeWeapon(75,1.5,40,[hammer1],1)

weaponList = {"hammer":hammer,"sword":sword,"axe":war_hammar,"fist":fist,"pickaxe":pickaxe,"spear":spear}

rocks       = item(177,267,50,50,screen.images,"rock","rock_invent.png",1)
flints      = item(267,177,50,50,screen.images,"flint","flintInvent.png",1)
wood        = item(177,177,50,50,screen.images,"wood","wood.png",1)
iron        = item(267,267,50,50,screen.images,"iron","iron_invent.png",1)
empty       = item(-100,-100,0,0,screen.images,"empty","empty.png",1)
refinedIron = item(177,357,50,50,screen.images,"refinedIron","refinedIron.png",1)
spearI      = item(177,267,50,50,screen.images,"spearI","spearInvent.png",2)
knifeI      = item(357,177,50,50,screen.images,"knifeI","throwingKnife.png",2)
swordI      = item(267,177,50,50,screen.images,"swordI","swordInvent.png",2)
pickaxeI    = item(267,267,50,50,screen.images,"pickaxeI","pickaxeInvent.png",2)
axeI        = item(177,357,50,50,screen.images,"axeI","axeInvent.png",2)
hammerI     = item(267,357,50,50,screen.images,"hammerI","hammerInvent.png",2)
itemList    = [wood,rocks,iron,refinedIron,flints,spearI,knifeI,swordI,pickaxeI,axeI,hammerI]

grass      = tileValues(["grass.png"],False,True,58,58,screen.images)
grass2     = tileValues(["grass2.png"],False,True,58,58,screen.images)
flower     = tileValues(["flower.png"],False,True,58,58,screen.images)
flint      = tileValues(["flints.png"],False,True,58,58,screen.images,[["fist",1]],flints,[grass2])
stump      = tileValues(["stump.png"],False,True,58,58,screen.images)
tree       = tileValues(["tree.png"],True,True,25,30,screen.images,[["fist",4],["axe",1]],wood,[stump])
portal     = tileValues(["portal.png"],False,True,58,58,screen.images,portal = True)
rock       = tileValues(["rock.png"],True,False,20,20,screen.images,[["pickaxe",1]],rocks,[grass2,portal])
GCD        = tileValues(["grassCD.png"],False,True,58,58,screen.images)
GCD2       = tileValues(["grassCD2.png"],False,True,58,58,screen.images)
sand       = tileValues(["sand.png"],False,True,58,58,screen.images)
sand2      = tileValues(["sand2.png"],False,True,58,58,screen.images)
sand3      = tileValues(["sand3.png"],False,True,58,58,screen.images)
catus      = tileValues(["catus.png"],True,True,58,58,screen.images)
sandPortal = tileValues(["sandportal.png"],False,True,58,58,screen.images,portal = True)
sandRocks  = tileValues(["sandRocks.png"],True,False,20,20,screen.images,[["pickaxe",1]],rocks,[sandPortal,sand2])

forest    = biome("forest",20,1,[[grass,1],[grass2,1],[flower,1],[flint,0.25],[tree,0.25],[rock,0.25]],[GCD,GCD2])
sand      = biome("sand",20,1,[[sand,1],[sand2,1],[sand3,1],[sandRocks,0.25]],[GCD,GCD2])
biomeList = [forest,sand]
biomeDict = {"forest":forest,"sand":sand}
invet     = invetory(0,"wood.png",itemList,empty,screen.images)
place     = place(biomeList,wood,rocks,flints)
wepon    += ["fist","axe"]
gob       = player(["gob.png","gobWalk.png","gobWalk2.png","gobHurt.png","gobIframes.png","gobRoll.png"],0,0,50,44,screen.images,wepon,10,spear)
cave      = Cave(["caveBackground.png","caveBlock.png","ironOre.png"],screen.images)
#test       = corruptedEnemy(["corruptedBlob.png","teleportCorrupt.png"],0,0,60,54,5)

enemy_list = []
for i in range(1):
   e = enemy(["blob.png","blobM.png","blobAttacking.png","blobHurt.png"],Ex,Ey,60,54,screen.images,12)
   enemy_list.append(e)
   Ex = random.randint(0,450)
   Ey = random.randint(0,450)

if load == "yes":
   with open("save.plk","rb") as file:
      load       = pickle.load(file)
      gob        = load[0]
      invet      = load[1]
      place      = load[2]
      cave       = load[3]
      enemy_list = load[4]
      for i in range(len(itemList)):
          itemList[i]          = load[i+3]

spearR     = [[["empty","empty","empty"],["refinedIron","wood","wood"],["empty","empty","empty"]],[spearI,1],[gob.tool,"spear"]]
swordR     = [[["empty","empty","empty"],["flint","flint","wood"],["empty","empty","empty"]],[swordI,1],[gob.tool,"sword"]]
pickaxeR   = [[["flint","empty","empty"],["flint","wood","wood"],["flint","empty","empty"]],[pickaxeI,1],[gob.tool,"pickaxe"]]
axeR       = [[["flint","flint","empty"],["flint","wood","wood"],["empty","empty","empty"]],[axeI,1],[gob.tool,"axe"]]
hammerR    = [[["flint","flint","empty"],["flint","wood","wood"],["flint","flint","empty"]],[hammerI,1],[gob.tool,"hammer"]]
refineR    = [[["iron","iron","empty"],["iron","iron","empty"],["empty","empty","empty"]],[refinedIron,1]]
craftRList = [spearR,refineR,hammerR,axeR,swordR,pickaxeR]


running = True
while running:
   keys = pygame.key.get_pressed()
   if keys[pygame.K_t]:
      with open("save.plk","wb") as file:
         saveList = [gob,invet,place,cave,enemy_list]
         for item in itemList:
             saveList.append(item)
         pickle.dump(saveList,file)
   enemyHit -= 1
   b += 1 
   a += 1   

   screen.clear(gob.x, gob.y)
   if gob.inPortal(place):
      enemy_list = []
      cave.update(screen,gob,pickaxe,iron)
   else:
      place.create(screen,gob,enemy_list,war_hammar,pickaxe,fist,keys,invet,biomeList,biomeDict,weaponList)

   gob.update(keys,screen,place,cave,invet,ballList,enemy_list,weaponList)
   gob.draw(screen)
   gob.weponChange(keys)
 #  test.update(gob,screen,place,ballList)

   if len(ballList) > 0:
      for ball in ballList:
          ball.update(gob,screen)

   hit = False
   for enmy in enemy_list:
      enmy.update(gob,noHit,enemy_list,keys,place,screen,weaponList)
      enmy.velocityX *= 0.95
      enmy.velocityY *= 0.95
      if enmy.iFrames:
         hit = True
         enmy.iFrames     = False
         enmy.image_index = 3
      enmy.draw(screen)
      enmy.checkMoveE(enemy_list,screen)
   if hit and enemyHit < 0:
      enemyHit = 50
      pygame.display.update()
      time.sleep(0.15)

   invet.open(screen,keys,gob,place,cave,craftRList)
   invet.make(place,screen,gob)

   if gob.roll < 0:
      gob.checkMoveE(enemy_list,screen)
   if gob.inMaze:
      gob.checkMoveM(cave,screen)
   if not gob.inMaze:
      gob.checkMove(place,screen)

   
   gob.x += gob.velocityX
   gob.y += gob.velocityY
   gob.velocityX *= 0.95
   gob.velocityY *= 0.95

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
     

import pygame
import copy
import numpy as np
import math
from placeObject import placeObject
from tileO        import tileO

class structure:
   def __init__(self,roomList,rartiy):
      self.roomList = roomList
      self.rarity   = rartiy
      self.rectList = []
      self.roomHitL = []
      self.addx     = 0

   def place(self,images,place,xPos,yPos,biomeList,roomNum,xA = 1,yA = 1):
      x    = 0
      y    = 0
      if self.roomList[roomNum] == []:
         return
      w     = (len(self.roomList[roomNum][0]) * 58)
      h     = (len(self.roomList[roomNum])    * 58)
      xPosC = xPos
      yPosC = yPos
      if xA == -1:
         xPosC = xPos - w + 58
      if yA == -1:
         yPosC = yPos - h + 58
      for room in self.roomHitL:
         self.addx += 15
         self.rectList.append([xPosC,yPosC,w,h])
         if self.isHit([xPosC,yPosC,w,h],room):
            return
      for a in range(len(self.roomList[roomNum])):
         if yA == -1:
            i = self.roomList[roomNum][len(self.roomList[roomNum])-a-1]
         else:
            i = self.roomList[roomNum][a]
         for tileVLL in range(len(i)):
            if xA == -1:
               tileVL = i[len(i)-tileVLL-1]
            else:
               tileVL = i[tileVLL]
            tileV = tileVL[0]
            xK    = x + xPos//58
            yK    = y + yPos//58
            key   = place.genKeyC(xK,yK)
            In    = False
            if key in place.map_dic2:
               tileL2 = place.map_dic2[key]
            else:
               place.map_dic[key]  = tileO(["grass2.png"],xPos+x*58,yPos+y*58,58,58,images,[[0,0,58,58]],False,biomeList,justMade = True)
               place.map_dic2[key] = tileO(["tree.png"],xPos+x*58,yPos+y*58,58,58,images,[[0,0,58,58]],False,biomeList,justMade = True)
               tileL2 = place.map_dic2[key]
            if type(tileV) is placeObject:
               tileV.change(place,key,images,biomeList)
            else:
               tileL2.soild     = tileV.soild
               tileL2.image     = tileV.image
               tileL2.chestList = copy.deepcopy(tileV.chestList)
               tileL2.toolList  = tileV.toolList
               tileL2.bounce    = tileV.bounce
               tileL2.noise     = tileV.noise
               tileL2.item      = tileV.item
               tileL2.change    = tileV.change
               tileL2.w         = tileV.w
               tileL2.h         = tileV.h
               tileL2.made      = True
               tileL2.bounce    = tileV.bounce
               tileL2.portal    = tileV.portal
            if len(tileVL) >= 2:
               Mx     = math.ceil(i.index(tileVL)/len(i))*2-1
               My     = math.ceil(self.roomList[roomNum].index(i)/len(self.roomList[roomNum]))*2-1
               struct = np.random.choice(tileVL[1],p = tileVL[1][0].probList)
               self.place(images,place,xPos+struct.List[1],yPos+struct.List[2],biomeList,struct.List[0],Mx,My)
            x += xA
         y += yA
         x  = 0
      self.roomHitL.append([xPosC,yPosC,w,h])


   def isHit(self,room1,room2):
      room1TopX = room1[0]+room1[2]
      room1TopY = room1[1]+room1[3]

      room2TopX = room2[0]+room2[2]
      room2TopY = room2[1]+room2[3]

      return (room2[0] < room1TopX) and (room2TopX > room1[0]) and \
             (room2[1] < room1TopY) and (room2TopY > room1[1])



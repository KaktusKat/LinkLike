import pygame

class invetory:
   def __init__(self,woodNum,wood):
      self.woodNum     = woodNum
      self.window      = False
      self.wood        = pygame.image.load(wood)
      self.wood        = pygame.transform.scale(self.wood,(50,50))
      self.sheild      = pygame.image.load("sheildInvent.png")
      self.sheild      = pygame.transform.scale(self.sheild,(50,40))
      self.crafter     = pygame.image.load("craft.png")
      self.crafter     = pygame.transform.scale(self.sheild,(100,100))
      self.spike       = pygame.image.load("spikeInvent.png")
      self.spike       = pygame.transform.scale(self.spike,(50,50))
      self.spear       = pygame.image.load("spearInvent.png")
      self.spear       = pygame.transform.scale(self.spear,(7,50))
      self.placeBlock  = 0
      self.place       = False
      self.timer       = 0
      self.table       = False
      self.holding     = ["none",0]
      self.first       = True
      self.Rlistx      = []
      self.Rlisty      = []
      self.craftList   = []
      self.craftPickUp = [[0,0]]
      self.craftTable  = [[[[0,0]],[[0,0]],[[0,0]]],[[[0,0]],[[0,0]],[[0,0]]],[[[0,0]],[[0,0]],[[0,0]]]]

   def open(self,screen,keys,player,place,maze):
       if keys[pygame.K_q] or self.window or self.table:
          pygame.draw.rect(screen.screen,(81,74,74),(screen.width/2 - 150,screen.height/2 - 150,300,300))
          self.window = True
          self.craft(screen,player,place,maze)
          if player.table:
             self.table = True
       if keys[pygame.K_c]:
          self.window = False
          self.table  = False

   def craft(self,screen,player,place,maze):
      print(self.craftList)
      self.woodNum = place.treesCut
      num          = pygame.font.SysFont("I don't think this dose anything",40)
      num          = num.render(f"{self.woodNum}",False,(0,0,0))
      screen.blit(num,-40+player.x,-40+player.y)
      screen.blit(self.wood,-90+player.x,-90+player.y)
      rocks = pygame.image.load("rock_invent.png")
      rocks = pygame.transform.scale(rocks,(50,50))
      num2  = pygame.font.SysFont("I don't think this dose anything",40)
      num2  = num2.render(f"{place.rocksBrocken}",False,(0,0,0))
      screen.blit(num2,-40+player.x,10+player.y)
      screen.blit(rocks,-90+player.x,-30+player.y)
      num3  = pygame.font.SysFont("I don't think this dose anything",40)
      num3  = num3.render(f"{maze.spikes}",False,(0,0,0))
      screen.blit(num3,90+player.x,-40+player.y)
      screen.blit(self.spike,90+player.x,-90+player.y)
      num4  = pygame.font.SysFont("I don't think this dose anything",15)
      num4  = num4.render(f"crafted:",False,(0,0,0))
      screen.screen.blit(num4,(320,320))
      if not self.craftList == []:
         y = 0
         for item in self.craftList:
            y+=15
            num4  = pygame.font.SysFont("I don't think this dose anything",15)
            num4  = num4.render(item,False,(0,0,0))
            screen.screen.blit(num4,(320,320+y))
      Mpos               = pygame.mouse.get_pos()
      Mpressed           = pygame.mouse.get_pressed()
      place.treesCut, place.rocksBrocken, maze.spikes = self.pickUp(50,50,place,maze,player,[[place.treesCut,["wood",self.wood],-90,-90],[place.rocksBrocken,["rock",rocks],-90,-30],[maze.spikes,["spike",self.spike],90,-90]])
      if not self.holding[0] == "none":
         screen.blit(pygame.transform.scale(self.holding[1],(25,25)),Mpos[0]-290+player.x,Mpos[1]-290+player.y) 
      if self.table:
         for x in range(3):
            for y in range(3):    
               pygame.draw.rect(screen.screen,(0,0,0),pygame.Rect(x*50,y*50,50,50),5)
               if self.first:
                  self.Rlistx.append(x*50)
                  self.Rlisty.append(y*50)
         self.first = False
         X = -1
         Y = -1
         for y in range(3):
            for x in range(3):
               X += 1
               Y += 1
               craftTable  = self.placeItem(self.Rlistx[X],self.Rlisty[Y],50,50,player,[["wood",self.wood],["rock",rocks],["spike",self.spike]])
               if len(craftTable) == 5:
                  self.craftTable[y][x] = craftTable
         for y in range(len(self.craftTable)):
            for x in range(len(self.craftTable[y])):
               if len(self.craftTable[y][x]) == 5:
                  screen.screen.blit(pygame.transform.scale(self.craftTable[y][x][0][1],(40,40)),(self.craftTable[y][x][1]+5,self.craftTable[y][x][2]+5))
                  self.craftTable[y][x] = self.pickUpCraft(50,50,place,maze,player,[self.craftTable[y][x][0],self.craftTable[y][x][0],self.craftTable[y][x][1],self.craftTable[y][x][2]],self.craftTable[y][x])
         pygame.draw.rect(screen.screen,(0,0,0),pygame.Rect(200,50,50,50),5)
         if not self.craftPickUp == [[0,0]]:
            screen.screen.blit(pygame.transform.scale(self.craftPickUp[0][1],(40,40)),(self.craftPickUp[1],self.craftPickUp[2]))
            self.craftPickUp = self.pickUpCraft(50,50,place,maze,player,[self.craftPickUp[0],self.craftPickUp[0],self.craftPickUp[1],self.craftPickUp[2]],self.craftPickUp,True,True,self.craftPickUp[0][0])
         if not self.carftMake([["rock","wood","wood"],["rock","spike","wood"],["rock","wood","wood"]],[["sheild",self.sheild],205,60],player,screen) == [[0,0]]:
            self.craftPickUp = self.carftMake([["rock","wood","wood"],["rock","spike","wood"],["rock","wood","wood"]],[["sheild",self.sheild],205,60],player,screen)
         if not self.carftMake([[0,0,0],["spike","wood","wood"],[0,0,0]],[["spear",self.spear],205,60],player,screen) == [[0,0]]:
            self.craftPickUp = self.carftMake([[0,0,0],["spike","wood","wood"],[0,0,0]],[["spear",self.spear],205,60],player,screen)
         
   def make(self,place,screen,player):
      self.timer  -= 1 
      x,y          = pygame.mouse.get_pos()
      Mpress       = pygame.mouse.get_pressed()
      if (Mpress[2] and place.treesCut < 0 and self.timer < 1 and not player.inMaze):
         image = pygame.image.load("woodPlanks.png")
         x,y   = screen.convertSTW(x,y)
         key   = place.genKeyP(x,y)
         place.map_dic[key].image[0] = pygame.transform.scale(image,(58,58))
         place.map_dic[key].soild    = True
         place.treesCut -= 1
         self.timer = 20

   def pickUp(self,w,h,place,maze,player,items):
      Mpos     = pygame.mouse.get_pos()
      Mpressed = pygame.mouse.get_pressed()
      hit      = False
      holding  = ""
      count    = []
      for item in items:
         if Mpressed[0] and player.isHitXYXY(Mpos[0],Mpos[1],1,1,item[2]+290,item[3]+290,w,h):
            if item[0] > 0 and not self.holding[0] == item[1][0]:
               holding  = item[1]
               item[0] -= 1
               hit      = True
         count.append(item[0])
      if not self.holding[0] == "none" and hit:
         if self.holding[0] == "rock":
             items[1][0] += 1
         elif self.holding[0] == "wood":
             items[0][0] += 1
         elif self.holding[0] == "spike":
             items[2][0] += 1
         count[0] = items[0][0]
         count[1] = items[1][0]
         count[2] = items[2][0]
      if hit:
         self.holding = holding
      return count[0],count[1],count[2]

   def pickUpCraft(self,w,h,place,maze,player,item,items,craft = False,addList = False,crafted = 0):
      Mpos     = pygame.mouse.get_pos()
      Mpressed = pygame.mouse.get_pressed()
      hit      = False
      holding  = ""
      if Mpressed[2] and player.isHitXYXY(Mpos[0],Mpos[1],1,1,item[2],item[3],w,h):
         if not self.holding[0] == item[1][0]:
            holding  = item[1]
            items    = [[0,0]]
            hit      = True
      if not self.holding[0] == "none" and hit:
         if self.holding[0] == "rock":
             place.rocksBrocken += 1
         elif self.holding[0] == "wood":
             place.treesCut += 1
         elif self.holding[0] == "spike":
             maze.spikes += 1
      if hit:
         self.holding = holding
         if craft:
            if addList:
               self.craftList.append(crafted)
            self.craftTable  = [[[[0,0]],[[0,0]],[[0,0]]],[[[0,0]],[[0,0]],[[0,0]]],[[[0,0]],[[0,0]],[[0,0]]]]
      return items

   def placeItem(self,x,y,w,h,player,items):
      Mpos   = pygame.mouse.get_pos()
      Mpress = pygame.mouse.get_pressed()
      for item in items:
         if Mpress[0] and player.isHitXYXY(Mpos[0],Mpos[1],1,1,x,y,w,h) and self.holding[0] == item[0]:
            self.holding = ["none",0]
            return [item,x,y,w,h]
      return []

   def carftMake(self,recpie,outcome,player,screen):
      for y in range(3):
         for x in range(3):
            if not recpie[y][x] == self.craftTable[y][x][0][0]:
               print("no")
               return [[0,0]]
      return outcome

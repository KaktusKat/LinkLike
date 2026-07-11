import pygame

class invetory:
   def __init__(self,woodNum,wood,itemList,empty):
      self.woodNum     = woodNum
      self.window      = False
      self.wood        = pygame.image.load(wood)
      self.wood        = pygame.transform.scale(self.wood,(50,50))
      self.sheild      = pygame.image.load("sheildInvent.png")
      self.sheild      = pygame.transform.scale(self.sheild,(50,40))
      self.crafter     = pygame.image.load("craft.png")
      self.crafter     = pygame.transform.scale(self.sheild,(100,100))
      self.iron        = pygame.image.load("iron_invent.png")
      self.iron        = pygame.transform.scale(self.iron,(50,50))
      self.spear       = pygame.image.load("spearInvent.png")
      self.spear       = pygame.transform.scale(self.spear,(7,50))
      self.placeBlock  = 0
      self.place       = False
      self.timer       = 0
      self.table       = False
      self.holding     = ["none",0]
      self.first       = True
      self.itemList    = itemList
      self.Rlistx      = []
      self.Rlisty      = []
      self.craftList   = []
      self.empty       = empty
      self.craftPickUp = [[0,0]]
      self.craftTable  = []
      self.pageNum     = 1
      self.maxPage     = 0
      for item in itemList:
          if self.maxPage < item.pageNum:
             self.maxPage = item.pageNum
      for x in range(3):
         self.craftTable.append([])
         for y in range(3):
            self.craftTable[x].append([empty,580-x*50,580-y*50])

   def open(self,screen,keys,player,place,maze,craftRList):
       if keys[pygame.K_q] or self.window or self.table:
          pygame.draw.rect(screen.screen,(81,74,74),(screen.width/2 - 150,screen.height/2 - 150,300,300))
          self.window = True
          self.craft(screen,player,place,maze,craftRList,keys)
          if player.table:
             self.table = True
       if keys[pygame.K_c]:
          self.window = False
          self.table  = False

   def craft(self,screen,player,place,maze,craftRList,keys):
      for item in self.itemList:
         if item.pageNum == self.pageNum:
            num          = pygame.font.SysFont("I don't think this dose anything",40)
            num          = num.render(f"{item.amount}",False,(0,0,0))
            screen.screen.blit(num,(item.x+item.w,item.y+item.h))
            screen.screen.blit(item.image,(item.x,item.y))
      if not self.craftList == []:
         y = 0
         for item in self.craftList:
            y+=15
            num4  = pygame.font.SysFont("I don't think this dose anything",15)
            num4  = num4.render(item,False,(0,0,0))
            screen.screen.blit(num4,(320,320+y))
      Mpos               = pygame.mouse.get_pos()
      Mpressed           = pygame.mouse.get_pressed()
      self.pickUp(50,50,place,maze,player,self.itemList)
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
               craftTable  = self.placeItem(self.Rlistx[X],self.Rlisty[Y],50,50,player,self.itemList)
               if not craftTable == "bob":
                  self.craftTable[y][x] = craftTable

         for y in range(len(self.craftTable)):
            for x in range(len(self.craftTable[y])):
               if not self.craftTable[y][x] == [[0,0]]:
                  newImg = pygame.transform.scale(self.craftTable[y][x][0].image,(40,40))
                  screen.screen.blit(newImg,(self.craftTable[y][x][1]+5,self.craftTable[y][x][2]+5))
                  self.craftTable[y][x] = self.pickUpCraft(50,50,place,maze,player,self.craftTable[y][x])
         pygame.draw.rect(screen.screen,(0,0,0),pygame.Rect(200,50,50,50),5)

         if keys[pygame.K_l]:
            if not self.pageNum == self.maxPage:
               self.pageNum += 1
         if keys[pygame.K_k]:
            if not self.pageNum == 1:
               self.pageNum -= 1

         for craftR in craftRList:
            if len(craftR) == 3:
               self.craftPickUp = self.carftMake(craftR[0],craftR[1],player,screen,craftR[2])
            if len(craftR) == 2:
               self.craftPickUp = self.carftMake(craftR[0],craftR[1],player,screen)
         
   def make(self,place,screen,player):
      self.timer  -= 1 
#      x,y          = pygame.mouse.get_pos()
 #     Mpress       = pygame.mouse.get_pressed()
  #    if (Mpress[2] and place.treesCut < 0 and self.timer < 1 and not player.inMaze):
   #      image = pygame.image.load("woodPlanks.png")
    #     x,y   = screen.convertSTW(x,y)
     #    key   = place.genKeyP(x,y)
      #   place.map_dic[key].image[0] = pygame.transform.scale(image,(58,58))
       #  place.map_dic[key].soild    = True
        # place.treesCut -= 1
         #self.timer = 20

   def pickUp(self,w,h,place,maze,player,items):
      Mpos     = pygame.mouse.get_pos()
      Mpressed = pygame.mouse.get_pressed()
      hit      = False
      holding  = ""
      count    = []
      for item in items:
         if Mpressed[0] and player.isHitXYXY(Mpos[0],Mpos[1],1,1,item.x,item.y,item.w,item.h):
            if item.amount > 0 and not self.holding[0] == item.name and self.pageNum == item.pageNum:
               holding      = [item.name,item.image]
               item.amount -= 1
               hit          = True
      if not self.holding[0] == "none" and hit:
         for item in items:
            if self.holding[0] == item.name:
               item.amount += 1
      if hit:
         self.holding = holding

   def pickUpCraft(self,w,h,place,maze,player,item,craft = False,addList = False,crafted = 0):
      Mpos     = pygame.mouse.get_pos()
      Mpressed = pygame.mouse.get_pressed()
      hit      = False
      holding  = ""
      if Mpressed[2] and player.isHitXYXY(Mpos[0],Mpos[1],1,1,item[1],item[2],item[0].w,item[0].h):
         if not self.holding[0] == item[0].name:
            holding  = [item[0].name,item[0].image]
            item     = [self.empty,item[1],item[2]]
            hit      = True
      if not self.holding[0] == "none" and hit:
         for items in self.itemList:
            if self.holding[0] == items.name:
               items.amount += 1
      if hit:
         self.holding = holding
      return item

   def placeItem(self,x,y,w,h,player,items):
      Mpos   = pygame.mouse.get_pos()
      Mpress = pygame.mouse.get_pressed()
      for item in items:
         if Mpress[0] and player.isHitXYXY(Mpos[0],Mpos[1],1,1,x,y,w,h) and self.holding[0] == item.name:
            self.holding = ["none",0]
            return [item,x,y]
      return "bob"

   def carftMake(self,recpie,outcome,player,screen,wepon = [[],1]):
      for y in range(3):
         for x in range(3):
            if not recpie[y][x] == self.craftTable[y][x][0].name:
               return [[0,0]]
      outcome[0].amount  += outcome[1]
      wepon[0].append(wepon[1])
      self.craftTable  = []
      for x in range(3):
         self.craftTable.append([])
         for y in range(3):
            self.craftTable[x].append([self.empty,580-x*50,580-y*50])


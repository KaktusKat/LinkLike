import tile

class tileC(tile):
   def __init__(self,img,posX,posY,w,h,images,soild):
      super().__init__(img,posX,posY,w,h,images,soild)
      self.reducedNoise = False
      self.type         = 0
      self.iron         = False
      self.nextTo       = []

   def randomPlace(self,img1,img2):
      if random.randint(0,1) == 1:
         self.type  = "wall"
         self.image = [img1]
         self.soild = True
      else:
        self.type  = "empty"
        self.image = [img2]
        self.soild = False

   def nebiors(self,tileList,width):
      posList     = [self.x//29,self.y//29]
      posList     = [int(posList[0]),int(posList[1])]
      self.nextTo = []
      for x in range(-1,2):
         for y in range(-1,2):
            self.nextTo.append(tileList[(posList[0]+x)][(posList[1]+y)])

   def reduceNoise(self,backG,block,blocks):
      numWall  = 0
      numEmpty = 0
      for tile in self.nextTo:
         if tile.type == "wall":
           numWall += 1
         else:
           numEmpty += 1
      self.type   = "empty"
      self.image  = [backG]
      self.soild  = False
      if numWall >= 5:
         self.type   = "wall"
         a           = np.random.choice(blocks,p = [0.95,0.05])
         self.soild  = True
         if a == "stone":
            self.image = [block[0]]
         else:
            self.image = [block[1]]
            self.iron  = True


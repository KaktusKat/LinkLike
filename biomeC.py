from biome import biome

class biomeC(biome):
   def __init__(self,name,maxMin,images1,images2,structures):
      super().__init__(name,maxMin,images1[0],images2[0],structures)
      self.images1W = []
      self.images2W = []
      self.prob1W   = []
      self.prob2W   = []
      total           = 0
      for img in images1[1]:
         self.images1W.append(img[0])
         total += img[1]
      for img in images1[1]:
         self.prob1W.append(img[1]/total)
      total           = 0
      for img in images2[1]:
         self.images2W.append(img[0])
         total += img[1]
      for img in images2[1]:
         self.prob2W.append(img[1]/total)
      

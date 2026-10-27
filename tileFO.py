from tileF import tileF
from tileO import tileO

class tileFO(tileF,tileO):
   def __init__(self,img,posX,posY,w,h,images,hitBoxL,soild,biomes,fenceO,justMade = True):
      super().__init__(img=img,posX=posX,posY=posY,w=w,h=h,images=images,hitBoxL=hitBoxL,solid=soild,biomes=biomes,justMade=justMade,fenceO=fenceO)
      

import math
import random

class perlinNoise:
   def __init__(self,scale,w,h):
      self.scale    = scale
      self.gradient = []
      for x in range(w//scale + 2):
         self.gradient.append([])
         for y in range(h//scale + 2):
            angle = random.uniform(0,2*math.pi)
            self.gradient[x].append((math.cos(angle),math.sin(angle)))

   def dot(self,a,b):
      return a[0] * b[0] + a[1] * b[1]

   def fade(self,a):
      return 6 * a ** 5 - 15 * a ** 4 + 10 * a ** 3

   def lerp(self,a,b,c):
      return (b - a) * c + a

   def lerp2D(self,corner1,corner2,corner3,corner4,value):
      top    = self.lerp(corner1,corner2,value[0])
      bottom = self.lerp(corner3,corner4,value[0])
      return self.lerp(top,bottom,value[1])

   def value(self,x,y):
      iX     = int(x//self.scale)
      iY     = int(y//self.scale)
      niX    = x/self.scale-iX
      niY    = y/self.scale-iY

      corner1 = self.dot(self.gradient[iX]  [iY],  (niX,  niY))
      corner2 = self.dot(self.gradient[iX+1][iY],  (niX-1,niY))
      corner3 = self.dot(self.gradient[iX]  [iY+1],(niX,  niY-1))
      corner4 = self.dot(self.gradient[iX+1][iY+1],(niX-1,niY-1))

      return self.lerp2D(corner1,corner2,corner3,corner4,(self.fade(niX),self.fade(niY)))


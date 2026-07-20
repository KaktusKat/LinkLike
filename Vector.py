import math

class Vector:
   def __init__(self, v = None):
      if v:
         self.x, self.y = v
      else:
         self.x = 0.0
         self.y = 0.0

   def __add__(self, other):
      return Vector((self.x + other.x, self.y + other.y))

   def __sub__(self, other):
      return Vector((self.x - other.x, self.y - other.y))

   def __neg__(self):
      return Vector((-self.x,-self.y))

   def __matmul__(self, other):
      return Vector((self.x*other.x, self.y*self.y*other.y))

   def __getitem__(self,index):
       if index == 0:
          return self.x
       elif index == 1:
          return self.y
       else:
          raise IndexError

   def __len__(self):
       return 2

   def __str__(self):
        return f"({self.x:5.2f}, {self.y:5.2f})"

   def magn(self):
       return math.sqrt(self.x*self.x + self.y*self.y)

import random
import pygame
from tile import tile

class Maze:

   def path(x, y):
      return tile(["grass.png"],x*70,y*70,70,70, soild = False)

   def wall(x, y):
      if random.randint(0,10) == 10:
         return tile(["spike.png"],x*70,y*70,70,70, soild = True,breakable = False, spike = True)
      return tile(["caveWall.png"],x*70,y*70,70,70, soild = True,breakable = False)

   def get_cell(self, x, y):
      if x < 0 or x >= self.width or y < 0 or y >= self.height:
         return None
      return self.map[y][x]

   def __init__(self, width, height, complexity = 0.75, density = 0.75):

      # Ensure width and height are odd
      self.width      = (width // 2) * 2 + 1
      self.height     = (height // 2) * 2 + 1
      self.complexity = complexity
      self.density    = density
      self.spikes     = 0

      self.clear()
      self.boundary()
      self.generate()

   def draw(self,screen,tool):
      """ print map on the console """
      for row in self.map:
         for cell in row:
           cell.draw(screen)
           if cell.spike and tool.attacking and cell.isHit(tool):
              cell.spike   = False
              img          = pygame.image.load("caveWall.png")
              cell.image   = [pygame.transform.scale(img,(70,70))]
              self.spikes += 1
 
   def print(self):
      """ print map on the console """
      for row in self.map:
         for cell in row:
            print(cell, end='')
         print('')

   def build(self, x, y):
      self.map[y][x] = Maze.wall(x, y)

   def is_path(self, x, y):
      return not self.map[y][x].soild

   def clear(self):
      """ reset to an empty map """
      self.map = []
      for y in range(self.height):
          row = []
          for x in range(self.width):
             row.append(Maze.path(x, y))
          self.map.append(row)

   def boundary(self):
      """ build boundary wall """

      for x in range(self.width):
         self.build(x, 0)
         self.build(x, self.height - 1)

      for y in range(self.height):
         self.build(0, y)
         self.build(self.width - 1, y)

   def generate(self):
      """ generate a random maze using prims algorithm """

      scaled_complexity = 5 * self.complexity * (self.width + self.height)
      scaled_density    = self.density * (self.width // 2) * (self.height // 2)

      for i in range(int(scaled_density)):

         x = random.randint(0, (self.width  // 2) - 1) * 2
         y = random.randint(0, (self.height // 2) - 1) * 2

         self.build(x, y)

         for j in range(int(scaled_complexity)):

            neighbours = []

            if x > 1:
               neighbours.append((x - 2, y))
            if x < (self.width - 2):
               neighbours.append((x + 2, y))
            if y > 1:
               neighbours.append((x, y - 2))
            if y < (self.height - 2):
               neighbours.append((x, y + 2))

            if neighbours != []:

               index  = random.randint(0, len(neighbours) - 1)
               nx, ny = neighbours[index]

               if self.is_path(nx, ny):
                  self.build(nx, ny)
                  self.build(nx + (x - nx) // 2, ny + (y - ny) // 2)
                  x = nx
                  y = ny

   def craftSpawn(self):
      spawning = True
      while spawning:
         craft = self.get_cell(0,0)
         if craft.soild:
            image = pygame.image.load("craft.png")
            craft.image = [pygame.transform.scale(image,(craft.w,craft.h))]
            craft.craft = True
            spawning = False

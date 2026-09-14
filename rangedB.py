import enemy
import pygame

class rangedB(enemy):
   def __init__(self,img,x,y,w,h,images,sound,hitS,attackS,ha,item,projectile):
      super().__init__(img,x,y,w,h,images,sound,hitS,ha,item)
      self.projectile = projectile
      self.attackS    = sound.load(attackS)

   def update(

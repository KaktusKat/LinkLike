class weapon:
   def __init__(self,Aspeed,damage,kback):
      self.Aspeed      = Aspeed
      self.damage      = damage
      self.kback       = kback
      self.AspeedTimer = 0
      self.attacking   = False
      self.attackTimer = 30
      self.x           = 0
      self.y           = 0
      self.w           = 0
      self.h           = 0

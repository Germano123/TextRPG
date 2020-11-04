class Tower:
  def __init__(self, name, cost):
    self.__name = name
    self.__level = 1
    self.__exp = 0
    self.__cost = cost

  def Get_Name(self):
    return self.__name

  def Get_Level(self):
    return self.__level

  def Get_Exp(self):
    return self.__exp

  def Get_Cost(self):
    return self.__cost

  def __LevelUp(self):
    self.__level += 1
  
  def AddExp(self, exp):
    self.__exp += exp
    if(self.__exp >= self.__level * 10):
      self.__LevelUp()
class Item:
    def __init__(self, name, stack, quantity = 0):
        self.__name = name
        self.__stack = stack
        self.__quantity = quantity
    
    def Get_Name(self):
        return self.__name

    def Get_Stack(self):
        return self.__stack

    def Get_Quantity(self):
        return self.__quantity

    def Set_Quantity(self, amount):
        self.__quantity = amount

    def AddQuantity(self, amount = 1):
        self.__quantity += amount

    def RemoveQuantity(self, amount):
        self.__quantity -= amount

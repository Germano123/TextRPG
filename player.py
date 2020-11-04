from inventory import Inventory

class Player:
    def __init__(self, name):
        self.__name = name
        self.__inventories = []
    
    def Get_Name(self):
        return self.__name
    
    def AddInventory(self, quantity):
        self.__inventories.append(Inventory(quantity))

    def AddItem(self, item, quantity=1):
        item.Set_Quantity(quantity)
        for _inventory in self.__inventories:
            if(_inventory.AddItem(item)):
                return True
        return False

    def RemoveItem(self, itemName, quantity):
        for _inventory in self.__inventories:
            if(_inventory.RemoveItem(itemName, quantity)):
                return True
        return False

    def Get_ItemQuantity(self, itemName):
      quantity = 0
      for _inventory in self.__inventories:
        quantity += _inventory.Get_ItemQuantity(itemName)
      return quantity

    def Get_AllItens(self):
        itens_list = []
        for _inventory in self.__inventories:
            for _item in _inventory.Get_AllItens():
                itens_list.append(_item)
        return itens_list
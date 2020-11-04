from copy import copy

class Inventory:
    def __init__(self, quantity):
        self.__quantity = quantity
        self.__slots = []
        
    def __FlushItens(self):
        # alphabetical sort
        def ByName(item):
            return item.Get_Name()
        self.__slots.sort(key = ByName)
        
        #reagrupre quantity
        # to do

    def Get_ItemQuantity(self, itemName):
      quantity = 0  
      for _item in self.__slots:
        if(_item.Get_Name() == itemName):
          quantity += _item.Get_Quantity()
      return quantity

    def AddItem(self, item):
        # check each item in inventory
        for _item in self.__slots:
            # check if has already an item
            if(_item.Get_Name() == item.Get_Name()):
                # check if has overflow of quantity
                if(_item.Get_Quantity()+item.Get_Quantity() > _item.Get_Stack()):
                    extra = _item.Get_Stack()-_item.Get_Quantity()
                    _item.AddQuantity(extra)
                    item.RemoveQuantity(extra)
                    self.__slots.append(item)
                    return True
                else:
                    _item.AddQuantity(item.Get_Quantity())
                    return True
        # if reaches here has no item equal the one to add before
        if(len(self.__slots) < self.__quantity):
            while(item.Get_Quantity() > item.Get_Stack()):
                item.RemoveQuantity(item.Get_Stack())
                _item = copy(item)
                _item.Set_Quantity(item.Get_Stack())
                self.__slots.append(_item)
            self.__slots.append(item)
            self.__FlushItens()
            return True
            
        return False
    
    def RemoveItem(self, itemName, quantity):
        for _item in self.__slots:
            if(_item.Get_Name() == itemName):
                _item.RemoveQuantity(quantity)
                self.__FlushItens()
                return True
                
        return False

    def Get_AllItens(self):
        self.__FlushItens()
        return self.__slots

from copy import copy

from player import Player
from Itens import itens_dict

player = Player("Germano")
player.AddInventory(15)

def PlayerItens(player):
    print(player.Get_Name()+" has:")
    for _item in player.Get_AllItens():
        print(str(_item.Get_Quantity())+" - "+str(_item.Get_Name()))

def PlayerAddItem(player, itemName, quantity):
    player.AddItem(copy(itens_dict[itemName]), quantity)

def PlayerRemoveItem(player, itemName, quantity):
    player.RemoveItem(itemName, quantity)

# main loop
PlayerAddItem(player, "Moeda", 150)
PlayerItens(player)

PlayerAddItem(player, "Carne seca", 37)
PlayerItens(player)


PlayerRemoveItem(player, "Carne seca", 4)
PlayerItens(player)




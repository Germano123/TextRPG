from copy import copy

from player import Player
from playeractions import *
from itens import itens_dict
from towers import towers_dict

player = Player("Germano")
player.AddInventory(15)

def PlayerItens(player):
    print("\n"+player.Get_Name()+" has:")
    for _item in player.Get_AllItens():
        print(str(_item.Get_Quantity())+" - "+str(_item.Get_Name()))

def PlayerAddItem(player, itemName, quantity):
    player.AddItem(copy(itens_dict[itemName]), quantity)

def PlayerRemoveItem(player, itemName, quantity):
    player.RemoveItem(itemName, quantity)

# inventory tests

# add some test itens
PlayerAddItem(player, "Pedra", 67)
PlayerAddItem(player, "Moeda de bronze", 150)
PlayerRemoveItem(player, "Pedra", 17)
PlayerAddItem(player, "Madeira", 35)

PlayerItens(player)

# inventory cost tests
def TowerConstruct(player, towerName):
  Construct(player, towers_dict[towerName])

TowerConstruct(player, "Archers tower")

PlayerItens(player)

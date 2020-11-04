def Construct(player, tower):
  print("\n"+tower.Get_Name()+" costs:")
  
  costs = tower.Get_Cost()
  for _cost in costs:
    print(str(costs[_cost])+" - "+_cost)
  
  can = []
  for _cost in costs:
    if(costs[_cost] <= player.Get_ItemQuantity(_cost)):
      can.append(True)
  
  if(sum(can) == len(costs)):
    for _cost in costs:
      player.RemoveItem(_cost, costs[_cost])
    print("\nThe itens were removed. You have constructed a tower.")
  else:
    print("\nCan't construct. You don't have the necessary itens.")


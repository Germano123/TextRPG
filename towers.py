from tower import Tower

#Tower(name, cost)
#cost = { item: quantity }
towers_dict = {
  "Archers tower": Tower("Archers tower", {
      "Pedra": 10,
      "Madeira": 15,
      "Moeda de bronze": 30,
    }
  ),
  "Flame tower": Tower("Flame tower", {
      "Pedra": 25,
      "Madeira": 15,
      "Moeda de bronze": 50,
    }
  ),
  "Aqua tower": Tower("Aqua tower", {
      "Pedra": 15,
      "Madeira": 30,
      "Moeda de bronze": 50,
    }
  ),
}
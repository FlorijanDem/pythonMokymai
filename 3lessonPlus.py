# 2. Žaidėjo inventorius
# Sukurkite klasę Item, kuri turi:
# name
# item_type
# weight
# Sukurkite klasę Player, kuri turi:
# name
# level
# inventory
# inventory turi būti tuščias sąrašas.
# Sukurkite metodus klasėje Player:
# add_item(item) — prideda daiktą į inventorių.
# remove_item(item_name) — pašalina daiktą pagal pavadinimą.
# get_total_weight() — grąžina bendrą inventoriaus svorį.
# level_up() — padidina žaidėjo lygį vienetu.
# __str__
# Sukurkite vieną žaidėją ir bent 5 daiktus.
# Pridėkite daiktus žaidėjui į inventorių.
# Išbandykite:
# pridėti daiktą;
# pašalinti daiktą;
# pakelti žaidėjo lygį;
# išvesti bendrą inventoriaus svorį.
# Papildomai:
# Žaidėjas negali turėti daugiau nei 20 kg inventoriaus. Jeigu pridėjus naują daiktą svoris viršytų 20 kg, daiktas neturi būti pridėtas.


class Item:
    def __init__(self, name, item_type, weight):
        self.name = name
        self.item_type = item_type
        self.weight = weight

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.inventory = []
    
    def level_up(self):
        self.level += 1

    def __str__(self):
        items_in_inventory = []
        for i in self.inventory:
            items_in_inventory.append({i.name, i.item_type, i.weight})
        result = f"Name:{self.name} Level:{self.level} Inventory:{items_in_inventory}"
        return result
    
    def add_item(self, item):
        if self.get_total_weight() + item.weight > 20:
            print("Cannot hadle it")
        else:
            self.inventory.append(item)

    def remove_item(self, item_name):
        self.inventory.remove(item_name)

    def get_total_weight(self):
        return sum(item.weight for item in self.inventory)

sword = Item("Sword", 1, 6.2)
bow = Item("Bow", 1, 2.3)
sheld = Item("Sheld", 2, 11)
rock = Item("Rock", 3, 25)
    
player = Player("Jonas", 1)
player.add_item(sword)
player.add_item(bow)
player.add_item(sheld)
# player.add_item(rock)

player.remove_item(bow)
player.level_up()
print(player)
print(f'Weight:{player.get_total_weight()}')
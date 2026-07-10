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

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item_name):
        self.inventory.remove(item_name)

    def get_total_weight(self):
        sum:float = 0
        for i in self.weight:
            sum = sum + self.weight
        return sum
    

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.inventory = []
    
    def level_up(self):
        self.level += 1

    def __str__(self):
        result = f"Name:{self.name} Level:{self.level} Inventory:{self.inventory}"
        return result
    
    
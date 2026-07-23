# 1. Skirtingi transporto priemonių garsai
# Tikslas
# Praktiškai išbandyti paveldėjimą ir metodo perrašymą.
# Užduotis
# Sukurkite bazinę klasę Vehicle, kuri turėtų:
# gamintoją;
# modelį;
# pagaminimo metus;
# metodą make_sound().
# Sukurkite tris paveldinčias klases:
# Car;
# Motorcycle;
# Bicycle.
# Kiekviena klasė turi skirtingai perrašyti metodą make_sound():
# automobilis gali skleisti variklio garsą;
# motociklas – kitokį variklio garsą;
# dviratis – skambučio garsą.
# Sudėkite bent po vieną kiekvienos klasės objektą į bendrą sąrašą ir su ciklu iškvieskite visų objektų make_sound() metodą.
# Papildomas reikalavimas
# Kiekviena klasė turi turėti metodą display_info(), kuris išveda tvarkingą informaciją apie objektą.
# Patarimai
# Visus bendrus atributus laikykite klasėje Vehicle.
# Vaikų klasėse nekartokite to, ką jau atlieka tėvinė klasė.
# Objektų tipų tikrinti su keliais if neturėtų reikėti.

class Vehicle:
    def __init__(self, make, model, manufacture_year):
        self.make = make
        self.model = model
        self.manufacture_year = manufacture_year
        
    def make_sound():
        return "Whoooo"

class Car(Vehicle):
    def make_sound():
        return "Ratatata"
    
class Motorcycle(Vehicle):
    def make_sound():
        return "Vzuu-vzuu"
    
class Bicycle(Vehicle):
    def make_sound():
        return "Dzin-dzin"
    
print(Car.make_sound())
print(Motorcycle.make_sound())
print(Bicycle.make_sound())
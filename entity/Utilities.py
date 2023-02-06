import random

class Weapon():
    def __init__(self, damage_send:int, durability:int, magic:bool, range:bool, strength:bool, name):
        #int
        
        self.damage = damage_send
        self.durability = durability 
        self.name = name

        #bool 

        self.magic = magic
        self.range = range
        self.strength = strength



knife = Weapon(100 + random.randint(0, 20), 10 + random.randint(0, 15), 0, 0, 1, "knife")
sword = Weapon(124 + random.randint(0, 10), 7 + random.randint(0, 15), 0, 0, 1, "sword")
bow = Weapon(120 + random.randint(0, 25), 14 + random.randint(0, 7), 0, 1, 0, "bow")
crossbow = Weapon(100 + random.randint(0, 15), 17 + random.randint(0, 15), 0, 1, 0, "crossbow")
magic_stick = Weapon(150 + random.randint(0, 35), 50 + random.randint(0, 15), 1, 0, 0, "magic_stick")

print("weapons class loaded")

class Potion():
    def __init__(self, heal:int):
        self.heal = heal

healing_potion = Potion(random.randint(5, 40))

print("potion class loaded")
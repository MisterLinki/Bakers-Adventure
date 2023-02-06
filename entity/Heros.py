from random import randint

class Hero():
    def __init__(self, life:int, mana:int, punch_damage:int,magic:bool, range:bool, strength:bool , name:str):
        #int
        self.punch_damage = punch_damage
        self.started_life = life
        self.life = life
        self.mana = mana
        self.name = name
        
        #bool
        self.magic = magic
        self.range = range
        self.strength = strength
    
    def is_dodging(self):
        #bool

        if randint(1, 4) == 4:   return True
        else:   return False


baker_warrior = Hero(125, 50, 34, 0, 0, 1, "baker warrior") #speciality : strength
baker_magician = Hero(60, 120, 30, 1, 0, 0, "baker magician") #speciality : magic
baker_dwarf = Hero(90, 80, 100, 0, 0, 0, "baker dwarf") #speciality : his fists
baker_archer = Hero(65, 60, 25, 0, 1, 0, "baker archer") #speciality : ranger

print("Heros class loaded")

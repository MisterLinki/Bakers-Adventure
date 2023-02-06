import random
import os

class Monster():
    def __init__(self, mana:int, big:bool):
        #monster's name
        
        file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'names.txt')
        with open(f"{file}") as txt:  self.name = txt.readlines()[random.randint(0, len(file))]
        #int
        self.life = random.randint(150, 500)
        self.mana = mana
        self.damage = 25                                                            
        
        #bool
        if big: 
            self.life += 150
            self.damage += 35

    def is_dodging():
        #bool
        if random.randint(1, 7) == 5:   return True
        else:   return False

print("Monsters class loaded")
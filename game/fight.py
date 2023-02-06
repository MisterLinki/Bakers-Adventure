from entity.Inventory import*
from entity.Heros import*
from entity.Monsters import*

import random

class Fight:
    def __init__(self):
        self.round = [
                baker_archer,
                baker_dwarf,
                baker_magician,
                baker_warrior
                    ]
        self.hero = [
                baker_archer,
                baker_dwarf,
                baker_magician,
                baker_warrior
                    ]

        self.ennemies = []
        self.current_round = 0
        self.current_round_player = 0
        self.is_fighting = True

        #list life

        self.hero_life = [
                    baker_archer.life,
                    baker_dwarf.life,
                    baker_magician.life,
                    baker_warrior.life
                        ]
        self.ennemies_life = []
        

    def shuffle_order(self):
        for i in range(random.randint(1, 3)):
            self.is_big = False
            monster = Monster(10, self.is_big)
            if random.randint(1, 9) == 5:
                self.is_big = True

            self.ennemies_life.append(monster.life)
            self.ennemies.append(monster)
            self.round.append(monster)
            
        random.shuffle(self.round)
        return self.round

    def is_playing(self):
        self.hero_selected = False

        if self.round[self.current_round] in self.hero:
            for is_hero in self.hero:
                if self.round[self.current_round] == is_hero:
                    self.hero_selected = True

        return self.hero_selected

    def inventory_randomly(self):
        items = [knife, sword, crossbow, bow, magic_stick, healing_potion]

        for i in range(random.randint(1, 15)):
            baker_inventory.is_inventory_full(items[random.randint(0, len(items)-1)])    

fight = Fight()


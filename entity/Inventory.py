from entity.Utilities import*

class Inventory():
    def __init__(self):
        self.content = [
            [], #knifes
            [], #swords
            [], #bows
            [], #crossbows
            [], #magic_sticks
            [], #healing Potions
            ]

    def is_inventory_full(self, item):
        if item == knife:
            if len(self.content[0]) < 4:  self.content[0].append(item)
            else:  return False
                    
        if item == sword:
            if len(self.content[1]) < 4:  self.content[1].append(item)
            else:   return False
        
        if item == bow:
            if len(self.content[2]) < 4:  self.content[2].append(item)
            else:   return False

        if item == crossbow:
            if len(self.content[3]) < 4:   self.content[3].append(item)
            else:   return False

        if item == magic_stick:
            if len(self.content[4]) < 4:   self.content[4].append(item)
            else:   return False

        if item == healing_potion:
            if len(self.content[5]) <2:   self.content[5].append(item)
            else: return False

baker_inventory = Inventory()
print("Inventory class loaded")

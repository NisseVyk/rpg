import random
class Loot:
    def __init__(self, name, damage, defense, enett):
        self.name = name
        self.damage = damage
        self.defense = defense
        self.enett = enett

loot_list = [Loot("Träsvärd", 25, 0, "ett"), Loot("Träsköld", 0 ,15, "en"), Loot("Pilbåge", 20, 0, "en")]

def get_loot():
    return random.choice(loot_list)

    
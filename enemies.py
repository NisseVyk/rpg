import random

class Enemies:
    def __init__(self, name, damage, health, enett):
        self.name = name
        self.damage = damage
        self.health = health
        self.enett = enett

enemies_list = [Enemies("slime", 20, 25, "ett")]

def get_enemy():
    return random.choice(enemies_list)
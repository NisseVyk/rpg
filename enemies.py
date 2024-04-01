import random

class Enemies:
    def __init__(self, name, damage, health, enett):
        self.name = name
        self.damage = damage
        self.health = health
        self.enett = enett

enemies_list = [Enemies("slime", 20, 25, "ett"), Enemies("skelett", 30, 50, "ett"), Enemies("zombie", 40, 80, "ett")]

def get_enemy():
    return random.choice(enemies_list)
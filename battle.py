import random
import os

def battle(player, enemy):
    #Fixar spelarens stats
    player_inventory = []
    player_damage = 0
    player_defense = 0
    player_health = player.health

    empty = True  #bestämmer om spelaren kommer behöva slåss med händerna
    if player.main_hand is not None:
        player_inventory.append(player.main_hand)
        empty = False
    if player.off_hand is not None:
        player_inventory.append(player.off_hand)
        empty = False
    if empty == True:
        player_damage +=5 #Ger spelaren en chans att slå vissa fiender
    
    for item in player_inventory:
        player_damage += item.damage
        player_defense += item.defense
    #---------------------
        
    #Fixar fiendens stats
    enemy_damage = enemy.damage
    enemy_health = enemy.health
    #--------------------

    clear()
    print(f"Himmel och pannkaka! Du mötte {enemy.enett} {enemy.name}!\n")
    while True:
        

def clear():
    os.system("cls" if os.name == 'nt' else 'clear')
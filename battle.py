import random
import time
import os

def clear():
    os.system("cls" if os.name == 'nt' else 'clear')

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

        #Får fram chansen att lyckas fly
        diff = player_health + player_damage - enemy_health - enemy_damage
        if diff > 100:
            diff = 100
        elif diff < 10:
            diff = 10
        #-------------------------------
            
        clear()
        player_input = input(f"Ditt HP: {player_health}\nFiendens HP: {enemy_health}\n\nVad vill du göra?\n1. Attackera ({player_damage}dmg)\n2. Fly ({diff}% chans)\n")
        
        clear()
        match player_input:
            case "1":
                enemy_health-=player_damage
            case "2":
                if diff >= random.randrange(1,101):
                    print("Du lyckades fly")
                    time.sleep(3)
                    return "2"
                else:
                    print("Du misslyckades")
                    time.sleep(3)

        if enemy_health > 0:
            if enemy_damage > player_defense: #så att spelaren inte får hp om den har nog hög defense
                player_health -= (enemy_damage - player_defense)
                clear()
                print(f"{enemy.name} gjorde {enemy.damage}dmg")
            
            if player_health <= 0:
                return "0"
            
        else:
            return "1"
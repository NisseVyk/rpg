import character
import map
import rooms
import loot
import enemies
import battle
import visuals
import os

player = character.Character(1,len(map.map)-2, 100, None, None)
start_pos = rooms.rooms[player.pos_y][player.pos_x]
start_pos.visited_toggle()
def clear():    
    os.system("cls" if os.name == 'nt' else 'clear')

while True:
    clear()
    visuals.print_map(player.pos_x, player.pos_y)

    #Definieras av storleken på kartan
    x_length = len(map.map[player.pos_y])-1
    y_length = len(map.map)-1
    #----------------------------------

    direction = input("\nVart vill du gå? \n\n1. NORR\n2. ÖST\n3. SYD\n4. VÄST\n\n")
    match direction: 
        case "1":
            if map.get_room(player.pos_x, player.pos_y - 1) != "w":
                player.change_pos(0, -1)
        case "2":
            if map.get_room(player.pos_x + 1, player.pos_y) != "w":
                player.change_pos(1, 0)
        case "3":
            if map.get_room(player.pos_x, player.pos_y - 1) != "w":
                player.change_pos(0, 1)
        case "4":
            if map.get_room(player.pos_x - 1, player.pos_y) != "w":
                player.change_pos(-1, 0)

    result = rooms.enter_room(player.pos_x, player.pos_y)

    if result is not None:
        if type(result) == loot.Loot:
            clear()
            print(f"Du hittade {result.enett} {result.name}, DMG: {result.damage}, DEF: {result.defense}\n\nDu har i dina händer:\n")

            if player.main_hand is not None:
                print(f"Main hand: {player.main_hand.name}, DMG:{player.main_hand.damage}, DEF:{player.main_hand.defense}")
            else:
                print("Main hand: tom")
            
            if player.off_hand is not None:
                print(f"Off hand: {player.off_hand.name}, DMG:{player.off_hand.damage}, DEF:{player.off_hand.defense}")
            else:
                print("Off hand: tom")
            
            answer = input("\nVar vill du ha vapnet?\n\n1. Main hand\n2. Off hand\n3. Lämna det\n")

            match answer:
                case "1":
                    player.main_hand = result
                
                case "2":
                    player.off_hand = result

        if type(result) == enemies.Enemies:
            battle.battle(player, result)
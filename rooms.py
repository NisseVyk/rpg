import map
import loot
import enemies

class Room:
    def __init__(self, letter):
        self.visited = False
        self.letter = letter

    def visited_toggle(self):
        if self.visited == False:
            self.visited = True

rooms = []

def create_rooms():

    for y in map.map:
        temp = []

        for x in y:
            temp.append(Room(x))

        rooms.append(temp)
  
def enter_room(pos_x, pos_y):

    if rooms[pos_y][pos_x].visited == False:
        rooms[pos_y][pos_x].visited_toggle()

        letter = rooms[pos_y][pos_x].letter
        match letter:
            case "l":
                result = loot.get_loot()
                return result
            case "e":
                result = enemies.get_enemy()
                return result

create_rooms()
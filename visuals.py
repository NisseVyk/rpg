import rooms
import map

def print_map(pos_x, pos_y):
    mini_map = []

    #Ritar mapen
    y=0
    while y < len(map.map):
        x=0
        temp = []
        while x < len(map.map[y]):

            if rooms.rooms[y][x].letter == "w":
                temp.append("# ")
            elif x == pos_x and y == pos_y:     #Spelarens nuvarande position som "o"
                temp.append("o ")
            elif rooms.rooms[y][x].visited == True: #Rum spelaren tidigare varit i som "  "
                temp.append("  ")
            else:                             #Övriga rum som "x"
                temp.append("x ")
            x+=1
    
        mini_map.append(temp)
        y+=1

    y=0
    while y < len(mini_map):

        print("".join(mini_map[y]))
        
        y+=1
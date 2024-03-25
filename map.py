
map = [
    ["w","w","w","w","w","w","w","w"],
    ["w","x","x","x","x","x","x","w"],
    ["w","x","x","x","x","x","x","w"],
    ["w","x","x","x","x","x","x","w"],
    ["w","x","l","x","x","x","x","w"],
    ["w","f","l","x","x","x","x","w"],
    ["w","x","l","f","x","x","x","w"],
    ["w","w","w","w","w","w","w","w"]
] 

def get_room(pos_x, pos_y):
    return map[pos_y][pos_x]
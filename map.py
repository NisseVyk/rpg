map = [
    ["w","w","w","w","w","w","w","w","w"],
    ["w","e","w","x","x","x","x","x","w"],
    ["w","x","w","e","w","w","w","x","w"],
    ["w","l","x","x","w","l","x","x","w"],
    ["w","x","w","w","w","w","w","x","w"],
    ["w","x","x","e","w","e","x","x","w"],
    ["w","w","w","x","w","w","l","w","w"],
    ["w","x","x","x","l","w","b","g","w"],
    ["w","w","w","w","w","w","w","w","w"]
] 

def get_room(pos_x, pos_y):
    return map[pos_y][pos_x]
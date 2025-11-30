
class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

def house_visited(input: str) -> int:
    santa_coord = (0,0)
    santa: set = {santa_coord}
    robo_santa_coord = (0,0)
    robo_santa: set = {robo_santa_coord}
    is_santa = True
    for dir in input:
        coord = ()
        if is_santa:
            coord = santa_coord
        else:
            coord = robo_santa_coord
        if dir == ">":
            new_coord = (coord[0]+1, coord[1])
        elif dir == "<":
            new_coord = (coord[0]-1, coord[1])
        elif dir == "^":
            new_coord = (coord[0], coord[1]+1)
        elif dir == "v":
            new_coord = (coord[0], coord[1]-1)
        if is_santa:
            santa.add(new_coord)
            santa_coord = new_coord
        else:
            robo_santa.add(new_coord)
            robo_santa_coord = new_coord
        is_santa = not is_santa
    visited = santa.union(robo_santa)
    return len(visited)

if __name__ == "__main__":
    with open("day3.txt", "r") as file:
        input = file.read()
        print(house_visited(input))
        #print(house_visited("^>v<"))

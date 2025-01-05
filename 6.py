import copy 

def turnRight(direction):
    if direction == "^":
        return ">"
    elif direction == ">":
        return "v"
    elif direction == "v":
        return "<"
    elif direction == "<":
        return "^"

def day6part1(placeMap, guardStart):
    locX, locY = guardStart
    visited = set()  # To track all distinct positions visited
    visited.add((locX, locY))  # Include the starting position
    directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

    while 0 <= locX < len(placeMap) and 0 <= locY < len(placeMap[0]):
        current_dir = placeMap[locX][locY]
        dx, dy = directions[current_dir]
        nextX, nextY = locX + dx, locY + dy

        if 0 <= nextX < len(placeMap) and 0 <= nextY < len(placeMap[0]) and placeMap[nextX][nextY] != "#":
            # Move forward
            locX, locY = nextX, nextY
            visited.add((locX, locY))  # Track visited position
            placeMap[locX][locY] = current_dir  # Update current direction
        elif 0 <= nextX < len(placeMap) and 0 <= nextY < len(placeMap[0]) and placeMap[nextX][nextY] == "#":
            # Turn right
            placeMap[locX][locY] = turnRight(current_dir)
        else:
            locX, locY = nextX, nextY
    # Mark all visited positions with 'X'
    for x, y in visited:
        placeMap[x][y] = "X"
    
    return len(visited)  # Return the final map and the count of distinct positions


def day6part2(placeMap, guardStart):
    directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}



    solutions = 0
    for i in range(len(placeMap)):
        for j in range(len(placeMap[i])):
            # create a copy of the map
            copyMap = copy.deepcopy(placeMap)
            # if the place is an obstacle or a direction, skip
            if copyMap[i][j] == "#" or copyMap[i][j] in directions:
                continue
            # set the place to be an obstacle
            copyMap[i][j] = "#"   
            locX, locY = guardStart

            moves = 0
            # move around the map
            while 0 <= locX < len(copyMap) and 0 <= locY < len(copyMap[0]):
                current_dir = copyMap[locX][locY]
                dx, dy = directions[current_dir]
                nextX, nextY = locX + dx, locY + dy
                moves+=1

                # when moves surpass the limit, break (loop found)
                if moves > len(copyMap) * len(copyMap[0]):
                    solutions+=1
                    break

                if 0 <= nextX < len(copyMap) and 0 <= nextY < len(copyMap[0]) and copyMap[nextX][nextY] != "#":
                    # Move forward
                    locX, locY = nextX, nextY
                    copyMap[locX][locY] = current_dir  # Update current direction
                elif 0 <= nextX < len(copyMap) and 0 <= nextY < len(copyMap[0]) and copyMap[nextX][nextY] == "#":
                    # Turn right
                    copyMap[locX][locY] = turnRight(current_dir)
                else:
                    locX, locY = nextX, nextY
            # print(moves)
            

    return solutions


placeMap = []
guardStart = 0,0
rouwCount = 0
for row in open("6.txt", "r"):
    row = list(row.strip())
    placeMap.append(row)
    if "^" in row:
        guardStart = rouwCount, row.index("^")
    rouwCount+=1

# print(day6part1(placeMap, guardStart))
print(day6part2(placeMap, guardStart))
# find XMAS on crossword (horizontal, vertical, diagonal, backwards)
def day4Part1(crossword):
    def findM(crossword, i, j): # should return a list since there could be multiple Ms for a given X
        Ms = []
        # search neighbors
        if i > 0 and crossword[i-1][j] == "M":
            Ms.append("up")
        if i < len(crossword) - 1 and crossword[i+1][j] == "M":
            Ms.append("down")
        if j > 0 and crossword[i][j-1] == "M":
            Ms.append("left")
        if j < len(crossword[i]) - 1 and crossword[i][j+1] == "M":
            Ms.append("right")
        if i > 0 and j > 0 and crossword[i-1][j-1] == "M":
            Ms.append("upleft")
        if i > 0 and j < len(crossword[i]) - 1 and crossword[i-1][j+1] == "M":
            Ms.append("upright")
        if i < len(crossword) - 1 and j > 0 and crossword[i+1][j-1] == "M":
            Ms.append("downleft")
        if i < len(crossword) - 1 and j < len(crossword[i]) - 1 and crossword[i+1][j+1] == "M":
            Ms.append("downright")
        return Ms

    def checkLetter(letter, crossword, i, j, direction):
        if direction == "up":
            if i > 0 and crossword[i-1][j] == letter:
                return True
        if direction == "down":
            if i < len(crossword) - 1 and crossword[i+1][j] == letter:
                return True
        if direction == "left":
            if j > 0 and crossword[i][j-1] == letter:
                return True
        if direction == "right":
            if j < len(crossword[i]) - 1 and crossword[i][j+1] == letter:
                return True
        if direction == "upleft":
            if i > 0 and j > 0 and crossword[i-1][j-1] == letter:
                return True
        if direction == "upright":
            if i > 0 and j < len(crossword[i]) - 1 and crossword[i-1][j+1] == letter:
                return True
        if direction == "downleft":
            if i < len(crossword) - 1 and j > 0 and crossword[i+1][j-1] == letter:
                return True
        if direction == "downright":
            if i < len(crossword) - 1 and j < len(crossword[i]) - 1 and crossword[i+1][j+1] == letter:
                return True
        return False


    def updateSearchIndex(i, j, direction): 
        if direction == "up":
            return i - 1, j
        if direction == "down":
            return i + 1, j
        if direction == "left":
            return i, j - 1
        if direction == "right":
            return i, j + 1
        if direction == "upleft":
            return i - 1, j - 1
        if direction == "upright":
            return i - 1, j + 1
        if direction == "downleft":
            return i + 1, j - 1
        if direction == "downright":
            return i + 1, j + 1

    def XMASatCurrentIndex(crossword, i, j):
        XMASatIndex = 0
        # find X
        if crossword[i][j] == "X":
            # print("X found at", i, j)
            # find M 
            # determine direction to find next letter
            Mdirections = findM(crossword, i, j)
            if len(Mdirections) == 0:
                return 0
            else:
                # print("M found at", i, j, "directions", Mdirections)
                for direction in Mdirections:
                    newi, newj = updateSearchIndex(i, j, direction)  
                    # print("M found at", newi, newj, "direction", direction)
                    # find A
                    isA = checkLetter("A", crossword, newi, newj, direction)
                    if not isA:
                        continue
                    else:
                        newi, newj = updateSearchIndex(newi, newj, direction)  
                        # print("A found at", newi, newj, "direction", direction)
                        # find S
                        isS = checkLetter("S", crossword, newi, newj, direction)
                        if not isS:
                            continue
                        else:
                            # print("S found at", newi, newj, "direction", direction)
                            XMASatIndex += 1
        return XMASatIndex
    


    XMASfound = 0
    for i in range(len(crossword)):
        for j in range(len(crossword[i])):
            XMASfound += XMASatCurrentIndex(crossword, i, j)
    return XMASfound



def day4part2(crossword):
    # is X_MAS if:
        # upper left and lower right are "M" and "S" (or vice versa)
        # upper right and lower left are "M" and "S" (or vice versa)
    def X_MAS(crossword, i, j):
        if (crossword[i-1][j-1] == "M" and crossword[i+1][j+1] == "S") or (crossword[i-1][j-1] == "S" and crossword[i+1][j+1] == "M"):
            if (crossword[i+1][j-1] == "M" and crossword[i-1][j+1] == "S") or (crossword[i+1][j-1] == "S" and crossword[i-1][j+1] == "M"):
                return True
        return False

    XMASfound = 0
    # only look at the inner part of the crossword (finding the center "A" of MAS shaped as X)
    for i in range(1, len(crossword)-1):
        for j in range(1, len(crossword[i])-1):
            if crossword[i][j] == "A":
                XMASfound += 1 if X_MAS(crossword, i, j) else 0

    return XMASfound

crossword = []
for line in open ("4.txt", "r"):
    row = line.strip()
    crossword.append(row)

print(day4Part1(crossword))
print(day4part2(crossword))
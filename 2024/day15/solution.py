
import copy
with open('input.txt') as file:
    map, moves  = file.read().strip().split("\n\n")

map = map.split("\n")

nrows = len(map)
ncols = len(map[0])

grid = {}

for nrow, line in enumerate(map):
    for ncol, thing in enumerate(line):
        grid[(nrow, ncol)] = thing
        if thing == "@":
            robot = (nrow, ncol)

directions = {"^":(-1, 0), ">":(0, 1), "v":(1, 0), "<":(0, -1)}

def printGrid(map, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print(map[(i, j)], end="")
        print("\n")

def getNextPos(pos, dir):
    return (pos[0] + directions[dir][0], pos[1] + directions[dir][1])


def canMove(grid, boxPos, dir):
    while(True):
        nextPos = getNextPos(boxPos, dir)
        if grid[nextPos] == ".":
            return (nextPos)
        elif grid[nextPos] == "#":
            return False
        else:
            boxPos = nextPos

def moveHorizontal(grid, pos, dir):
    copyGrid = copy.deepcopy(grid)

    while(True):
        nextPos = getNextPos(pos, dir)
        if grid[nextPos] == ".":
            copyGrid[nextPos] = grid[pos]
            return copyGrid
        elif grid[nextPos] == "#":
            return False
        else:
            copyGrid[nextPos] = grid[pos]
            pos = nextPos


def moveVertical(grid, pos, move):
    copyGrid = copy.deepcopy(grid)
    if grid[pos] == "[":
        posOther = (pos[0], pos[1] + 1)
    elif grid[pos] == "]":
        posOther = (pos[0], pos[1] - 1)

    boxes = {pos, posOther}
    visited = [pos, posOther]
    changed = set()
    while(len(boxes) > 0):
        curr = boxes.pop()
        nextPos = getNextPos(curr, move)
        visited.append(curr)
        if grid[curr] == "[":
            posTwo = (curr[0], curr[1] + 1)
            if posTwo not in visited:
                boxes.add(posTwo)
        elif grid[curr] == "]":
            posTwo = (curr[0], curr[1] - 1)
            if posTwo not in visited:
                boxes.add(posTwo)
        if grid[nextPos] == ".":
            copyGrid[nextPos] = grid[curr]
            changed.add(nextPos)
            continue
        elif grid[nextPos] == "#":
            return False
        else:
            if nextPos not in visited:
                boxes.add(nextPos)
            copyGrid[nextPos] = grid[curr]
            changed.add(nextPos)
            curr = nextPos
    for x in visited:
        if x not in changed:
            copyGrid[x] = "."
            changed.add(x)
    copyGrid[pos] = "@"
    copyGrid[posOther] = "."
    return copyGrid
    


def moveBox(grid, robo, move):
    if move == "<" or move == ">":
        moved = moveHorizontal(grid, robo, move)
        if moved != False:
            moved[robo] = "."
            return moved
    else:
        nextPos = getNextPos(robo, move)
        moved = moveVertical(grid, nextPos, move)
        if moved != False:
            moved[robo] = "."
            return moved
    return False

        

def partOne(grid, moves, robot):
    map = copy.deepcopy(grid)
    for move in moves:
        if move not in directions.keys():
            continue
        nextPos = getNextPos(robot, move)
        if map[nextPos] == ".":
            map[robot] = "."
            map[nextPos] = "@"
            robot = nextPos
        elif map[nextPos] == "O":
            pos = canMove(map, nextPos, move)
            if pos != False:
                map[pos] = "O"
                map[robot] = "."
                map[nextPos] = "@"
                robot = nextPos
    
    total = 0

    for pos, value in map.items():
        if value == "O":
            total += (pos[1] + 100*pos[0])

    print("Part 1:",total)



def getNewGrid(grid):
    newGrid = {}
    for i in range(nrows):
        for j in range(ncols):
            if grid[(i,j)] == "#":
                newGrid[(i, 2*j)] = "#"
                newGrid[(i, 2*j+1)] = "#"
            elif grid[(i,j)] == "O":
                newGrid[(i, 2*j)] = "["
                newGrid[(i, 2*j+1)] = "]"
            elif grid[(i,j)] == ".":
                newGrid[(i, 2*j)] = "."
                newGrid[(i, 2*j+1)] = "."
            else:
                newRobot = (i, 2*j)
                newGrid[(i, 2*j)] = "@"
                newGrid[(i, 2*j+1)] = "."
    return newGrid, newRobot


def partTwo(map, moves):
    newGrid, newRobot = getNewGrid(map)

    for move in moves:
        if move not in directions.keys():
            continue
        nextPos = getNextPos(newRobot, move)
        if newGrid[nextPos] == ".":
            newGrid[newRobot] = "."
            newGrid[nextPos] = "@"
            newRobot = nextPos
        elif newGrid[nextPos] == "[" or newGrid[nextPos] == "]":
            movedGrid = moveBox(newGrid, newRobot, move)
            if movedGrid != False:
                newGrid = movedGrid
                newRobot = nextPos
                
    
    total = 0

    for pos, value in newGrid.items():
        if value == "[":
            total += (pos[1] + 100*pos[0])

    print("Part 2:",total)


partOne(grid, moves, robot)
partTwo(grid, moves)

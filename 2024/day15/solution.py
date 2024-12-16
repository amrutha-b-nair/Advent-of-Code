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


def partOne(map, moves, robot):
    for move in moves:
        if move not in directions.keys():
            continue
        nextPos = getNextPos(robot, move)
        if map[nextPos] == ".":
            map[robot] = "."
            map[nextPos] = "@"
            robot = nextPos
        elif map[nextPos] == "O":
            pos = canMove(grid, nextPos, move)
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


partOne(grid, moves, robot)
# partTwo(grid, moves)

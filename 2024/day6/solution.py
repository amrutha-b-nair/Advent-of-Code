with open('input.txt') as file:
    lines = file.read().strip().split('\n')

directionChange = {"^": ">", ">": "v", "v": "<", "<": "^"}

def getGuardInfo(direction, row, col, ncols, nrows):
    if direction == "^":
        return [[row, col], range(row - 1, -1, -1), [1, 0], directionChange["^"]]
    elif direction == "v":
        return [[row, col], range(row + 1, nrows), [1, 0], directionChange["v"]]
    elif direction == ">":
        return [[row, col], range(col + 1, ncols), [0, 1], directionChange[">"]]
    elif direction == "<":
        return [[row, col], range(col - 1, -1, -1), [0, 1], directionChange["<"]]

def find_neighbors(currPos, prevPos):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = [
        (currPos[0] + dr, currPos[1] + dc)
        for dr, dc in directions
        if 0 <= currPos[0] + dr < nrow and 0 <= currPos[1] + dc < ncol
        and (currPos[0] + dr, currPos[1] + dc) != prevPos
    ]
    return neighbors



def checkPathForObstacles(guardInfo, coveredPositions, possibleObstacle):

    position = guardInfo[0]
    movementRange = guardInfo[1]
    movementDirection = guardInfo[2]
    coveredPositions.append(tuple(position))

    for step in movementRange:
        next_position = [
            position[0] + movementDirection[0] * (step - position[0]),
            position[1] + movementDirection[1] * (step - position[1])
        ]
        if next_position in obstacles:
            newGuardInfo = getGuardInfo(guardInfo[3],coveredPositions[-1][0], coveredPositions[-1][1], ncol, nrow)
            return checkPathForObstacles(newGuardInfo, coveredPositions, possibleObstacle)
        else:
            if tuple(next_position) in coveredPositions:
                neighbours = find_neighbors(next_position, coveredPositions[-1])
                print(neighbours, coveredPositions)
                for neighbour in neighbours:
                    if neighbour in coveredPositions:
                        possibleObstacle += 1
                        print(next_position)
            coveredPositions.append(tuple(next_position))
    
    return coveredPositions, possibleObstacle

 

grid = []

obstacles = []

for row, line in enumerate(lines):
    grid.append(list(line))
    for col, pos in enumerate(list(line)):
        if pos == "#":
            obstacles.append([row, col])
        elif pos != ".":
            guard = getGuardInfo(pos, row, col, len(line), len(lines))

print(grid)

nrow = len(grid)
ncol = len(grid[0])

guardDirection = guard[1]

coveredPositions, possibleObstaclePositions = checkPathForObstacles(guard, [], 0)

print(len(set(coveredPositions)), possibleObstaclePositions)
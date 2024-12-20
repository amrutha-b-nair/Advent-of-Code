
##TODO Try to find a faster solution


from collections import defaultdict

with open('input.txt') as file:
    lines = file.read().strip().split('\n')

directionChange = {"^": ">", ">": "v", "v": "<", "<": "^"}

def getGuardInfo(direction, row, col, ncols, nrows):
    if direction == "^":
        return [[row, col], range(row - 1, -1, -1), [1, 0], "^"]
    elif direction == "v":
        return [[row, col], range(row + 1, nrows), [1, 0], "v"]
    elif direction == ">":
        return [[row, col], range(col + 1, ncols), [0, 1], ">"]
    elif direction == "<":
        return [[row, col], range(col - 1, -1, -1), [0, 1], "<"]

def find_neighbors(currPos, prevPos):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = [
        (currPos[0] + dr, currPos[1] + dc)
        for dr, dc in directions
        if 0 <= currPos[0] + dr < nrow and 0 <= currPos[1] + dc < ncol
        and (currPos[0] + dr, currPos[1] + dc) != prevPos
    ]
    return neighbors

def getNextPosition(direction, currentPosition):
    if direction == "^":
        return (currentPosition[0] - 1, currentPosition[1])
    elif direction == "v":
        return (currentPosition[0] + 1, currentPosition[1])
    elif direction == ">":
        return (currentPosition[0], currentPosition[1] + 1)
    elif direction == "<":
        return (currentPosition[0], currentPosition[1] - 1)


def getNextPossiblePositions(direction, currentPosition):
    guardInfo = getGuardInfo(direction, currentPosition[0], currentPosition[1], ncol, nrow)
    positions = []
    for step in guardInfo[1]:
        positions.append((guardInfo[0][0] + guardInfo[2][0] * (step - guardInfo[0][0]),
            guardInfo[0][1] + guardInfo[2][1] * (step - guardInfo[0][1])))
    return positions


def canHaveAnObstacle(guardInfo, nextPosition, positionInfo):
    if getNextPosition(guardInfo[3], nextPosition) not in obstacles:
        # print("#######", nextPosition, getNextPossiblePositions(directionChange[guardInfo[3]], nextPosition), directionChange[guardInfo[3]])
        for possiblePos in getNextPossiblePositions(directionChange[guardInfo[3]], nextPosition):
            if possiblePos == (8, 6):
                print(directionChange[guardInfo[3]], positionInfo[getNextPosition(directionChange[guardInfo[3]], possiblePos)])
            if directionChange[guardInfo[3]] in positionInfo[getNextPosition(directionChange[guardInfo[3]], possiblePos)]:
                print(nextPosition, getNextPosition(guardInfo[3], nextPosition), guardInfo[3],
                        directionChange[guardInfo[3]], getNextPosition(directionChange[guardInfo[3]], nextPosition))
                return True
    return False


def checkPathForObstacles(guardInfo, coveredPositions, possibleObstacle, positionInfo = defaultdict(list)):

    position = guardInfo[0]
    movementRange = guardInfo[1]
    movementDirection = guardInfo[2]
    coveredPositions.append(tuple(position))
    positionInfo[tuple(position)].append(guardInfo[3])
    newObstacles = []

    for step in movementRange:
        next_position = [
            position[0] + movementDirection[0] * (step - position[0]),
            position[1] + movementDirection[1] * (step - position[1])
        ]
        if next_position in obstacles:
            newGuardInfo = getGuardInfo(directionChange[guardInfo[3]],coveredPositions[-1][0], coveredPositions[-1][1], ncol, nrow)
            return checkPathForObstacles(newGuardInfo, coveredPositions, possibleObstacle, positionInfo)
        else:
            if canHaveAnObstacle(guardInfo, next_position, positionInfo):
                possibleObstacle+= 1
                newObstacles.append(getNextPosition(guardInfo[3], next_position))
            coveredPositions.append(tuple(next_position))
            positionInfo[tuple(next_position)].append(guardInfo[3])
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


realOnes = [(6, 4), (6, 6), (7, 6), (8, 2), (8, 4), (8, 7)]
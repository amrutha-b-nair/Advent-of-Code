import time

start_time = time.time()

with open('input.txt') as file:
    lines = file.read().strip().split('\n')



directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
grid = []
obstacles = []

for row, line in enumerate(lines):
    grid.append(list(line))
    for col, pos in enumerate(list(line)):
        if pos == "#":
            obstacles.append((row, col))
        elif pos != ".":
            guardPos = (row, col)

nrow = len(grid)
ncol = len(grid[0])



def getNextPos(pos, dir):
    return (pos[0] + directions[dir][0], pos[1] + directions[dir][1])

def outOfGrid(pos):
    return (pos[0] < 0 or pos[0] >= nrow or pos[1] < 0 or pos[1] >= ncol)

def formsLoop(currPos, dir, obstaclePos):
    posVisited = {}
    while(True):
        nextPos = getNextPos(currPos, dir)
        if outOfGrid(nextPos):
            return False
        
        if (nextPos in obstacles or nextPos == obstaclePos):
            dir = (dir + 1) % 4
            continue
        
        if (nextPos in posVisited and dir in posVisited[nextPos]):
            return True
        
        currPos = nextPos

        if currPos in posVisited:
            posVisited[currPos].append(dir)
        else:
            posVisited[currPos] = [dir]
        
       

    
dir = 0
currPos = guardPos

visited = []
newObstacles = []

while(True):
    visited.append(currPos)
    nextPos = getNextPos(currPos, dir)
    if outOfGrid(nextPos):
        break
    if nextPos in obstacles:
        dir = (dir + 1) % 4
        continue
    
    possibleObstacle = nextPos
    if possibleObstacle not in newObstacles and possibleObstacle not in visited:
        loopDetected = formsLoop(currPos, (dir + 1) % 4, possibleObstacle)
        if (loopDetected != False):
            newObstacles.append(possibleObstacle)

    currPos = nextPos
    
    


print(len(set(visited)), len(set(newObstacles)))
    
    


print("--- %s seconds ---" % (time.time() - start_time))

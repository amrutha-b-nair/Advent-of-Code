import heapq, copy, time


start_time = time.time()

with open('input.txt') as file:
    lines  = file.read().strip().split("\n")

grid = []
for row, line in enumerate(lines):
    grid.append(list(line))
    for col, value in enumerate(line):
        if value == "S":
            start = (row, col)
        elif value == "E":
            end = (row, col)

  
def dijkstra(grid, start, end):

    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    pq = [(0, start, [])] #steps, startPos, path
    visited = set()
    
    while pq:
        steps, (currRow, currCol), path = heapq.heappop(pq)
        
        if (currRow, currCol) == end:
            return steps, path
        
        if (currRow, currCol) in visited:
            continue
        visited.add((currRow, currCol))
        
        for dr, dc in directions:
            nextRow, nextCol = currRow + dr, currCol + dc
            
            if (0 <= nextRow < rows and 0 <= nextCol < cols and
                grid[nextRow][nextCol] != "#" and
                (nextRow, nextCol) not in visited):
                
                heapq.heappush(pq, (steps + 1, (nextRow, nextCol), path + [(nextRow, nextCol)]))
    
    return -1

def getPathNeighbours(grid, path):
    rows, cols = len(grid), len(grid[0])
    pathSet = set(path)
    neighbours = set()
    for (row, col) in pathSet:
        potential = [
        (row - 1, col),  
        (row + 1, col),  
        (row, col - 1),  
        (row, col + 1)]
        neighbours.update({
            (r, c) for r, c in potential
            if 0 <= r < rows and 0 <= c < cols
            and (r, c) not in neighbours
            and grid[r][c] == "#"
            })
        
    return neighbours

def getNeighbours(grid, pos):
    rows, cols = len(grid), len(grid[0])
    potential = [
    (pos[0] - 1, pos[1]),  
    (pos[0] + 1, pos[1]),  
    (pos[0], pos[1] - 1),  
    (pos[0], pos[1] + 1)]
    neighbours = [
        (r, c) for r, c in potential
        if 0 <= r < rows and 0 <= c < cols]
    
    return neighbours

def isNeighbourValid(grid, pos):
    neighbours = getNeighbours(grid, pos)
    for (row, col) in neighbours:
        if grid[row][col] == ".":
            return True
    return False


def getShotest(grid, start, end):
    gridCopy = copy.deepcopy(grid)
    steps, path = dijkstra(grid, start, end)
    neighbours = getPathNeighbours(grid, path)
    visited = []
    cheats = 0

    for neighbour in neighbours:
        gridCopy[neighbour[0]][neighbour[1]] = "."
        cheatCells = getNeighbours(grid, neighbour)
        for cell in cheatCells:
            if isNeighbourValid(grid, cell) and neighbour not in visited and cell not in visited:
                gridCopy[cell[0]][cell[1]] = "."
                newSteps, newPath = dijkstra(gridCopy, start, end)
                if newSteps <= 100:
                    cheats += 1
                visited += [neighbour, cell]

    return cheats   
        



steps, path = dijkstra(grid, start, end)
neighbours = getPathNeighbours(grid, path)

print(getShotest(grid, start, end))

print("--- %s seconds ---" % (time.time() - start_time))

from collections import deque, defaultdict

with open('input.txt') as file:
    lines  = file.read().strip().split("\n")

grid = []
for row, line in enumerate(lines):
    grid.append(list(line))
    for col, value in enumerate(line):
        if value == "S":
            start = (row, col)
            grid[row][col] = "."
        elif value == "E":
            end = (row, col)
            grid[row][col] = "."

def isValid(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def bfs(grid, start, end):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque([(start[0], start[1], 0, [start])])  # (row, col, steps_taken, path)
    visited = set()
    visited.add(start)
    
    while queue:
        r, c, steps, path = queue.popleft()
        
        if (r, c) == end:
            return steps, path
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if isValid(grid, nr, nc):
                if grid[r][c] != '#' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, steps + 1, path + [(nr, nc)]))
                
    
    return -1

def getNeighbours(r, c, rows, cols):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        return [
            (r + dr, c + dc) for dr, dc in directions
            if 0 <= r + dr < rows and 0 <= c + dc < cols
        ]


def getCheatCells(rows, cols, pos, d):
    x, y = pos
    result = set()
    for dx in range(-d, d + 1):
        for dy in range(-(d - abs(dx)), d - abs(dx) + 1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) != (x, y) and grid[nx][ny] != "#":
                result.add((nx, ny))
    return result

def distance(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x2 - x1) + abs(y2 - y1)


def getShotest(grid, start, end, cheatDist = 2, timeSaved = 100):
    rows, cols = len(grid), len(grid[0])
    steps, path = bfs(grid, start, end)
    pathInfo = {p: (len(path) - i - 1, i) for i, p in enumerate(path)}
    cheats = 0
    cheatDict = defaultdict(int)
    for pos in path:
        cheatCells = getCheatCells(rows, cols, pos, cheatDist)
        for cell in cheatCells:
            if pathInfo[cell][1] > pathInfo[pos][1]:
                stepsSaved = pathInfo[pos][0] - pathInfo[cell][0] - distance(pos, cell)
                if stepsSaved >= timeSaved:
                    cheats += 1          
                    cheatDict[stepsSaved] += 1      
    return cheats
        

print(getShotest(grid, start, end))
print(getShotest(grid, start, end, 20, 100))
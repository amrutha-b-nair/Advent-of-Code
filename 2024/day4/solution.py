with open('input.txt') as file:
    lines = file.read().strip().split('\n')

grid = [list(line) for line in lines]

nrows, ncols = len(grid), len(grid[0])

directions = [
        (-1, 0),
        (1, 0), 
        (0, -1),  
        (0, 1), 
        (-1, -1),
        (-1, 1), 
        (1, -1), 
        (1, 1) 
    ]

def insideGrid(x, y):
        return 0 <= x < nrows and 0 <= y < ncols

def XMASFound(x, y, direction, word = "XMAS"):
    dx, dy = direction
    for i in range(len(word)):
        nx, ny = x + i * dx, y + i * dy
        if ((not insideGrid(nx, ny)) or grid[nx][ny] != word[i]):
            return False
    return True

def XShapedMASFound(x, y):
    if grid[x][y] != "A":
        return False
    if insideGrid(x-1, y-1) and insideGrid(x+1, y+1) and insideGrid(x-1, y+1) and insideGrid(x+1, y-1):
        if (grid[x-1][y-1] == "M" and grid[x+1][y+1] == "S") or (grid[x-1][y-1] == "S" and grid[x+1][y+1] == "M"):
            if (grid[x-1][y+1] == "M" and grid[x+1][y-1] == "S") or (grid[x-1][y+1] == "S" and grid[x+1][y-1] == "M"):
                return True
    return False
    


XMASCount = 0
XShapedMASCount = 0

for x in range(nrows):
    for y in range(ncols):
        for direction in directions:
            if XMASFound(x, y, direction):
                XMASCount += 1

        if XShapedMASFound(x, y):
            XShapedMASCount += 1

            

print(XMASCount, XShapedMASCount)
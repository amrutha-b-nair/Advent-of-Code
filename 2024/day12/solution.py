import time

startTime = time.time()

with open("input.txt") as file:
    lines = file.read().strip().split("\n")

grid = []
for line in lines:
    grid.append(list(line))



def getNeighbours(grid, row, col):
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            neighbors.append((nr, nc))
    return neighbors

def dfs(grid, visited, row, col, plant):
    nrows, ncols = len(grid), len(grid[0])
    stack = [(row, col)]
    visited[row][col] = True
    area = 0
    perimeter = 0
    region = []
    while stack:
        r, c = stack.pop()
        region.append((r, c))
        area += 1
        if r == 0 or r == nrows -1:
            perimeter += 1
        if c == 0 or c == ncols -1:
            perimeter += 1
        for nr, nc in getNeighbours(grid, r, c):
            if grid[nr][nc] != plant:
                perimeter += 1
            elif not visited[nr][nc] and grid[nr][nc] == plant:
                visited[nr][nc] = True
                stack.append((nr, nc))
    return area, perimeter, region

def edges(positions):
    
    def countEdges(lines):
        return sum(
            sum(1 for i in range(len(sorted(line)) - 1) if sorted(line)[i + 1] - sorted(line)[i] > 1) + 1
            for line in lines.values()
        )

    north, south, west, east = {}, {}, {}, {}

    for x, y in positions:
        directions = {
            (x - 1, y): (north, x, y),
            (x + 1, y): (south, x, y),
            (x, y - 1): (west, y, x),
            (x, y + 1): (east, y, x),
        }
        for (nx, ny), (edge, key, value) in directions.items():
            if (nx, ny) not in positions:
                if key not in edge:
                    edge[key] = set()
                edge[key].add(value)

    return (
        countEdges(north) +
        countEdges(south) +
        countEdges(west) +
        countEdges(east)
    )



def totalPrice(grid):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    total = 0
    totalPartTwo = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if not visited[row][col]:
                plant = grid[row][col]
                area, perimeter, region = dfs(grid, visited, row, col, plant)
                sides = edges(region)
                total += area * perimeter
                totalPartTwo += area * sides
    
    return total, totalPartTwo


part1, part2 = totalPrice(grid)

print(part1, part2)

print("timeTaken: ", time.time() - startTime)








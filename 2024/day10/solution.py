from collections import deque

with open('input.txt') as file:
    lines = file.read().strip().split("\n")

grid = []
heads = []
ends = []
for i, line in enumerate(lines):
    grid.append([int(x) for x in list(line)])
    for j, val in enumerate(line):
        if val == "0":
            heads.append((i, j))
        elif val == "9":
            ends.append((i, j))


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def countPaths(grid, x, y, target, memo):
    if target == 10:
        return 1

    if (x, y, target) in memo:
        return memo[(x, y, target)]

    path_count = 0
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == target:
            path_count += countPaths(grid, nx, ny, target + 1, memo)

    memo[(x, y, target)] = path_count
    return path_count

def pathExists(grid, start, end):
    # (x, y, current number)
    queue = deque([(start[0], start[1], 0)])
    visited = set()

    while queue:
        x, y, current = queue.popleft()

        if (x, y) == end and current == 9:
            return True

        visited.add((x, y, current))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny, current + 1) not in visited:
                if grid[nx][ny] == current + 1:
                    queue.append((nx, ny, current + 1))

    return False


def total_paths(grid):
    headScore = 0
    totalPaths = 0
    memo = {}
    for start in heads:
        for end in ends:
            reachable = pathExists(grid, start, end)
            if reachable:
                headScore += 1
        pathCount = countPaths(grid, start[0],start[1], 1, memo)
        totalPaths += pathCount
    return headScore, totalPaths


part1, part2 = total_paths(grid)
print(part1, part2)

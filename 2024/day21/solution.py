from collections import deque
from functools import cache
import time

start_time = time.time()
with open('input.txt') as file:
    codes  = file.read().strip().split("\n")


numerical = [["7", "8", "9"], 
             ["4", "5", "6"],
             ["1", "2", "3"],
             ["#", "0", "A"]]

directional = [["#","^", "A"], 
               ["<", "v", ">"]]


dirs = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

def getPositions(grid):
    posDict = {}
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            posDict[grid[row][col]] = (row, col)
    
    return posDict

dirPos = getPositions(directional)
numPos = getPositions(numerical)


def distance(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x2 - x1) + abs(y2 - y1)

def bfs(grid, startPos, endPos):
    queue = deque([(startPos[0], startPos[1], "")])  # (row, col, path)
    visited = set()
    visited.add(startPos)

    while queue:
        r, c, path = queue.popleft()

        if (r, c) == endPos:
            return path + "A"
        
        for direction, (dr, dc) in dirs.items():
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#" and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, path + direction))
    
    return "No path found"

def bfsAll(grid, startPos, endPos):
    dirs = {
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
        "^": (-1, 0)
    }
    queue = deque([(startPos[0], startPos[1], "", 0)])  # (row, col, path, steps)
    shortest_distance = float('inf')
    all_paths = []
    visited = {}

    while queue:
        r, c, path, steps = queue.popleft()

        if steps > shortest_distance:
            continue

        if (r, c) == endPos:
            if steps < shortest_distance:
                shortest_distance = steps
                all_paths = [path]
            elif steps == shortest_distance:
                all_paths.append(path)
            continue

        for direction, (dr, dc) in dirs.items():
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#":
                if (nr, nc) not in visited or visited[(nr, nc)] >= steps + 1:
                    visited[(nr, nc)] = steps + 1
                    queue.append((nr, nc, path + direction, steps + 1))

    return all_paths if all_paths else ["No path found"]

@cache
def getCode(robot, start, target, depth):
    keyPad = numPos if robot == 0 else dirPos
    grid = numerical if robot == 0 else directional
    startPos, endPos = keyPad[start], keyPad[target]

    if robot ==  depth - 1:
        return distance(startPos, endPos) + 1
    
    if start == target:
        return 1
    
    path = bfs(grid, startPos, endPos)
    paths = bfsAll(grid, startPos, endPos)
    final = []
    for path in paths:
        steps = 0
        for i, dir in enumerate(path):
            steps += getCode(robot + 1, "A" if i == 0 else path[i-1], dir, depth)
        steps += getCode(robot + 1, path[-1], "A", depth)
        final.append(steps)
    return min(final)


depth = 3


total = 0
for code in codes:
    steps = getCode(0, "A", code[0], depth)
    for i in range(1, len(code)):
        steps += getCode(0, code[i-1], code[i], depth)
    total += steps*int(code[:-1])

print("Part 1:", total)


newDepth = 26

total = 0
for code in codes:
    steps = getCode(0, "A", code[0], newDepth)
    for i in range(1, len(code)):
        steps += getCode(0, code[i-1], code[i], newDepth)
    total += steps*int(code[:-1])

print("Part 2: ", total)

print("--- %s seconds ---" % (time.time() - start_time))

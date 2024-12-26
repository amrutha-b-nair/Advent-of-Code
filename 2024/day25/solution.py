
with open("input.txt") as file:
    grids = [grid.split("\n") for grid in file.read().strip().split("\n\n")]


locks = []
keys = []

rows, cols = len(grids[0]), len(grids[0][0])
print(rows, cols)

def getHeight(grid):
    heights = [0] * cols
    for row in grid:
        for i, cell in enumerate(row):
            if cell == '#':
                heights[i] += 1
    
    return heights


for grid in grids:
    
    if "." not in grid[0]:
        locks.append(getHeight(grid))
    elif "#" not in grid[0]:
        keys.append(getHeight(grid))

pairs = 0
for lock in locks:
    for key in keys:
        print(lock, key)
        print([a + b for a, b in zip(lock, key)])
        if all(x <= rows for x in [a + b for a, b in zip(lock, key)]):
            pairs += 1

print(pairs)
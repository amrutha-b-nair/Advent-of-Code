
with open('trial.txt') as file:
    lines = file.read().strip().split('\n')


bricks = []
highest_z = 0
for line in lines:
    start_raw, end_raw = line.split('~')
    start = tuple(int(coord) for coord in start_raw.split(','))
    end = tuple(int(coord) for coord in end_raw.split(','))
    bricks.append([start, end])
    if start[2]> highest_z: highest_z = start[2]
    print(line)


bricks_level = {i:[] for i in range(1, highest_z + 1)}

for brick in bricks:
    bricks_level[brick[0][2]].append(brick)

print(bricks_level)

fallen_bricks = bricks_level.copy()
for bricks in bricks_level:
    pass


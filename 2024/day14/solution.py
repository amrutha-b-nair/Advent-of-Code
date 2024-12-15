with open('input.txt') as file:
    lines = file.read().strip().split("\n")


# width = 11
# height = 7
width = 101
height = 103

quadrantCount = {1: 0, 2: 0, 3: 0, 4: 0}

def getQuadrant(x, y):
    mid_row = int((width - 1)/2)
    mid_col = int((height - 1)/2)
    if x < mid_row:
        if y < mid_col:
            quadrantCount[1] += 1
        elif y > mid_col:
            quadrantCount[2] += 1
    elif x > mid_row:
        if y < mid_col:
            quadrantCount[3] += 1
        elif y > mid_col:
            quadrantCount[4] += 1

def posAfterHundred(posX, posY, velX, velY):
    posX = (int(posX) + 100*int(velX)) % width
    posY = (int(posY) + 100*int(velY)) % height
    return posX, posY

robots = []

for line in lines:
    pos, vel = line.split(" ")
    posX, posY = pos[2:].split(",")
    velX, velY = vel[2:].split(",")
    robots.append([int(posX), int(posY), int(velX), int(velY)])
    posXAfter = (int(posX) + 100*int(velX)) % width
    posYAfter = (int(posY) + 100*int(velY)) % height
    getQuadrant(posXAfter, posYAfter)


total = 1

for value in quadrantCount.values():
    total*= value

print("Part 1: ", total)

def posAfter(time):
    return [((x + time*vx)%width, (y + time*vy)%height) for [x, y, vx, vy] in robots]
from statistics import variance

minX, minY, minVarX, minVarY = 0, 0, float('inf'), float('inf')

for t in range(max(width, height)):
    x, y = zip(*posAfter(t))
    varX = variance(x)
    varY = variance(y)
    if (varX < minVarX):
        minX, minVarX = t, varX
    if (varY < minVarY):
        minY, minVarY = t, varY




print("Part 2:", minX+((pow(width, -1, height)*(minY-minX)) % height)*width)
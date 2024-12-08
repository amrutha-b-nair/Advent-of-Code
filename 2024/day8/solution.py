from collections import defaultdict
with open('input.txt') as file:
    lines = file.read().strip().split("\n")

grid = []

antennas = {}

for row, line in enumerate(lines):
    grid.append(list(line))
    for col, element in enumerate(line):
        if element != ".":
            if element in antennas:
                antennas[element].append((row, col))
            else:
                antennas[element] = [(row, col)]


nrows = len(grid)
ncols = len(grid[0])


def outOfGrid(pos):
    return (pos[0] < 0 or pos[0] >= nrows or pos[1] < 0 or pos[1] >= ncols)


def insdieGrid(pos):
    return (0 <= pos[0] < nrows and 0 <= pos[1] < ncols)


def findAntinodes(pos1, pos2):
    diff = (pos1[0] - pos2[0], pos1[1] - pos2[1])
    antiNode1 = (pos1[0] + diff[0], pos1[1] + diff[1])
    antiNode2 = (pos2[0] - diff[0], pos2[1] - diff[1])
    result = []
    if insdieGrid(antiNode1):
        result.append(antiNode1)
    if insdieGrid(antiNode2):
        result.append(antiNode2)
    return result

def findAntiNodesPart2(pos1, pos2):
    result = []
    diff = (pos1[0] - pos2[0], pos1[1] - pos2[1])
    antiNode1 = pos1
    x=1
    while (insdieGrid(antiNode1)):
        result.append(antiNode1)
        antiNode1 = (pos1[0] + x*diff[0], pos1[1] + x*diff[1])
        x+=1

    y=1
    antiNode2 = pos2
    while (insdieGrid(antiNode2)):
        result.append(antiNode2)
        antiNode2 = (pos1[0] - y*diff[0], pos1[1] - y*diff[1])
        y+=1

    return result

antiNodes = []
antiNodesPart2 = []

for antenna in antennas:
    positions = antennas[antenna]
    if len(positions) > 1:
        for i, pos1 in enumerate(positions):
            for pos2 in positions[i+1:]:
                antiNodes += findAntinodes(pos1, pos2)

                antiNodesPart2 += findAntiNodesPart2(pos1, pos2)


print(len(set(antiNodes)), len(set(antiNodesPart2)))


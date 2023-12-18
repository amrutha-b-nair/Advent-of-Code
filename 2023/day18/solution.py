
def shoelace_area(vertices):
    area = 0
    for i in range(-1, len(vertices)-1):
        area += vertices[i][0]*(vertices[i+1][1] - vertices[i-1][1])
    return abs(area/2)

def volume_inside(vertices, count):
    area =  shoelace_area(vertices)
    total = area + 1 - (count//2)
    return int(total) 



with open('input.txt') as file:
    instructions = [line.split(' ') for line in file.read().strip().split('\n')]

directions = {'R': (0,1), 'L': (0, -1), 'U': (-1,0), 'D': (1,0)}
directions_two = {'0': (0,1), '2': (0, -1), '3': (-1,0), '1': (1,0)}

curr_pos = (0,0)
curr_pos_two = (0,0)

vertices = []
vertices_two = []
count = 0
count_two = 0
for instruction in instructions:
    curr_pos = tuple(x+(y*int(instruction[1])) for x, y in zip(curr_pos, directions[instruction[0]]))
    vertices.append(curr_pos)
    count += int(instruction[1])
    
    dir_two = directions_two[instruction[2][-2]]
    to_dig = int(instruction[2][2:-2], 16)
    curr_pos_two = tuple(x+(y*to_dig) for x, y in zip(curr_pos_two, dir_two))
    vertices_two.append(curr_pos_two)
    count_two += int(to_dig)

print('Part 1:',volume_inside(vertices, count) + count)
print('Part 2:',volume_inside(vertices_two, count_two) + count_two)

def shoelace_area(vertices):
    area = 0
    for i in range(-1, len(vertices)-1):
        area += vertices[i][0]*(vertices[i+1][1] - vertices[i-1][1])
    return abs(area/2)

# using Pick's theorem

def volume_inside(vertices, count):
    area =  shoelace_area(vertices)
    total = area + 1 - (count//2)
    return int(total) 

def get_vertices(instructions):
    curr_pos = (0,0)
    count = 0
    vertices = []
    for instruction in instructions:
        curr_pos = tuple(x+(y*instruction[1]) for x, y in zip(curr_pos, instruction[0]))
        vertices.append(curr_pos)
        count += instruction[1]
    return vertices, count

with open('input.txt') as file:
    instructions = [line.split(' ') for line in file.read().strip().split('\n')]



directions = {'R': (0,1), 'L': (0, -1), 'U': (-1,0), 'D': (1,0)}
directions_two = {'0': (0,1), '2': (0, -1), '3': (-1,0), '1': (1,0)}

part_one = []
part_two = []
for instruction in instructions:
    part_one.append([directions[instruction[0]], int(instruction[1])])
    dir_two = directions_two[instruction[2][-2]]
    to_dig = int(instruction[2][2:-2], 16)
    part_two.append([dir_two, to_dig])


vertices_part_one, count_part_one = get_vertices(part_one)
vertices_part_two, count_part_two = get_vertices(part_two)

print('Part 1:',volume_inside(vertices_part_one, count_part_one) + count_part_one)
print('Part 2:',volume_inside(vertices_part_two, count_part_two) + count_part_two)

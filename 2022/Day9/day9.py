
with open('input.txt') as file:
    motion_instructions = file.read().strip().split('\n')


def tail_neighbours(position):
    neighbours = []
    for i in range(-1,2):
        for j in range(-1,2):
            neighbours.append([position[0]- i, position[1]- j])
    return neighbours


def sign_movement(x):
    if x != 0:
        return x/abs(x)
    else:
        return 0

tail_row, tail_column = (0, 0)
head_row, head_column = (0, 0)

tail_positions = [(0,0)]

direction_movement = {'L':(-1, 0), 'R': (1,0), 'U': (0,1), 'D': (0,-1), 
'DRU': (1,1), 'DLU': (1, -1), 'DRD': ((-1,1)), 'DLD': (-1,-1)
}

for motion in motion_instructions:
    direction, value = motion.split(' ')
    for i in range(int(value)):
        head_row += direction_movement[direction][0]
        head_column += direction_movement[direction][1]
        if [head_row, head_column] not in tail_neighbours((tail_row, tail_column)):
            tail_row +=  sign_movement(head_row - tail_row )
            tail_column += sign_movement(head_column - tail_column)
        tail_positions.append((tail_row, tail_column))


print("Part 1:",len(set(tail_positions)))

knot_positions = [(0, 0) for i in range(9)]
head_row, head_column = (0, 0)

positions = [[(0,0)] for i in range(9)]

for motion in motion_instructions:
    direction, value = motion.split(' ')
    for i in range(int(value)):
        head_row += direction_movement[direction][0]
        head_column += direction_movement[direction][1]
        knot = tuple((head_row, head_column))

        for i in range(9):
            if list(knot) not in tail_neighbours(knot_positions[i]):
                knot_positions_list = list(knot_positions[i])
                knot_positions_list[0] +=  sign_movement(knot[0] - knot_positions[i][0])
                knot_positions_list[1] += sign_movement(knot[1] - knot_positions[i][1])
                knot_positions[i] = tuple(knot_positions_list)
            knot = knot_positions[i]
            positions[i].append(knot_positions[i])

print("Part 2:",len(set(positions[8])))




def tail_movements(motion_instructions):
    for i in range(int(value)):
        head_row += direction_movement[direction][0]
        head_column += direction_movement[direction][1]
        if (head_row, head_column) not in tail_neighbours(tail_row, tail_column):
            tail_row +=  sign_movement(head_row - tail_row )
            tail_column += sign_movement(head_column - tail_column)
        tail_positions.append((tail_row, tail_column))



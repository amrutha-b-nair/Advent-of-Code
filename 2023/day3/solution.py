

def get_neighbours(tuple, ncols, nrows):
    cols = sorted([tuple[i][1] for i in range(1, len(tuple))])
    neighbours = []
    for i in range(tuple[0]-1 , tuple[0]+2):
        for j in range(cols[0]-1, cols[-1] + 2):
            if 0 <= i < nrows and 0 <= j < ncols and (i,j) not in tuple:
                neighbours.append((i,j))
    return neighbours

with open('input.txt') as file:
    input_arr = [list(line) for line in file.read().strip().split('\n')]

nrows = len(input_arr)
ncols = len(input_arr[0])

symbols = []
numbers = {}
for i in range(nrows):
    number = ''
    indices = [i]
    for j in range(ncols):
        if not input_arr[i][j].isdigit() and input_arr[i][j] != '.':
            symbols.append((i,j))
            if number != '':
                numbers[tuple(indices)] = number
                number = ''
                indices = [i]
        elif input_arr[i][j].isdigit():
            number += input_arr[i][j]
            indices.append((i,j))
        elif input_arr[i][j] == '.':
            if number != '':
                numbers[tuple(indices)] = number
                number = ''
                indices = [i]
    if number != '':
        numbers[tuple(indices)] = number


part_sum = 0
part_numbers = []
for key, value in numbers.items():
    neighbours = get_neighbours(key, ncols, nrows)
    if len([indice for indice in neighbours if indice in symbols]) > 0:
        part_sum += int(value)
        part_numbers.append(int(value))

print("Part 1: ", part_sum)


gear_sum = 0
visited = []
for i in range(nrows):
    for j in range(ncols):
        if input_arr[i][j]== '*':
            neighbours = get_neighbours([i, (i,j)], ncols, nrows)
            neighbour_numbers = []
            for neighbour in neighbours:
                if neighbour not in visited and len(neighbour_numbers) < 2:
                    for key, value in numbers.items():
                        if neighbour in key:
                            neighbour_numbers.append(int(value))
                            visited += list(key[1:])
            if  len(neighbour_numbers) == 2:
                gear_sum += neighbour_numbers[0]*neighbour_numbers[1]

print("Part 2:", gear_sum)
                            
                            

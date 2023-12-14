import numpy as np 

def north_load(array):
    final_sum = 0
    nrows, ncols = array.shape
    for j in range(nrows):
        final_sum += np.count_nonzero(array[j] == 'O')*(ncols - j)
    return final_sum

def tilt_north(array):
    nrows, ncols = array.shape
    for j in range(ncols):
        empty_row = []
        for i in range(nrows):
            if array[i,j] == 'O':
                if len(empty_row)!= 0:
                    space = empty_row.pop(0)
                    array[space[0],j] = 'O'
                    array[i,j] = '.'
                    empty_row.append([i,j])
            elif array[i,j] == '.':
                empty_row.append([i,j])
            elif array[i,j] == '#':
                empty_row = []
    return array

def spin_cycle(array):
    for i in range(4):
        array = np.rot90(tilt_north(array), k = -1).copy()
    return array


with open('input.txt') as file:
    lines = [list(line) for line in file.read().strip().split('\n')]

input_data = np.array(lines)

nrows, ncols = input_data.shape
print(nrows, ncols)

round_rocks_rows, round_rocks_cols = np.where(input_data == 'O')

tilted_array = input_data

print('Part 1:',north_load(tilt_north(tilted_array)))

tilted_arrays = []
for i in range(200):
    tilted_array = spin_cycle(tilted_array)
    tilted_list = tilted_array.tolist()
    # print(north_load(tilted_array))
    if tilted_list in tilted_arrays:
        cycle_start = tilted_arrays.index(tilted_list)
        cycle_end = i  # excluding i
        break
    else:
        tilted_arrays.append(tilted_list)


total_cycles = 1000000000-1

index = (total_cycles - cycle_start) % (cycle_end  - cycle_start) + cycle_start

print(index)

print('Part 2:',north_load(np.array(tilted_arrays[index])))
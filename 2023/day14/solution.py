import numpy as np 

def north_load(array):
    final_sum = 0
    nrows, ncols = array.shape
    for j in range(nrows):
        # print()
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

def floyds_cycle_detection(values):
    tortoise = values[0]
    hare = values[0]

    while True:
        tortoise = values[tortoise]
        hare = values[values[hare]]

        if tortoise == hare:
            break

    tortoise = values[0]
    while tortoise != hare:
        tortoise = values[tortoise]
        hare = values[hare]

    return hare 





with open('input.txt') as file:
    lines = [list(line) for line in file.read().strip().split('\n')]

input_data = np.array(lines)

nrows, ncols = input_data.shape
print(nrows, ncols)

round_rocks_rows, round_rocks_cols = np.where(input_data == 'O')

tilted_array = input_data
# print('@@\n',tilted_array)
print(north_load(tilted_array))

# final_sum, tilted_array = north_load(tilted_array)


tilted_arrays = {}
for i in range(200):
    tilted_array = spin_cycle(tilted_array).copy()
    





# final_sum, tilted_array = north_load(tilted_array)

# print(tilted_array)
 
import numpy as np

def empty_indices(input_array):
    rows = []
    cols = []
    for i, line in enumerate(input_data):
        if '#' not in line:
            rows.append(i)
    for j, line in enumerate(input_data.T):
        if '#' not in line:
            cols.append(j)
    return rows, cols

def shortest_dist(input_data):
    empty_rows, empty_cols = empty_indices(input_data)
    row_indices, col_indices = np.where(input_data == '#')
    total_length = 0
    count = 0
    for i in range(len(row_indices) - 1):
        for j in range(i+1, len(row_indices)):
            for index in empty_rows:
                if row_indices[i] < index < row_indices[j] or row_indices[j] < index < row_indices[i]:
                    count += 1
            for index in empty_cols:
                if col_indices[i] < index < col_indices[j] or col_indices[j] < index < col_indices[i]:
                    count += 1
            total_length += abs(row_indices[i]-row_indices[j]) + abs(col_indices[i]-col_indices[j])
    return total_length, count

with open('input.txt') as file:
    lines = file.read().strip().split('\n')

input_data = np.array([list(line) for line in lines])

shortest_distance, count = shortest_dist(input_data)


print('Part 1:',shortest_distance + count)

print('Part 2:',shortest_distance + (1000000-1)*count)


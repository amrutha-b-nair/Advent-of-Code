
def get_min_cost(curr_cell, dir_prev = [None, None,(0,-1)]):
    visited = []
    if nrows == 1 and ncols == 1:
        # return arr[]
        pass


    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    min_value = float('inf')
    for direction in directions:
        if direction != dir_prev and len(set(dir_prev[1:] + [direction])) != 1:
            next_cell = tuple(x+y for x, y in zip(curr_cell, direction))
            print(next_cell)
            if 0 <= next_cell[0] < nrows and 0 <= next_cell[1] < ncols:
                value_dir = input_arr[curr_cell[0]][curr_cell[1]] + get_min_cost(next_cell, -direction)



    return min()

with open('trial.txt') as file:
    input_arr = [list(line) for line in file.read().strip().split('\n')]

nrows = len(input_arr)
ncols = len(input_arr[0])

memo_table = [[None for _ in range(nrows)] for _ in range(ncols)]
print(memo_table)
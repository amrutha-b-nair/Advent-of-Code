with open('input.txt') as file:
    lines = file.read().strip().split('\n')

grid = [list(line) for line in lines]

print(grid)
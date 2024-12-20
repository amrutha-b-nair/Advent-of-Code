
with open('trial.txt') as file:
    lines = file.read().strip().split('\n')

curr_pos = (0,0)
curr_dir = (0,1)
print(tuple(x+y for x, y in zip(curr_pos, curr_dir)))

for line in lines:
    pass
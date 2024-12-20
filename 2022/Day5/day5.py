from collections import defaultdict
from copy import deepcopy

with open('input.txt') as file:
    input_data = file.read().split('\n\n')


crates_stack = input_data[0].split("\n")
procedure_rearrangement = input_data[1].strip().split('\n')
stack_numbers = crates_stack.pop(-1).split("  ")

stack_height = len(stack_numbers)


stacked_columns = defaultdict(list)

for stacks in crates_stack:
    crates = stacks.replace("    ", " ").split(" ")
    for i in range(stack_height):
        if crates[i]!= '':
            stacked_columns[i].insert(0, crates[i])



procedures = [
    procedure_rearrangement[i].split(" ") for i in range(len(procedure_rearrangement))
]

stacked_columns_new = deepcopy(stacked_columns)
for procedure in procedures:
    i = int(procedure[1])
    while i != 0:
        stacked_columns[int(procedure[5])-1].append(stacked_columns[int(procedure[3])-1].pop(-1))
        i = i-1

top_crates = ''.join([stacked_columns[i][-1][1] for i in range(stack_height)])

print("Part 1:", top_crates)


for procedure in procedures:
    i = int(procedure[1])
    l = len(stacked_columns_new[int(procedure[3])-1])
    crates_to_move = stacked_columns_new[int(procedure[3])-1][l-i:l] 
    stacked_columns_new[int(procedure[3])-1] = stacked_columns_new[int(procedure[3])-1][0:l-i]  
    stacked_columns_new[int(procedure[5])-1] = stacked_columns_new[int(procedure[5])-1] + crates_to_move

top_crates_new = ''.join([stacked_columns_new[i][-1][1] for i in range(stack_height)])

print("Part 2:", top_crates_new)
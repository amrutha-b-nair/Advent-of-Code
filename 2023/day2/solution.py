import re
from functools import reduce 
import operator

with open('input.txt') as file:
    lines = file.read().strip().split('\n')

######################## part 1 ###################

game_id_sum = 0 
possible_cubes = {'red':12, 'blue':14, 'green':13}
for line in lines:
    new_line = re.split('; |, |: | |\n',line)
    for i in range(3, len(new_line), 2):
        if int(new_line[i-1]) > possible_cubes[new_line[i]]:
            game_id_sum += int(new_line[1])
            break
print(int(len(lines)*(len(lines)+1)/2 -  game_id_sum))

######################## part 2 ######################


total_power = 0
for line in lines:
    number_cubes = {'red':0, 'blue':0, 'green':0}
    new_line = re.split('; |, |: | |\n',line)
    for i in range(3, len(new_line), 2):
        number_cubes[new_line[i]] = max(number_cubes[new_line[i]], int(new_line[i-1]))
    total_power += reduce(operator.mul, number_cubes.values(), 1)

print(total_power)
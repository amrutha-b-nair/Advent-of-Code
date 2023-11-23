
with open('input.txt') as file:
    instructions_raw = file.read().strip().split('\n')

instructions = []
for instruction in instructions_raw:
    instructions.append(instruction.split(" "))

length = len(instructions)

X = 1
cycle_number = 0

signal_strengths = []

for instruction in instructions:

    if len(instruction) == 1:
        cycle_number += 1
        if ((cycle_number -20) % 40) == 0:
            signal_strengths.append((cycle_number, X))

    elif len(instruction) ==2:
        cycle_number += 2
        extra_cycle = (cycle_number - 20) % 40
        if extra_cycle in {0, 1}:
            signal_strengths.append((cycle_number - extra_cycle,  X))
        X += int(instruction[1])


signal_strength = sum([(x*y) for x, y in signal_strengths])

print(cycle_number)

print("Part 1:", signal_strength)

number_rows = cycle_number // 40

def draw_pixel(cycle_number, sprite_positions, CRT):
    
    row =  ((cycle_number - 1)//40)
    if int((cycle_number - 1) % 40) in sprite_positions:
        CRT[row].append('#')
    else:
        CRT[row].append('.')

sprite_positions = [0, 1, 2]
Y = 1
cycle_number_new = 0
CRT = [[] for i in range(number_rows)]



for instruction in instructions:
    
    if len(instruction) == 1:
        cycle_number_new += 1
        draw_pixel(cycle_number_new, sprite_positions, CRT)

    elif len(instruction) ==2:
        for i in range(2):
            cycle_number_new += 1
            draw_pixel(cycle_number_new, sprite_positions, CRT)
        
        Y += int(instruction[1])
        print("X", Y)
        sprite_positions = [Y-1, Y, Y+1]


for row in CRT:
    print(''.join(row))

# print(CRT)

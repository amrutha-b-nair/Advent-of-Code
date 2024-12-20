def get_hash_value(string):
    return sum([(ord(char))*(17**(len(string)-i))%256  for i,char in enumerate(string)])%256

with open('input.txt') as file:
    input = file.read().strip().split(',')



total_hash_value = 0
for string in input:
    total_hash_value += get_hash_value(string)


print('Part 1:',total_hash_value)


boxes = {}
for instruction in input:
    if '=' in instruction:
        lens_to_insert = instruction.split('=')
        box_number = get_hash_value(lens_to_insert[0])
        if box_number in boxes:
            existing_lens = [boxes[box_number].index(lens) for lens in boxes[box_number] if lens_to_insert[0] in lens]
            if len(existing_lens) == 0:
                boxes[box_number] += [lens_to_insert]
            else:
                boxes[box_number][existing_lens[0]] = lens_to_insert
        else:
            boxes[box_number] = [lens_to_insert]
        
            
    elif '-' in instruction:
        label = instruction[:-1]
        box_number = get_hash_value(label)
        if box_number in boxes:
            boxes[box_number] = [lens for lens in boxes[box_number] if label not in lens]


focusing_power = 0

for key, value in boxes.items():
    if len(value)!= 0:
        for i,lens in enumerate(value):
            focusing_power += (key+1)*(i+1)*int(lens[1])

print('Part 2:',focusing_power)
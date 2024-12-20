
with open('input.txt') as file:
    lines = file.read().strip().split('\n')

total_value = 0

###################### part 1 #########################

# for line in lines:
#     calibration_value = ''
#     for i in range(len(line)):
#         if line[i].isdigit():
#             calibration_value+= line[i]
#             break
#     for i in range(len(line)):
#         if line[len(line)-i-1].isdigit():
#             calibration_value += line[len(line)-i-1]
#             break
#     total_value += int(calibration_value)
# print(total_value)


###################### part 2 #########################

spelled_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for line in lines:
    for i in range(len(spelled_numbers)):
        if spelled_numbers[i] in line:
            line = line.replace(spelled_numbers[i], spelled_numbers[i][0]+str(i+1) + spelled_numbers[i][-1])
    calibration_value = ''
    for i in range(len(line)):
        if line[i].isdigit():
            calibration_value+= line[i]
            break
    for i in range(len(line)):
        if line[len(line)-i-1].isdigit():
            calibration_value += line[len(line)-i-1]
            break
    total_value += int(calibration_value)
print(total_value)
from itertools import takewhile
import numpy as np


def is_palindrome(lines, index):
    palindrom_dict ={}
    for i in range(index):
        if lines[i] not in palindrom_dict:
            palindrom_dict[lines[i]] = 1
        else:
            del palindrom_dict[lines[i]]
    if len(palindrom_dict) == 0:
        return True
    else:
        return False

def row_reflection(lines):
    possible_indices = [i for i in range(1, len(lines)) if lines[0] == lines[i]]
    if len(possible_indices) == 0:
        return None
    else:
        for index in possible_indices:
            if is_palindrome(lines, index + 1):
                return (index +1)//2
    return None


def get_summary(input_data):
    reflection_lines = []
    summerize = 0
    for input in input_data:
        lines = input.split('\n')
        for i in range(4):
            arr = np.array([list(row) for row in lines])
            rotated = [''.join(row) for row in np.rot90(arr, k = i)]
            index = row_reflection(rotated)

            if index != None:
                reflection_lines.append([i,index])
                if i == 0:
                    summerize += index*100 
                elif i == 1:
                    summerize += len(rotated) - index
                elif i == 2:
                    summerize += (len(rotated) - index)*100
                elif i == 3:
                    summerize += index
                break

    return summerize, reflection_lines

            

def smudged_line(lines):
    for i in range(len(lines)-1):
        for j in range(i + 1, len(lines)):
            diff_count = sum(x != y for x, y in zip(lines[i], lines[j]))
            if diff_count == 1:
                index = next(k for k, (x, y) in enumerate(zip(lines[i], lines[j])) if x != y)
                char_map = {'#': '.', '.': '#'}
                new_lines = lines.copy()
                new_lines[i] = lines[i][:index] + char_map.get(lines[i][index], lines[i][index]) + lines[i][index + 1:]
                index = row_reflection(new_lines)
                if index != None:
                    return index
    return None


def get_smudged_summary(input_data, reflection_lines):
    summerize = 0
    for j,input in enumerate(input_data):
        lines = input.split('\n')
        for i in range(4):
            arr = np.array([list(row) for row in lines])
            rotated = [''.join(row) for row in np.rot90(arr, k = i)]
            index = smudged_line(rotated)
            if index != None and reflection_lines[j] != [i,index]:
                if i == 0:
                    summerize += index*100 
                elif i == 1:
                    summerize += len(rotated) - index
                elif i == 2:
                    summerize += (len(rotated) - index)*100
                elif i == 3:
                    summerize += index
                break
    return summerize



with open('input.txt') as file:
    input_data = file.read().strip().split('\n\n')


summary, reflection_lines = get_summary(input_data)
print('Part 1:',summary)
print('Part 2:', get_smudged_summary(input_data, reflection_lines))
from itertools import takewhile
import numpy as np

def is_reflection(count_list):

    leading_zeros = len(list(takewhile(lambda x: x == 0, count_list)))
    trailing_zeros = len(list(takewhile(lambda x: x == 0, reversed(count_list))))
    if leading_zeros != 0:
        return leading_zeros
    elif trailing_zeros != 0:
        return (len(count_list) - trailing_zeros)
    else:
        return 0

def row_reflection(lines):
    visited = []
    indices = [1 for _ in range(len(lines))]
    palindrome = False
    palindrome_start = None
    for i,line in enumerate(lines):
        if line not in visited:
            # print('$$$$', i)
            visited.append(line)
            if palindrome:
                # print('palindrome')
                if lines[i-1] == lines[0]:
                    # print('!!!!!!!!!!',i)
                    return i//2
                
                for k in range(i):
                    indices[k] = 1
                palindrome = False
        else:
            if palindrome:
                if indices[i-1] != 0:
                    # print('#####',i)
                    indices[i] = 1
                    palindrome = False
                else:
                    if lines[i] == lines[2*palindrome_start - i- 1]:
                        # print('^^^^^',i)
                        indices[i] = 0

            elif palindrome == False:
                if visited[-1] == line:
                    palindrome_start = i
                    # print('&&&&', i)
                    palindrome = True
                    indices[i] = 0
                else:
                    # print('((()))', i)
                    visited.append(line)

    # print(indices)
    return is_reflection(indices)

def col_reflection(lines):
    arr = np.array([list(row) for row in lines])
    transposed = [''.join(row) for row in arr.T]
    return row_reflection(transposed)

def get_summary(input_data):
    summerize = 0
    for input in input_data:
        # print(input, '\n\n')
        lines = input.split('\n')
        nrows = row_reflection(lines)
        if nrows == 0:
            ncols = col_reflection(lines)
            summerize += ncols
        else:
            # print(nrows)
            summerize += 100*(nrows)
    return summerize


# def get_smudged_summary(input_data):
#     for input in input_data:
#         lines = input.split('\n')
#         for i in range(len(lines)):
#             for j in range(i, len(lines)):
#                 difference = 0
#                 for k in range(len(lines[i])):
#                     if lines[i][k] != lines[j][k]:
#                         difference += 1
#                         if difference > 1:
#                             break




with open('trial.txt') as file:
    input_data = file.read().strip().split('\n\n')


print(get_summary(input_data))
print(get_smudged_summary(input_data))
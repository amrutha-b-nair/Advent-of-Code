from collections import defaultdict
from copy import deepcopy

with open('input.txt') as file:
    terminal_output = file.read().strip().split('\n')


output = []
for line in terminal_output:
    output.append(line.split(" "))

length_output = len(output)

directory_tree = defaultdict(list)
path_folders = []

k = 0
i = 0

while i < length_output:
    if output[i][1] == 'cd':
        if output[i][2] == '..':
            k = k - 1
        else:
            directory = output[i][2]
            if len(path_folders) == 0:
                path_folders.insert(k, directory + '|')
            else:
                path_folders.insert(k, path_folders[k-1] + directory + '|')

            j = i+2
            while j < length_output and output[j][0]!= '$':
                if output[j][0].isdigit():
                    directory_tree[path_folders[k]].append(int(output[j][0]))
                elif output[j][0] == 'dir':
                    directory_tree[path_folders[k]].append(path_folders[k] + output[j][1] + '|')
                j = j+1
            i = j-1
                       
            k = k + 1


    i +=1



directory_tree_new = deepcopy(directory_tree)

def nested_directory(tree, tree_new, directory):
    for i in range(len(tree[directory])):

        if str(tree[directory][i]).isdigit() == False:
            tree_new[directory][i] = nested_directory(tree, tree_new, tree[directory][i])

    return sum(tree_new[directory])

for key in directory_tree:
    nested_directory(directory_tree, directory_tree_new, key)
    directory_tree_new[key] = sum(directory_tree_new[key])


size_directories  = 0
for key in directory_tree_new.keys():
    if directory_tree_new[key] < 100000:
        size_directories += int(directory_tree_new[key])


print("Part 1:",size_directories)

total_size = directory_tree_new['/|']
total_unused = 70000000 - total_size
size_to_delete = 30000000 - total_unused
smallest_to_delete = total_size

for key in directory_tree_new.keys():
    if directory_tree_new[key] > size_to_delete:
        smallest_to_delete = min(smallest_to_delete, directory_tree_new[key])

print("Part 2:", smallest_to_delete)
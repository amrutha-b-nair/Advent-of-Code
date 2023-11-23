
import numpy as np
from collections import defaultdict

with open('input.txt') as file:
    height_map_raw = file.read().strip().split('\n')


height_map = [list(item) for item in height_map_raw]

col_length = len(height_map[0])
row_length = len(height_map)


height_map.insert(0, ['z' for i in range(len(height_map[0]))])
height_map.append(['z' for i in range(len(height_map[0]))])

for i in range(len(height_map)):
    height_map[i].insert(0, 'z')
    height_map[i].append('z')


def get_index(height_map, value, col_length, row_length):
    for i in range(1, row_length + 1):
        for j in range(1, col_length + 1):
            if height_map[i][j] == value:
                return (i, j)


def neighbours_to_visit(i, j, height_map):
    neighbours = []
    value = height_map[i][j]
    if value == 'S':
        height = 97
    elif value == 'E':
        height = 122
    else:
        height = ord(height_map[i][j])
    neighbours_index = [(-1, 0), (1, 0), (0, 1), (0, -1) ]
    for k, l in neighbours_index:

        if (ord(height_map[i + k][j + l]) - height) <= 1:
            neighbours.append((i + k, j + l))
    return neighbours


def BFS(graph, start, end):
    visited = set()
    queue = start
    for value in start:
        if value == end:
            return start

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == end:
                    return new_path

            visited.add(node)
            

    return []



index_start = get_index(height_map, 'S', col_length, row_length)
index_end = get_index(height_map, 'E', col_length, row_length)

height_map[index_start[0]][index_start[1]] = 'a'
height_map[index_end[0]][index_end[1]] = 'z'


graph_heights = defaultdict(list)

for i in range(1, row_length + 1):
    for j in range(1, col_length + 1):
        graph_heights[(i, j)] = neighbours_to_visit(i, j, height_map)

shortest_path = BFS(graph_heights, [[index_start]], index_end)
print("Part 1",len(shortest_path) - 1)
    


lowest_elevation = []
for i in range(1, row_length + 1):
    for j in range(1, col_length + 1):
        if height_map[i][j] == 'a':
            lowest_elevation.append([(i, j)])

shortest_path_multi = BFS(graph_heights, lowest_elevation, index_end)
print("Part 2",len(shortest_path_multi) - 1)
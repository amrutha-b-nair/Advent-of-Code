def get_start(maze):
    start = [i for i, value in enumerate(maze[0]) if value!= '#']
    return start[0]

def possible_neighbours(maze, curr_pos, visited):
    nrows, ncols = len(maze), len(maze[0])
    slopes = {'<':(0, -1), '>':(0, 1), 'v':(1, 0), '^':(-1,0)}
    if maze[curr_pos[0]][curr_pos[1]] in slopes.keys():
        next_pos = tuple(x+y for x,y in zip(slopes[maze[curr_pos[0]][curr_pos[1]]], curr_pos))
        if maze[next_pos[0]][next_pos[1]] != '#' and 0 <= next_pos[0] < nrows and 0 <= next_pos[1] < ncols and next_pos not in visited:
            return next_pos 
    moves = [(1,0), (0,1), (-1,0), (0,-1)]
    neighbours = []
    for move in moves:
        next_pos = tuple(x+y for x,y in zip(move, curr_pos))
        if maze[next_pos[0]][next_pos[1]] != '#' and 0 <= next_pos[0] < nrows and 0 <= next_pos[1] < ncols and next_pos not in visited:
            neighbours.append(next_pos)
    return neighbours

def dfs(maze, start, visited = {}):
    visited.add(start)
    neighbours = possible_neighbours(maze, start, visited) 
    for neighbour in neighbours:
        path_length += 1
        path_length = max(path_length, dfs(maze, neighbour, visited))


with open('trial.txt') as file:
    lines = file.read().strip().split('\n')

maze = []
for line in lines:
    maze.append(list(line))

nrows, ncols = len(maze), len(maze[0])

# print(get_start(maze))
# print(possible_neighbours(maze, (3,10), []))


# # DFS algorithm
# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)

#     print(start)

#     for next in graph[start] - visited:
#         dfs(graph, next, visited)
#     return visited


# graph = {'0': set(['1', '2']),
#          '1': set(['0', '3', '4']),
#          '2': set(['0']),
#          '3': set(['1']),
#          '4': set(['2', '3'])}

# dfs(graph, '0')
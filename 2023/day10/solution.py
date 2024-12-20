def get_neighbours(coords, ncols, nrows):
    return [(coords[0], j) for j in [coords[1]-1, coords[1]+1] if 0<=j<ncols] + [(i, coords[1]) for i in [coords[0]-1, coords[0]+1] if 0<=i<nrows]

def useful_neighbours(node, coords):
    directions = {'|': {'N','S'},'7':{'W','S'}, 'J':{'N','W'},'-':{'W','E'},'L':{'N','E'},'F':{'E','S'}}
    direction = directions[node]
    neighbours = []
    direction_coord = {'N':(-1,0), 'S': (1,0), 'W':(0,-1), 'E':(0,1)}
    for dir in direction:
        neighbours.append(tuple(a+b for a, b in zip(direction_coord[dir],coords)))
    return neighbours

def get_start(lines):
    arr = [list(line) for line in lines.split('\n')]
    nrows = len(arr)
    ncols = len(arr[0])
    starting_node = 'S'
    starting_coord = [(i,j) for i in range(nrows) for j in range(ncols) if arr[i][j] == starting_node][0]
    return arr, starting_node, starting_coord

def starting_neighbours(arr, starting_node, starting_coord):
    nrows = len(arr)
    ncols = len(arr[0])
    path_nodes = [[starting_node] for _ in range(2)]
    path_coords = [[starting_coord] for _ in range(2)]
    index = 0
    all_neighbours = get_neighbours(starting_coord, ncols, nrows)
    for neighbour_coord in all_neighbours:
        neighbour = arr[neighbour_coord[0]][neighbour_coord[1]]
        if  neighbour!= '.':
            if starting_coord in useful_neighbours(neighbour, neighbour_coord):
                path_nodes[index].append(neighbour)
                path_coords[index].append(neighbour_coord)
                index += 1
    return path_nodes, path_coords

def path_length(arr, path_nodes, path_coords):
    path_length = 1
    while True:
        for i in range(2):
            next_coord = [coord for coord in useful_neighbours(path_nodes[i][1], path_coords[i][1]) if coord != path_coords[i][0]][0]
            path_coords[i].append(next_coord)
            path_nodes[i].append(arr[next_coord[0]][next_coord[1]])
            path_nodes[i].pop(0)
            path_coords[i].pop(0)
        path_length += 1
        if len(set(path_coords[0]) & set(path_coords[1])) != 0:
            return path_length


def part_one(lines):
    arr, starting_node, starting_coord = get_start(lines)
    path_nodes, path_coords = starting_neighbours(arr, starting_node, starting_coord)
    return path_length(arr, path_nodes, path_coords)

def get_path(arr, path_nodes, path_coords):
    while True:
        next_coord = [coord for coord in useful_neighbours(path_nodes[0][-1], path_coords[0][-1]) if coord != path_coords[0][-2]]
        if arr[next_coord[0][0]][next_coord[0][1]] == 'S':
            return path_coords[0]
        path_coords[0].append(next_coord[0])
        path_nodes[0].append(arr[next_coord[-1][0]][next_coord[-1][1]])

def shoelace_area(vertices):
    area = 0
    for i in range(-1, len(vertices)-1):
        area += vertices[i][0]*(vertices[i+1][1] - vertices[i-1][1])
    return abs(area/2)

def part_two(lines):
    arr, starting_node, starting_coord = get_start(lines)
    path_nodes, path_coords = starting_neighbours(arr, starting_node, starting_coord)
    path = get_path(arr, path_nodes, path_coords)
    area =  shoelace_area(list(path))
    inside = area + 1 - ((len(path))/2)
    return int(inside)


with open('trial.txt') as file:
    lines = file.read().strip()

print(lines)


print(part_one(lines))
print(part_two(lines))

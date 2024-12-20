import numpy
with open('input.txt') as file:
    tree_height_map = file.read().strip().split('\n')

tree_matrix = []
for row in tree_height_map:
    tree_matrix.append(list(row))


row_length = len(tree_matrix)
column_length = len(tree_matrix[0])

edge_trees = 2*(column_length + row_length - 2)

def get_neighbours(tree_matrix, i, j):
    neighbours_left = [int(tree_matrix[i][k]) for k in range(0, j )]
    neighbours_right = [int(tree_matrix[i][k]) for k in range(j+1, column_length)]
    neighbours_above = [int(tree_matrix[k][j]) for k in range(0, i)]
    neighbours_below = [int(tree_matrix[k][j]) for k in range(i+1, row_length)]
    neighbours_max = [max(neighbours_left), max(neighbours_right), max(neighbours_above), max(neighbours_below)]
    neighbours = [neighbours_left, neighbours_right, neighbours_above, neighbours_below]
    return neighbours, neighbours_max

visible_count = 0
for i in range(1, row_length-1):
    for j in range(1, column_length-1):
        tree_neighbours = get_neighbours(tree_matrix, i, j)[1]
        if min(tree_neighbours) < int(tree_matrix[i][j]):
            visible_count += 1


print("Part 1:", visible_count + edge_trees)


def scenic_score(tree_matrix, i, j):
    tree_neighbours = get_neighbours(tree_matrix, i, j)[0]
    score =[0,0,0,0]
    
    for k in {0,2}:
        score[k] = len(tree_neighbours[k])
        for index, tree in enumerate(reversed(tree_neighbours[k])):
            if tree >= int(tree_matrix[i][j]):
                score[k] = index + 1
                break 

    for k in {1,3}:
        score[k] = len(tree_neighbours[k])
        for index, tree in enumerate(tree_neighbours[k]):
            if tree >= int(tree_matrix[i][j]):
                score[k] = index + 1
                break 
            

    final_score = numpy.prod(score)
    return final_score


highest_score = 0
for i in range(1, row_length-1):
    for j in range(1, column_length-1):
        highest_score = max(scenic_score(tree_matrix, i, j), highest_score)

print("Part 2:", highest_score)
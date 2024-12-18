import heapq

with open('input.txt') as file:
    currupted = [tuple(map(int, value.split(","))) for value in file.read().strip().split("\n")]


def printGrid(gridSize, obstacles):
    for i in range(gridSize[0]):
        for j in range(gridSize[1]):
            if (i,j) in obstacles:
                print("#", end="")
            else: print(".", end="")
        print("\n")

def dijkstra(gridSize, obstacles, start, end):

    rows, cols = gridSize
    obstacleSet = set(obstacles)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    pq = [(0, start)]
    visited = set()
    
    while pq:
        steps, (currRow, currCol) = heapq.heappop(pq)
        
        if (currRow, currCol) == end:
            return steps
        
        if (currRow, currCol) in visited:
            continue
        visited.add((currRow, currCol))
        
        for dr, dc in directions:
            nextRow, nextCol = currRow + dr, currCol + dc
            
            if (0 <= nextRow < rows and 0 <= nextCol < cols and
                (nextRow, nextCol) not in obstacleSet and
                (nextRow, nextCol) not in visited):
                
                heapq.heappush(pq, (steps + 1, (nextRow, nextCol)))
    
    return -1


def firstImpossible(gridSize, obstacles, start, end):

    def pathExists(index):

        path = dijkstra(gridSize, obstacles[:index + 1], start, end)
        return path != -1

    left, right = 0, len(obstacles) - 1
    result = None

    while left <= right:
        mid = (left + right) // 2
        if pathExists(mid):
            left = mid + 1
        else:
            result = obstacles[mid]
            right = mid - 1

    return result



# size = 6
# fallingBytes = 12
size = 70
fallingBytes = 1024

shortest_steps = dijkstra((size+1, size+1), currupted[:fallingBytes], (0, 0), (size, size))
print("Part 1:", shortest_steps)

byte = firstImpossible((size+1, size+1), currupted, (0, 0), (size, size))
print("Part 2:", byte)
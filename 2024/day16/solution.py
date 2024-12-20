import heapq
from collections import defaultdict

with open('input.txt') as file:
    lines  = file.read().strip().split("\n")

grid = []

for row, line in enumerate(lines):
    grid.append(list(line))
    for col, value in enumerate(line):
        if value == "S":
            start = (row, col)
        elif value == "E":
            end = (row, col)

grid[end[0]][end[1]] = "."


def dijkstra_all_best_paths(maze, start, end):
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
    rows, cols = len(maze), len(maze[0])
    
    pq = [(0, start, 0, [], 0)]  # Cost, Position, Direction, Path, Turns
    
    best_cost = defaultdict(lambda: float('inf')) 
    best_paths = defaultdict(list)
    turn_counts = defaultdict(int)
    
    while pq:
        cost, (current_row, current_col), current_dir, path, turns = heapq.heappop(pq)
        
        if cost > best_cost[((current_row, current_col), current_dir)]:
            continue
        
        if (current_row, current_col) == end:
            best_paths[cost].append(path)
            turn_counts[cost] = turns
            continue
        
        for i, (dr, dc) in enumerate(directions):
            next_row, next_col = current_row + dr, current_col + dc
            new_turns = turns + (1 if current_dir != i else 0)
            new_cost = 1000 * new_turns + len(path)
            
            if (0 <= next_row < rows and 0 <= next_col < cols and
                maze[next_row][next_col] == "."):
                
                state = ((next_row, next_col), i)
                if new_cost < best_cost[state]:
                    best_cost[state] = new_cost
                    heapq.heappush(pq, (new_cost, (next_row, next_col), i, path + [(next_row, next_col)], new_turns))
                
                elif new_cost == best_cost[state]:
                    heapq.heappush(pq, (new_cost, (next_row, next_col), i, path + [(next_row, next_col)], new_turns))
    
    min_cost = min(best_paths.keys(), default=None)
    return (best_paths[min_cost], turn_counts[min_cost]) if min_cost is not None else []



paths, turns = dijkstra_all_best_paths(grid, start, end)
print(len(paths[0]), turns)
print("Part 1:", len(paths[0]) + 1000*turns)
unique_cells = {cell for path in paths for cell in path}
print("Part 2:", len(unique_cells) + 1)


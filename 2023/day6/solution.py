import math

def winning_races(total_time, record_distance): 
    root1 = ((total_time + ((total_time**2 -4*record_distance)**(1/2)))/2 - 0.05) 
    root2 = ((total_time - ((total_time**2 -4*record_distance)**(1/2)))/2 + 0.05)
    return math.floor(root1)-math.ceil(root2) + 1

with open("input.txt") as file:
    lines = file.read().strip().split('\n')

times = [value for value in lines[0].split(' ')[1:] if value != '']
distances = [value for value in lines[1].split(' ')[1:] if value != '']

product_records = 1
for i in range(len(times)):
    product_records *= winning_races(int(times[i]), int(distances[i]))

print("Part 1:", product_records)

actual_time = int(''.join(times))
actual_distance = int(''.join(distances))

print("Part 2:", winning_races(actual_time, actual_distance))
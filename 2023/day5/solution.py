import re


def next_category(maps, seed_number):
    for map in maps:
        if seed_number in range(map[1], map[1]+map[2]):
            return map[0] + seed_number - map[1]
    return seed_number

def mapping(conversion, seed_number):
    source_number = seed_number
    for key, maps in conversion.items():
        source_number = next_category(maps, source_number) 
    return source_number

def get_range(maps):
    intervals = []
    for map in maps:
        intervals.append([[map[1], map[1]+ map[2]], [map[0], map[0]+ map[2]]])
    intervals.sort(key=lambda x: x[0][0])
    l = len(intervals)
    if intervals[0][0][0] > 0:
        intervals.append([[0, intervals[0][0][0]]]*2)    
    for i in range(l - 1):
        if intervals[i][0][1] != intervals[i+1][0][0]:
            intervals.append([[intervals[i][0][1], intervals[i+1][0][0]]]*2)
    return intervals

def next_range(maps, seed_range):
    seed_range = sorted(seed_range)
    intervals = get_range(maps)
    for interval in intervals:
        if interval[0][0] <= seed_range[0] < interval[0][1]:
            if seed_range[1] < interval[0][1]:
                return [[next_category(maps, seed_range[i]) for i in range(2)]]
            else:
                return [[next_category(maps, seed_range[0]), interval[1][1]]] + next_range(maps, [interval[0][1], seed_range[1]])
    return [seed_range]

def mapping_range(conversion, seed_intervals):
    intervals = [seed_intervals]
    for key, maps in conversion.items():
        interval_tent = []
        for interval in intervals:
            ranges = next_range(maps, interval)
            interval_tent += ranges
        intervals = interval_tent
    return intervals


with open('input.txt') as file:
    lines = file.read().strip().split('\n\n')

seed_numbers = [int(line) for line in lines.pop(0).split(' ')[1:]]
conversion = {}
categories = []
for line in lines:
    parsed_map = re.split(r'[:\n]', line)
    category = parsed_map.pop(0).split(' ')[0].split('-to-')[1]
    categories.append(category)
    conversion[category] = []
    for map in parsed_map:
        if map != '':
            conversion[category] += [[int(number) for number in map.split(' ')]]

location_number = float('inf')
for seed_number in seed_numbers:
    location_number =  min(location_number, mapping(conversion, seed_number))

print(location_number)

seed_ranges = [[seed_numbers[i], seed_numbers[i]+seed_numbers[i+1]] for i in range(0, len(seed_numbers), 2)]

# print(next_range(conversion['soil'], seed_ranges[0]))

# print(next_range(conversion['temperature'], [74,95]))
# print(next_range(conversion['light'], [81,95]))
# print(next_range(conversion['humidity'], [78,63]))

# print(mapping(conversion, 93))
# print(mapping(conversion, 95))

# print(next_category(conversion['humidity'], 63))
location_number = []
for seed_range in seed_ranges:
    location_number.append(min(item for sublist in mapping_range(conversion,seed_range) for item in sublist))

print(min(location_number))

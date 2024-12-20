import re
import numpy as np

with open('input.txt') as file:
    sensor_output = file.read().strip().split('\n')

positions_sensor = dict()
positions_beacon = dict()
sensors = []
beacons = set()
for sensor in sensor_output:
    position = re.findall('[-+]?\d+', sensor)
    positions_beacon[(int(position[2]), int(position[3]))] = (int(position[0]), int(position[1]))
    positions_sensor[(int(position[0]), int(position[1]))] = (int(position[2]), int(position[3]))
    sensors.append((int(position[0]), int(position[1])))
    beacons.add((int(position[2]), int(position[3])))


def manhattan_distance(cord_1, cord_2):
     return (abs(cord_1[0] - cord_2[0]) + abs(cord_1[1] - cord_2[1]))

def is_neigbour(sensor, coordinate):
    beacon = positions_sensor[sensor]
    distance_1 = manhattan_distance(sensor, beacon)
    distance_2 = manhattan_distance(sensor, coordinate)
    if distance_1 >= distance_2:
        return True
    else:
        return False

def outline(sensor, coordinate):
    beacon = positions_sensor[sensor]
    distance_1 = manhattan_distance(sensor, beacon)
    distance_2 = manhattan_distance(sensor, coordinate)
    if distance_1 == distance_2:
        return True
    else:
        return False

def end_sensor_row(sensor, y_coord, distance):
    return (distance - abs(sensor[1] - y_coord) + sensor[0])

def get_y_neigbour(sensor):
    return range(sensor[1] - radius_sensor[sensor], sensor[1] + radius_sensor[sensor])

def get_corners(sensor):
    return [(sensor[0] - radius_sensor[sensor], sensor[1]), (sensor[0] + radius_sensor[sensor], sensor[1]), (sensor[0], sensor[1] - radius_sensor[sensor]), (sensor[0], sensor[1] + radius_sensor[sensor])]

def get_y_intercept(sensor):
    A, X, Y, Z  =  get_corners(sensor)
    slope_1 = int(X[0] - Y[0])/(X[1] - Y[1])
    y_1 = int(Y[1] - (slope_1 * Y[0]))
    y_2 = int(Z[1] - (slope_1 * Z[0]))

    slope_2 = int(X[0] - Z[0])/(X[1] - Z[1])
    y_3 = int(Y[1] - (slope_2 * Y[0]))
    y_4 = int(Z[1] - (slope_2 * Z[0]))  
    return [[y_1, y_2, slope_1], [y_3, y_4, slope_2]]

def intersection_lines(m1, m2, c1, c2):
    x = int((c2 - c1)/(m1 - m2))
    y = int(m1*x + c1)
    return (y, x)



radius_sensor = dict()

for sensor in sensors:
    dist = manhattan_distance(sensor, positions_sensor[sensor])
    radius_sensor[sensor] = dist

row = 10
column = []
for sensor in sensors:
    y_intercepts = get_y_intercept(sensor)
    for i in range(2):
        for j in range(2):
            point_new = intersection_lines(y_intercepts[i][2], 0, y_intercepts[i][j], row)
            if is_neigbour(sensor, (point_new[1], point_new[0])):
                column.append(point_new[1])


impossible_beacon_left = min(column)
impossible_beacon_right = max(column)

sorted_sensors = [x for _, x in sorted(zip(radius_sensor.values(), sensors), reverse=True)]

x = impossible_beacon_left

impossible_positions = 0
while x < impossible_beacon_right:
    for sensor in sorted_sensors:
        if is_neigbour(sensor, (x, row)):
            new_x = end_sensor_row(sensor, row, radius_sensor[sensor])
            impossible_positions += new_x - x + 1
            x = new_x
            break
    x += 1
            
beacon_count = 0
for beacon in beacons:
    if beacon[1] == row:
        beacon_count += 1
    

print("Part 1:", impossible_positions -  beacon_count)

###############################################################


boards = []
for i in range(21):
    list_j = []
    for j in range(21):
        if (j, i) in sensors:
            # print("S", i, j)
            list_j.append('S')
        elif (j, i) in beacons:
            # print("B",i, j)
            list_j.append('B')
        else:
            sensor_number = 0

            for sensor in sensors:
                if outline(sensor, (j, i)):
                    # print("#", i,j)
                    list_j.append('#')
                    break
                elif is_neigbour(sensor, (j, i)):
                    list_j.append('*')
                    break
                else:
                    sensor_number += 1
            if sensor_number == len(sensors):
                # print(".",i, j)
                list_j.append('.')
            
            
    boards.append(list_j)

# for board in boards:
#     print(''.join(board))


def mid_point(l):
    l1, l2, l3, l4 = l[0], l[1], l[2], l[3]
    coords = [l1[0], l1[1], l2[0], l2[1]]
    if l3[0] in coords:
        return (l3[0], l4[1])

    else:
        return (l4[0], l3[1])


Y = [[], []]
for sensor in sensors:
    y_intercepts = get_y_intercept(sensor)
    for i in range(2):
        for j in range(2):
            Y[i].append([y_intercepts[i][j], y_intercepts[i][2], sensor])
            # looked.append([y_intercepts[i][j], y_intercepts[i][2]])




# print(Y)
# setY = [set(Y[0]), set(Y[1])]
lines = [[], []]
set_looked = []
for i in range(2):
    for j in range(len(Y[i])):
        for k in range(j+1, len(Y[i])):
            if Y[i][k][2] != Y[i][j][2]:
                if abs(Y[i][j][0] - Y[i][k][0]) ==  2 and (Y[i][j][1], Y[i][j][0], Y[i][k][0]) not in set_looked:
                    lines[i].append([Y[i][j][1], Y[i][j][0], Y[i][k][0], Y[i][k][2], Y[i][j][2]])
                    set_looked.append((Y[i][j][1], Y[i][j][0], Y[i][k][0]))
print(lines)



def beacon_point(lines, size):   
    for line_1 in lines[0]:
        for line_2 in lines[1]:
            intersections = []
            for i in range(1, 3):
                for j in range(1, 3):
                    intersections.append(intersection_lines(line_1[0], line_2[0], line_1[i], line_2[j]))
            # print(intersections)
            (x, y) = mid_point(intersections)
            if 0 <= x <= size and 0 <= y <= size:
                print(x, y)
                if len([line_1]) == len([line_2]) == 1:
                    # print("final")
                    return (x, y)
                sensor_count = 0
                for sensor in sensors:
                    if is_neigbour(sensor, (x, y)) == False:
                        sensor_count += 1

                # print(len(sensors), sensor_count)
                if sensor_count == len(sensors):
                    return (x, y)


# print(beacon_point(lines, 20))

(x, y) = beacon_point(lines, 4000000)
# print((x, y))


# l1, l2 = lines[0][0], lines[1][6]
# print(l1, l2)
# print(intersection_lines(l1[0], l2[0], l1[1], l2[1]))
# print(intersection_lines(l1[0], l2[0], l1[1], l2[2]))
# print(intersection_lines(l1[0], l2[0], l1[2], l2[1]))
# print(intersection_lines(l1[0], l2[0], l1[2], l2[2]))



print("Part 2:",  (y*4000000) + x)

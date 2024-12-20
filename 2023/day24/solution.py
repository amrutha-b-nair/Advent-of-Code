from itertools import combinations, permutations
import numpy as np

def find_cross_points(hailstones, test_area):
    hailstone_pairs = list(combinations(hailstones.items(), 2))
    count = 0
    for pair in hailstone_pairs:
        x, y, z = pair[0][0]
        vx, vy, vz = pair[0][1]
        x1,y1,z1 = pair[1][0] 
        vx1, vy1, vz1 = pair[1][1]
        if vx1*vy - vx*vy1 != 0:
            t1 = (vy*(x - x1) - vx*(y - y1))/(vx1*vy - vx*vy1)
            t = (x1 - x + vx1*t1)/vx
            dist_x = x1+ vx1*t1
            dist_y= y1+ vy1*t1
            if t1 >=0 and t >= 0:
                if test_area[0] <= dist_x <= test_area[1] and test_area[0] <= dist_y <= test_area[1]:
                    count += 1
    return count

def parse_input(hailstones):
    x = {}
    y = {}
    z = {}
    vx = {}
    vy = {}
    vz = {}
    for i, item in enumerate(hailstones.items()):
        x[i+1], y[i+1], z[i+1] = item[0]
        vx[i+1], vy[i+1], vz[i+1] = item[1]
    return x,y,z,vx,vy,vz


def all_possible(hailstones):
    pairs = list(permutations(range(1, len(hailstones)+1), 2))
    x,y,z,vx,vy,vz = parse_input(hailstones)
    possible = []
    for pair in pairs:
        t = pair[0]
        t1 = pair[1]
        dx = -(t*t1*vx[1] - (t1*vx[2] + x[2])*t + t1*x[1])/(t - t1)
        dy = -((t1*vy[1] - t1*vy[2] - y[2])*t + t1*y[1])/(t - t1) 
        dz = -((t1*vz[1] - t1*vz[2] - z[2])*t + t1*z[1])/(t - t1)
        dvy = (t*vy[1] - t1*vy[2] + y[1] - y[2])/(t - t1) 
        dvx = (t*vx[1] - t1*vx[2] + x[1] - x[2])/(t - t1)
        dvz = (t*vz[1] - t1*vz[2] + z[1] - z[2])/(t - t1)
        possible.append([t,t1,dx,dy,dz,dvx,dvy,dvz])

    return possible

# def exact_position(hailstones, i, visited):


def get_final(hailstones):
    x,y,z,vx,vy,vz = parse_input(hailstones)
    possible_positions = all_possible(hailstones)
    possible_sums = []
    i = 3
    wrong_position = []
    while i < len(hailstones):
        print(i)
        possible_positions = [pos for pos in possible_positions if pos not in wrong_position]
        print(len(possible_positions))
        print('#####')
        for position in possible_positions:
            t,t1,dx,dy,dz,dvx,dvy,dvz = position
            if (dvx - vx[i])!=0 and (-(dx - x[i])/(dvx - vx[i])).is_integer() and dy - y[i] +(dvy - vy[i])*(-(dx - x[i])/(dvx - vx[i])) == 0 and dz - z[i] +(dvz - vz[i])*(-(dx - x[i])/(dvx - vx[i])) == 0:
                    possible_sums.append(sum([dx,dy,dz]))
            else:
                wrong_position.append(position)
        if len(possible_sums) == 1:
            return int(possible_sums[0])
        i += 1
    return 0



with open('input.txt') as file:
    lines = file.read().strip().split('\n')

hailstones = {}

for line in lines:
    parsed_line = [input.split(', ') for input in line.split(' @ ')]
    hailstones[tuple(int(input) for input in parsed_line[0])] = tuple(int(input) for input in parsed_line[1])

test_case = [7,27]
input_case = [200000000000000, 400000000000000]

print(find_cross_points(hailstones, input_case))


print(get_final(hailstones))
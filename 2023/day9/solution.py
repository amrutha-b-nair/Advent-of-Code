import math

def nth_pascal(n):
    row = [((-1)**(k+n))*math.comb(n, k) for k in range(n + 1)]
    return row

with open('input.txt') as file:
    lines = file.read().strip().split('\n')

value_following = 0
value_previous = 0
for line in lines:
    history = [int(value) for value in line.split(' ')]
    pascal = nth_pascal(len(history))
    value_following += -sum(history[i]*pascal[i] for i in range(len(history)))
    value_previous += -pascal[0]*sum(history[i]*pascal[i + 1] for i in range(len(history)))

print('Part 1:',value_following)
print('Part 2:',value_previous)


from collections import defaultdict
from copy import deepcopy


with open('input.txt') as file:
    monkey_items_raw = file.read().strip().split('\n\n')


def substitution(eqn, list, x, number, test_number):

    eqn_list = eqn.split(' ')
    final = []
    for value in list:
        substituted_1 = int(eqn_list[0].replace(x, str(value))) 
        substituted_2 = int(eqn_list[2].replace(x, str(value)))
        if eqn_list[1] == '*':
            eqn_2 = substituted_1 * substituted_2
        elif eqn_list[1] == '+':
            eqn_2 = substituted_1 + substituted_2

        final.append((eqn_2// number) % test_number)
    return final


monkey_data = defaultdict(list)

operations = defaultdict(list)

test_product = 1

for monkey_list in monkey_items_raw:

    monkey_items = monkey_list.split('\n')
    
    monkey = int(monkey_items[0].split(' ')[1][:-1])
    starting_items = monkey_items[1].split(': ')[1].split(',')
    operation = monkey_items[2].split('= ')[1]
    monkey_data[monkey].append([int(item) for item in starting_items])
    test =  int(monkey_items[3].split(' ')[-1])
    test_product = test_product * test
    monkey_data[monkey].append(test)
    throw = {}
    for i in {4,5}:
        action = monkey_items[i].strip().split(' ')
        throw[action[1]] = int(action[-1])
        monkey_data[monkey].append(throw)
        
    monkey_data[monkey].append(0)

    monkey_data[monkey].append(operation)
    
monkey_data_new = deepcopy(monkey_data)

def throw_round(monkey_data, number):
    for monkey in monkey_data.keys():
        # items = monkey_data[monkey][0]
        to_remove = []
        items = substitution(monkey_data[monkey][-1], monkey_data[monkey][0], 'old', number, test_product)
        for worry_level in items:
            to_pop = items.index(worry_level)
            if worry_level % monkey_data[monkey][1] == 0:
                result = 'true:'
            else:
                result = 'false:'
            to_remove.append([monkey_data[monkey][2][result], to_pop])
            
        
        for value in to_remove:
            monkey_data[value[0]][0].append(items.pop(0))
            monkey_data[monkey][-2] += 1
        monkey_data[monkey][0] = []
    return monkey_data


for i in range(20):
    monkey_data = throw_round(monkey_data, 3)

monkey_business = []
for monkey in monkey_data:
    monkey_business.append(monkey_data[monkey][-2])

sorted_monkey_business = sorted(monkey_business, reverse = True)
print("Part 1:", sorted_monkey_business[0]*sorted_monkey_business[1])


for i in range(10000):
    monkey_data_new = throw_round(monkey_data_new, 1)

monkey_business_new = []
for monkey in monkey_data_new:
    monkey_business_new.append(monkey_data_new[monkey][-2])

sorted_monkey_business_new = sorted(monkey_business_new, reverse = True)
print("Part 2:", sorted_monkey_business_new[0]*sorted_monkey_business_new[1])


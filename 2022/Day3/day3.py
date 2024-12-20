with open('input.txt') as file:
    rucksacks = file.read().split('\n')


priority_score = 0

number_rucksacks = len(rucksacks)

def get_score(item):
    if item.islower():
        return ord(item)-96
    if item.isupper():
        return ord(item)-38


for i in range(0,len(rucksacks)):

    rucksack = list(rucksacks[i])
    length = len(rucksack)
    compartment_1 = set(rucksack[0 : int(length/2)])
    compartment_2 = set(rucksack[int(length/2) : int(length)])
    
    for item in compartment_1:
        if item in compartment_2:
            priority_score +=get_score(item)

print("Part 1:", priority_score)

def common_element_lists(L1, L2, L3):
    common_12 = set(L1).intersection(set(L2))
    common_123 = set(common_12).intersection(set(L3))
    return common_123.pop()


n=3
score = 0
for i in range(int(number_rucksacks/3)):
    badge = common_element_lists(list(rucksacks[n*i]), list(rucksacks[n*i + 1]), list(rucksacks[n*i + 2]))
    score += get_score(badge)

print("Part 2:", score)
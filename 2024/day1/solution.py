with open('input.txt') as file:
    lines = file.read().strip().split('\n')

################### Part 1 #####################

# left_list = []
# right_list = []

# for line in lines:
#     left, right = line.split("   ")
#     left_list.append(int(left))
#     right_list.append(int(right))

# left_list.sort()
# right_list.sort()

# total = 0

# for position, value in enumerate(left_list):
#     total += abs(value - right_list[position])

# print(total)

################### Part 2 #####################


left_dict = {}
right_dict = {}
similarity_score = 0

for line in lines:
    left, right = map(int, line.split("   "))
    if left in left_dict.keys():
        left_dict[left] += 1
    else: left_dict[left] = 1

    if right in right_dict.keys():
        right_dict[right] += 1
    else: right_dict[right] = 1

for key in left_dict.keys():
    if key in right_dict.keys():
        similarity_score += key*right_dict[key]*left_dict[key]
    
print(similarity_score)
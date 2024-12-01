
def workflow_eval(rating_dict, workflow = 'in'):
    # print('$$$$$$$$$$$$',workflow)
    for step in workflow_dict[workflow]:
        if len(step) == 1:
            if step[0] == 'A':
                return True
            elif step[0] == 'R':
                return False
            return workflow_eval(rating_dict, step[0])
        elif eval(step[0], {step[0][0]:rating_dict[step[0][0]]}):
            if step[1] == 'A':
                return True
            elif step[1] == 'R':
                return False
            return workflow_eval(rating_dict, step[1])


with open('input.txt') as file:
    workflow_raw, part_ratings_raw = file.read().strip().split('\n\n')

workflows = [line.strip().split('{') for line in workflow_raw.split('\n')]
part_ratings = part_ratings_raw.split('\n')

workflow_dict = {}

for workflow in workflows:
    workflow_dict[workflow[0]] = [step.split(':') for step in workflow[1][:-1].split(',')]

total_rating_value = 0
for ratings in part_ratings:
    rating_dict = {}
    part_rating = [rating.split('=') for rating in ratings[1:-1].split(',')]
    for category in part_rating:
        rating_dict[category[0]] = int(category[1])
    if workflow_eval(rating_dict):
        total_rating_value += sum(rating_dict.values())



print('Part 1:',total_rating_value)




possible_range = {'x': [1,4000], 'm':[1,4000], 'a':[1,4000], 's':[1,4000] }
ppssibilities = 0

def workflow_all_possibe(possible_range, workflow = 'in'):
    possible_range_temp = possible_range.copy()
    # print('workflow@@@@',workflow)
    # print(possible_range)
    accepted_values = 0
    if workflow == 'A':
        accepted = 1
        for values in possible_range.values():
            accepted *= (values[1] - values[0] + 1) 
        accepted_values += accepted
        # print('@@@@@@@@', accepted_values)
        return accepted_values
    elif workflow == 'R':
        return 0
    for step in workflow_dict[workflow]:
        if len(step) == 1:
            accepted_values += workflow_all_possibe(possible_range_temp, step[0])
        else:
            if step[0][1] == '<':
                possible_range_temp[step[0][0]] = [possible_range[step[0][0]][0],min(int(step[0][2:])-1,possible_range[step[0][0]][1])]
                less_than = True
            elif step[0][1] == '>':
                possible_range_temp[step[0][0]] = [max(possible_range[step[0][0]][0],int(step[0][2:])+1), possible_range[step[0][0]][1]]
                less_than = False
            accepted_values += workflow_all_possibe(possible_range_temp, step[1])
            print(step, possible_range_temp[step[0][0]])
            if less_than:
                possible_range_temp[step[0][0]] = [max(possible_range[step[0][0]][0], int(step[0][2:])), possible_range[step[0][0]][1]]
            else:
                possible_range_temp[step[0][0]] = [possible_range[step[0][0]][0],min(int(step[0][2:]),possible_range[step[0][0]][1])]
            print(step,possible_range_temp[step[0][0]])
    return accepted_values
    
# print('\n\n\n\n')


def workflow_all_possibe_two(possible_range, workflow = 'in'):
    possible_range_temp = possible_range.copy()
    print('workflow@@@@',workflow)
    print(possible_range)
    rejected_values = 0
    if workflow == 'A':
        return 0
    elif workflow == 'R':
        rejected = 1
        for values in possible_range.values():
            rejected *= (values[1] - values[0]) 
        rejected_values += rejected
        print('@@@@@@@@@@@', rejected_values)
        return rejected_values
    for step in workflow_dict[workflow]:
        if len(step) == 1:
            rejected_values += workflow_all_possibe_two(possible_range_temp, step[0])
        else:
            if step[0][1] == '<':
                possible_range_temp[step[0][0]] = [possible_range[step[0][0]][0],int(step[0][2:])]
                less_than = True
            elif step[0][1] == '>':
                possible_range_temp[step[0][0]] = [int(step[0][2:])+1, possible_range[step[0][0]][1]]
                less_than = False
            rejected_values += workflow_all_possibe_two(possible_range_temp, step[1])
            if less_than:
                possible_range_temp[step[0][0]] = [int(step[0][2:]), possible_range[step[0][0]][1]]
            else:
                possible_range_temp[step[0][0]] = [possible_range[step[0][0]][0],int(step[0][2:]) + 1]
                
    return rejected_values
    
print(workflow_all_possibe(possible_range))
# print('\n\n\n\n')
# print(4000**4 - workflow_all_possibe_two(possible_range))
# print(workflow_all_possibe_two(possible_range))
# print(4000**4)
# print(13479615000000 + 2987370272000 + 5938910016000 + 5282977218480 + 10843207776000 + 49890912000000)
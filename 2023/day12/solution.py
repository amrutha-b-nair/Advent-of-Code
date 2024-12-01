
def get_spring_count(string, list):
    if len(string) == 0:
        return 1
    if len(string) == 1:
        return 1
    if '?' not in string:
        return 1
    
    print(list[1:], sum(list[1:]) + len(list) - 1)
    print(string[:sum(list[1:]) + len(list) - 1])



with open('trial.txt') as file:
    lines = file.read().strip()

input_data = [line.split(' ') for line in lines.split('\n')] 

for input in input_data:
    get_spring_count(input[0], [int(value) for value in input[1].split(',')])
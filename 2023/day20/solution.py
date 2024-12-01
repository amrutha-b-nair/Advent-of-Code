def broadcaster(destinations):
    for destination in destinations:
        in_outs[destination][0] = 'Low'
        
    return 0


with open('trial.txt') as file:
    lines = file.read().strip().split('\n')

modules_outputs = {}
states = {}
flip_flops = []
conjuctions = []
in_outs = {}
for line in lines:
    parsed = line.split(' -> ')
    if parsed[0][0] == '%':
        flip_flops.append(parsed[0][1:])
        states[parsed[0][1:]] = False
        modules_outputs[parsed[0][1:]] = parsed[1].split(', ')
        # 1 is input 0 is output
        in_outs[parsed[0][1:]] = ['','']
    elif parsed[0][0] == '&':
        conjuctions.append(parsed[0][1:])
        states[parsed[0][1:]] = []
        modules_outputs[parsed[0][1:]] = parsed[1].split(', ')
        in_outs[parsed[0][1:]] = ['','']
    else:
        modules_outputs[parsed[0]] =parsed[1].split(', ')
        in_outs[parsed[0]] = ['','']
for conjuction in conjuctions:
    for key, values in modules_outputs.items():
        if conjuction in values:
            states[conjuction] = {key:'Low'}


in_outs['broadcaster'] = ['Low', 'Low']

initial_states = states.copy()

# print(states, conjuctions, flip_flops)
print(in_outs)

print(broadcaster(modules_outputs['broadcaster']))
print(in_outs)

print(states)

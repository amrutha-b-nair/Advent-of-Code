from collections import defaultdict

with open("input.txt") as file:
    initial, gates = file.read().strip().split("\n\n")

inputs = defaultdict(int, {val.split(": ")[0]: int(val.split(": ")[1]) for val in initial.split("\n")})
gates = [gate.split(" ") for gate in gates.split("\n")]

def perform(a, b, operation):
    if operation == "AND":
        return a & b
    elif operation == "XOR":
        return a ^ b
    elif operation == "OR":
        return a | b
    return 0

def mapOutput(output:defaultdict):
    outputKeys = [output[key] for key in sorted(output.keys(), reverse=True)]
    binary = ''.join(map(str, outputKeys))
    return binary



def getOutput(inputs: defaultdict, gates: list):
    outputs = defaultdict(int)
    while gates:
        gate = gates.pop(0)
        known = set(inputs.keys())
        if gate[0] in known and gate[2] in known:
            result = perform(inputs[gate[0]], inputs[gate[2]], gate[1])
            inputs[gate[4]] = result
            if gate[4][0] == "z":
                outputs[int(gate[4][1:])] = result
        else:
            gates.append(gate)
    
    return mapOutput(outputs)



print("Part 1: ",int(getOutput(inputs, gates), 2))
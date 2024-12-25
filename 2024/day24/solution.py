from collections import defaultdict



with open("input.txt") as file:
    initial, lines = file.read().strip().split("\n\n")

inputs = defaultdict(int, {val.split(": ")[0]: int(val.split(": ")[1]) for val in initial.split("\n")})
gatesList = [gate.split(" ") for gate in lines.split("\n")]



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
    localInputs = inputs.copy()
    outputs = defaultdict(int)
    while gates:
        gate = gates.pop(0)
        known = set(localInputs.keys())
        if gate[0] in known and gate[2] in known:
            result = perform(localInputs[gate[0]], localInputs[gate[2]], gate[1])
            localInputs[gate[4]] = result
            if gate[4][0] == "z":
                outputs[int(gate[4][1:])] = result
        else:
            gates.append(gate)
    
    return mapOutput(outputs)

xWires = sorted([key for key in inputs if key.startswith("x")], reverse=True)
yWires = sorted([key for key in inputs if key.startswith("y")], reverse=True)

xBinary = ''.join(str(inputs[wire]) for wire in xWires)
yBinary = ''.join(str(inputs[wire]) for wire in yWires)
expectedSum = bin(int(xBinary, 2) + int(yBinary, 2))[2:].strip()
zWires = [f"z{i:02}" for i in range(len(expectedSum)-1, -1, -1)]

print("Part 1: ",int(getOutput(inputs.copy(), gatesList.copy()), 2))

def sort(x,y):
    if x < y: return (x, y)
    else: return (y, x)


gates = {}
gatesInv = {}
for gate in lines.split("\n"):
    gate = gate.split(" ")
    a, b = sort(gate[0], gate[2])
    gates[(a, b, gate[1])] = gate[4]
    gatesInv[gate[4]] = (a, b, gate[1])


def swap(a, b):
    gatesInv[a], gatesInv[b] = gatesInv[b], gatesInv[a]
    gates[gatesInv[a]], gates[gatesInv[b]] = gates[gatesInv[b]], gates[gatesInv[a]]


output = set()
carry = ''
for i in range(int(max(gatesInv)[1:])):
    x = f'x{i:02}'
    y = f'y{i:02}'
    z = f'z{i:02}'
    xor = gates[x, y, "XOR"]
    And = gates[x, y, "AND"]
    if not carry:
        carry = And
    else:
        a, b = sort(carry, xor)
        k = a, b, "XOR"
        if k not in gates:
            a, b = list(set(gatesInv[z][:2]) ^ set(k[:2]))
            output.add(a)
            output.add(b)
            swap(a, b)
        elif gates[k] != z:
            output.add(gates[k])
            output.add(z)
            swap(z, gates[k])
        k = gatesInv[z]
        xor = gates[x, y, "XOR"]
        And = gates[x, y, "AND"]

        carrySort, xorSort = sort(carry, xor)
        carry = gates[carrySort, xorSort, "AND"]

        carrySort, AndSort = sort(carry, And)
        carry = gates[carrySort, AndSort, "OR"]

        
print("Part 2:",','.join(sorted(output)))
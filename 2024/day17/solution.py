from z3 import *
with open('input.txt') as file:
    rawReg, rawProg  = file.read().strip().split("\n\n")

regs = {value[9:10] : int(value[12:]) for value in rawReg.split("\n")}
program = [int(value) for value in rawProg[9:].split(",")]

print(program)
print(regs)
combo = lambda key: (
    0 if key == 0 else
    1 if key == 1 else
    2 if key == 2 else
    3 if key == 3 else
    regs["A"] if key == 4 else
    regs["B"] if key == 5 else
    regs["C"] if key == 6 else
    None
)
jumps = False
pointer = 0

def perform(opcode, operand):
    if opcode == 0:
        regs["A"] = regs["A"]//(2**combo(operand))
    elif opcode == 1:
        regs["B"] = regs["B"]^operand
    elif opcode == 2:
        regs["B"] = combo(operand) % 8
    elif opcode == 3:
        if regs["A"] != 0:
            global jumps, pointer
            jumps = True
            pointer = operand
    elif opcode == 4:
        regs["B"] = regs["B"]^regs["C"]
    elif opcode == 5:
        return [combo(operand) % 8]
    elif opcode == 6:
        regs["B"] = regs["A"]//(2**combo(operand))
    elif opcode == 7:
        regs["C"] = regs["A"]//(2**combo(operand))



final = []
while(pointer < len(program)):
    if jumps:
        jump = 1
    if pointer+1 < len(program):
        currPointer = pointer
        pointer += 2
        result = perform(program[currPointer], program[currPointer+1])
        print(format(regs["A"], '032b'))
        if result != None:
            final += result
    

print("Part 1:", ",".join(map(str, final)))



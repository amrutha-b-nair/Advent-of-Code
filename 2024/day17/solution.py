from z3 import *
with open('input.txt') as file:
    rawReg, rawProg  = file.read().strip().split("\n\n")

combo = lambda key, regs: (
    key if 0 <= key <= 3 else
    regs["A"] if key == 4 else
    regs["B"] if key == 5 else
    regs["C"] if key == 6 else
    None
)

def run(program,regs):
    final = []
    pointer = 0
    while pointer < len(program):
        if pointer+1 < len(program):
            opcode, operand = program[pointer], program[pointer+1]
            comboOper = combo(operand, regs)
            if opcode == 0:
                regs["A"] = regs["A"]//(2**comboOper)
            elif opcode == 1:
                regs["B"] = regs["B"]^operand
            elif opcode == 2:
                regs["B"] = comboOper % 8
            elif opcode == 3:
                if regs["A"] != 0:
                    pointer = operand
                    continue
            elif opcode == 4:
                regs["B"] = regs["B"]^regs["C"]
            elif opcode == 5:
                final += [comboOper % 8]
            elif opcode == 6:
                regs["B"] = regs["A"]//(2**comboOper)
            elif opcode == 7:
                regs["C"] = regs["A"]//(2**comboOper)
        pointer += 2
    return final 


def getA(program):
    regs = {"A": 0, "B": 0, "C": 0}
    j = 1
    start = 0
    loop = 0
    while j <= len(program) and j >= 0:
        regs["A"] *= 8
        for i in range(start, 8):
            interRegs = {"A": regs["A"] + i, "B": regs["B"], "C": regs["C"]}
            if program[-j:] == run(program, interRegs):
                loop = i
                break
        else:
            #go back to find a different i for the previous reg value 
            j -= 1
            regs["A"] //= 64
            start = loop + 1
            continue
        
        j += 1
        regs["A"] += i
        start = 0
    return regs["A"]

regs = {value[9:10] : int(value[12:]) for value in rawReg.split("\n")}
program = [int(value) for value in rawProg[9:].split(",")]

print("Part 1:", ",".join(map(str, run(program, regs))))

print("Part 2:", getA(program))


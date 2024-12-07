import re

with open('input.txt') as file:
    instruction = file.read().strip()



pattern = r"mul\(\d{1,3},\d{1,3}\)"

def findProduct(instruction):
    matches = re.findall(pattern, instruction)

    total = 0
    for match in matches:
        values = [int(val) for val in match[4:-1].split(",")]
        total += values[0]*values[1]

    return total

print(findProduct(instruction))


donts = instruction.split("don't")
newInstruction = donts[0]

for part in donts[1:]:
    dos = part.split("do")
    if len(dos) > 1:
        newInstruction += "".join(dos[1:])

print(findProduct(newInstruction))


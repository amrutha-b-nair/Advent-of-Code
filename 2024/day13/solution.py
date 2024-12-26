with open("input.txt") as file:
    inputs = [input.split("\n") for input in file.read().strip().split("\n\n")]

def solve(mat, val):
    xA, xB = mat[0]
    yA, yB = mat[1]
    pA, pB = val
    det = xA*yB - yA*xB
    if det != 0:
        nA = yB*pA - xB*pB
        nB = -yA*pA + xA*pB
        if nA % det == 0 and nB % det == 0:
            return (nA//det)*3 + nB//det
        return 0
    else:
        print(det)
        return 0
        

tokens = 0
tokens2 = 0
for input in inputs:
    infoA = input[0].split(" ")
    xA = int(infoA[2][2:-1])
    yA = int(infoA[3][2:])
    infoB = input[1].split(" ")
    xB = int(infoB[2][2:-1])
    yB = int(infoB[3][2:])
    infoPrize = input[2].split(" ")
    xPrize = int(infoPrize[1][2:-1])
    yPrize = int(infoPrize[2][2:])
    xPrize2 = 10000000000000 + int(infoPrize[1][2:-1])
    yPrize2 = 10000000000000 + int(infoPrize[2][2:])

    mat = [[xA, xB],
                  [yA, yB]]
  

    prize = [xPrize, yPrize]
    prize2 = [xPrize2, yPrize2]
    tokens += solve(mat, prize)
    tokens2 += solve(mat, prize2)


print("Part 1: ", tokens) 
print("Part 2: ", tokens2) 
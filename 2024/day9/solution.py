import time
from itertools import accumulate

start_time = time.time()

with open('input.txt') as file:
    line = file.read().strip()



lastID = int((len(line)-1)/2)

checksum = 0
position = 0
freeSpaces = []

usingBlock = []
i=0

while(len(line[i:]) > 0):
    if i%2 == 0:
        id = str(int(i/2))
        for j in range(int(line[i])):
            checksum += int(i/2)*(position)
            position += 1

    else:
        for j in range(int(line[i])):
            if len(usingBlock) < 1:
                x = int(line[-1])
                freeSpaces.append(int(line[-2]))
                line = line[:-2]
                usingBlock = [int(str(lastID))] * x
                lastID -= 1
            
            y = usingBlock.pop(-1)
            checksum += int(y)*position
            position += 1
    
    i += 1
            

for i in range(len(usingBlock)):
    checksum += int(usingBlock[i])*position
    position += 1

print(checksum)

print("--- %s seconds ---" % (time.time() - start_time))

######################### Part 2 #####################################

with open('input.txt') as file:
    line = file.read().strip()

lastID = int((len(line)-1)/2)

checksum = 0
freeSpaces = [int(x) for i, x in enumerate(line) if i%2==1]

finalPositions = list(accumulate([int(d) for d in str(line)], lambda x, y: x + y))

goToNext = True

while(lastID > 0):
    goToNext = False
    fileBlock = line[-1]
    line = line[:-2]
    for pos, space in enumerate(freeSpaces[:lastID + 1]):
        if int(fileBlock) <= space:
            for k in range(int(fileBlock)):
                checksum += int(lastID)*(finalPositions[pos*2 + 1]-int(space)+k) 
            lastID -= 1
            goToNext = True
            freeSpaces[pos] = space - int(fileBlock)
            break
    if goToNext:
        continue
    
    for l in range(int(fileBlock)):
        checksum += int(lastID)*(finalPositions[lastID*2]-int(fileBlock)+l)
    lastID -= 1

   

print(checksum)

print("--- %s seconds ---" % (time.time() - start_time))





    
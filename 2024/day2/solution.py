with open('input.txt') as file:
    lines = file.read().strip().split('\n')

################### Part 1 #####################


# notSafe = 0

# for line in lines:
#     report = [int(data) for data in line.split(" ")]
#     print([report[i+1] - report[i] for i in range(len(report)-1)])

#     ## increasing : sign = 1, else -1
#     if 1<= abs(report[1] - report[0]) <= 3:
#         sign = (report[1] - report[0]) / abs(report[0]-report[1])
        
#         for x, y in zip(report, report[1:]):
#             if (y - x) in [sign*1, sign*2, sign*3]:
#                 continue
#             else:
#                 notSafe += 1
#                 break
#     else:
#         notSafe += 1


# print(len(lines) - notSafe)

################### Part 2 #####################
safe = 0

getSign = lambda x: 1 if x > 0 else -1 if x < 0 else 0

great = 0

for line in lines:
    report = [int(data) for data in line.split(" ")]
    
    diff = {report[i+1] - report[i]: getSign(report[i+1] - report[i]) for i in range(len(report)-1)}
    if set(diff.keys()) <= {diff[next(iter(diff))]*1, diff[next(iter(diff))]*2, diff[next(iter(diff))]*3}:
        great += 1
        continue
    



print(safe, great)




    
    

with open('input.txt') as file:
    lines = file.read().strip().split('\n')

def isValidEqualtion(testValue, numbers, includeConcat = False, index=0, accumulated=None, operations=[]):
    if accumulated is None:
        accumulated = numbers[0]

    if accumulated > testValue:
        return False
    
    if index == len(numbers) -1:
        if accumulated == testValue:
            return True
        else:
            return False
        
    if isValidEqualtion(
        testValue, 
        numbers,
        includeConcat,
        index + 1,
        accumulated + numbers[index + 1],
        operations + ["+"]
    ):return True
    
    if isValidEqualtion(
        testValue, 
        numbers,
        includeConcat,
        index + 1,
        accumulated * numbers[index + 1],
        operations + ["*"]
    ):return True

    if includeConcat:
        if isValidEqualtion(
            testValue,
            numbers,
            includeConcat,
            index + 1,
            int(f"{accumulated}{numbers[index + 1]}"),
            operations + ["||"]
        ): return True
    
    return False


caliberationResult = 0
calibWithConcat = 0

for line in lines:
    testValue, rawNumbers = line.strip().split(":")
    testValue = int(testValue)
    numbers = [int(number) for number in rawNumbers.strip().split(" ")]    
    if isValidEqualtion(testValue, numbers):
        caliberationResult += testValue
    
    if isValidEqualtion(testValue, numbers, True):
        calibWithConcat += testValue



print(caliberationResult)
print(calibWithConcat)
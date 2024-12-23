from collections import defaultdict
from functools import cache
with open('input.txt') as file:
    stones = file.read().strip().split(" ")


def blink(val, blinkCount, memo):
    
    if (val, blinkCount) in memo:
        return memo[(val, blinkCount)]
    
    if blinkCount == 0:
        return 1
    
    if val == 0:
        result = blink(1, blinkCount - 1, memo)
    elif len(str(val)) % 2 == 0:
        val_str = str(val)
        mid = len(val_str) // 2
        result = blink(int(val_str[:mid]), blinkCount - 1, memo) + blink(int(val_str[mid:]), blinkCount - 1, memo)
    else:
        result = blink(val * 2024, blinkCount - 1, memo)
    
    memo[(val, blinkCount)] = result
    return result

def blinks(count, stones):
    stones = list(map(int, stones))
    memo = {}
    total_count = 0
    for stone in stones:
        total_count += blink(stone, count, memo)
    
    return total_count

print("Part 1:", blinks(25, stones))
print("Part 2:", blinks(75, stones))
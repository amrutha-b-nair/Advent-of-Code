from collections import defaultdict

with open('input.txt') as file:
    secrets  = [int(secret) for secret in file.read().strip().split("\n")]

def nextSecret(secret, priceChanges: defaultdict):
    prices = [secret % 10] 
    changes = []
    visited = set()
    for i in range(2000):
        secret = ((secret * 64) ^ secret) % 16777216
        secret = ((secret // 32) ^ secret) % 16777216
        secret = ((secret * 2048) ^ secret) % 16777216
        
        price = secret % 10
        prices.append(price)
        changes.append(prices[i+1] - prices[i])
        if i >= 3:
            fourChanges = tuple(changes[i-3:])
            if fourChanges not in visited:
                priceChanges[fourChanges].append(prices[i+1])
                visited.add(fourChanges)
    return secret, priceChanges

def solve(secrets):
    result = 0
    priceChanges = defaultdict(list)
    for secret in secrets:
        val, priceChanges = nextSecret(secret, priceChanges)
        result += val
    return result, priceChanges

result, priceChanges = solve(secrets)
print("Part 1:",result)

highestPrice = sum(max(priceChanges.values(), key=lambda x: sum(x)))

print("Part 2:",highestPrice)













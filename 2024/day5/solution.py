with open('input.txt') as file:
    rawRules, rawUpdates = (section.split('\n') for section in file.read().strip().split('\n\n'))

rules = {}

for rule in rawRules:
    before, after = rule.split('|')
    rules.setdefault(before, [[], []])[1].append(after)
    rules.setdefault(after, [[], []])[0].append(before)


from collections import defaultdict, deque

def createGraphToOrder(listToOrder, rules):

    graph = defaultdict(list)
    incomingEdgeCounts = defaultdict(int)

    for element in listToOrder:
        incomingEdgeCounts[element] = 0
        

    for element in listToOrder:
        constraints = rules[element]
        for before in constraints[0]:
            if before in listToOrder and before not in graph[element]:
                graph[before].append(element)  # before -> element
                incomingEdgeCounts[element] += 1

        for after in constraints[1]:
            if after in listToOrder and element not in graph[after]:
                graph[element].append(after)  # element -> after
                incomingEdgeCounts[after] += 1
    return graph, incomingEdgeCounts

def topologicalSort(listToOrder):
    graph, incomingEdgeCounts = createGraphToOrder(listToOrder, rules)
    queue = deque([node for node in listToOrder if incomingEdgeCounts[node] == 0])
    sortedList = []

    while queue:
        current = queue.popleft()
        sortedList.append(current)
        for neighbor in graph[current]:
            incomingEdgeCounts[neighbor] -= 1
            if incomingEdgeCounts[neighbor] == 0:
                queue.append(neighbor)

    return sortedList


def getMiddleUpdate(update):
    return int(update[int((len(update)-1)/2)])


sumPart1 = 0
sumPart2 = 0

for rawUpdate in rawUpdates:
    update = rawUpdate.split(",")
    rightOrder = True
    for pos, number in enumerate(update):
        if number in rules.keys():
            if not (set(update[:pos]) <= set(rules[number][0]) and set(update[pos+1:]) <= set(rules[number][1])):
                rightOrder = False
                sumPart2 += getMiddleUpdate(topologicalSort(update))
                break
    if rightOrder == True:
        sumPart1 += getMiddleUpdate(update)




print(sumPart1, sumPart2)
    

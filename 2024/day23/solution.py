from collections import defaultdict

with open("input.txt") as file:
    lines = file.read().strip().split("\n")
    


graph = defaultdict(set)
for line in lines:
    a, b = line.split("-")
    graph[a].add(b)
    graph[b].add(a)

triples = set()
nodes = list(graph.keys())

def tripleCount():
    for node in nodes:
        connections = graph[node]
        for connection in connections:
            commons = connections.intersection(graph[connection])
            for common in commons:
                triple = tuple(sorted([node, connection, common]))
                triples.add(triple)

    withChief = [triple for triple in triples if any(comp.startswith('t') for comp in triple)]
    return len(withChief)

def bronKerbosch(r, p, x, cliques):
    if not p and not x:
        cliques.append(r)
        return
    for node in list(p):
        bronKerbosch(
            r | {node},
            p & graph[node],
            x & graph[node],
            cliques
        )
        p.remove(node)
        x.add(node)

print("Part 1:", tripleCount())

cliques = []
bronKerbosch(set(), set(graph.keys()), set(), cliques)

largest = max(cliques, key=len)

password = ",".join(sorted(largest))
print("Part 2:", password)




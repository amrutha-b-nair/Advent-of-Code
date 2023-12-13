import numpy as np

def load_note(n):
    n = np.array([
        [*s]
        for s in n.split("\n")
    ]) == "#"
    return n.astype(np.int8)

def find_bisector(n, r=0, smudges=0):
    h, __ = n.shape

    if r > 3:
        return 0
    
    for i in range(1, h//2+1):
        d = n[:i][::-1] - n[i:i*2]
        
        if np.abs(d).sum() == smudges:
            match r:
                case 0:
                    return i * 100
                case 1:
                    return h - i
                case 2:
                    return (h - i) * 100
                case 3:
                    return i
                
    return find_bisector(
        np.rot90(n),
        r=r+1,
        smudges=smudges,
    )

with open("input.txt") as src:
    notes = [
        load_note(n)
        for n in src.read().strip().split("\n\n")
    ][51:53]

print("part one answer:", sum(map(find_bisector, notes)))
print("part two answer:", sum((
    find_bisector(n, smudges=1)
    for n in notes
)))

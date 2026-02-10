import sys
from collections import Counter

with open(sys.argv[1]) as f:
    rows = f.read().strip().split("\n")

splits = 0
beams = Counter([len(rows[0])//2])
for row in rows:
    new_beams = Counter()
    for b in beams.keys():
        if row[b] == "^":
            splits += 1
            new_beams[b - 1] += beams[b]
            new_beams[b + 1] += beams[b]
        else:
            new_beams[b] += beams[b]
    beams = new_beams
print("Part One:", splits)
print("Part Two:", beams.total())

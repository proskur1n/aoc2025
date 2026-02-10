import sys
import itertools
import math

class DisjointSet:
    def __init__(self, elements):
        self.parent = {e: e for e in elements}
        self.size = {e: 1 for e in elements}

    def root(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]
        else:
            return x

    def merge(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            self.parent[x] = y
            self.size[y] += self.size[x]
        else:
            self.parent[y] = x
            self.size[x] += self.size[y]

    def disjoint(self, x, y):
        return self.root(x) != self.root(y)

with open(sys.argv[1]) as f:
    boxes = [tuple(map(int, line.split(","))) for line in f.read().strip().split("\n")]

distances = sorted([math.dist(b1, b2), b1, b2] for b1, b2 in itertools.combinations(boxes, 2))

ds = DisjointSet(boxes)
for [_, b1, b2] in distances[:1000]:
    if ds.disjoint(b1, b2):
        ds.merge(b1, b2)
circuits = []
for box, parent in ds.parent.items():
    if parent == box:
        circuits.append(ds.size[box])
circuits.sort()
print("Part One:", math.prod(circuits[-3:]))

for [_, b1, b2] in distances[1000:]:
    if ds.disjoint(b1, b2):
        ds.merge(b1, b2)
        if ds.size[ds.root(b1)] == len(boxes):
            print("Part Two:", b1[0] * b2[0])
            break

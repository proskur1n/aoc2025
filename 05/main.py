import sys
from itertools import chain

with open(sys.argv[1]) as f:
    [ranges, ingredients] = f.read().split("\n\n")
    ranges = [list(map(int, r.split("-"))) for r in ranges.split()]
    ingredients = list(map(int, ingredients.split()))

print("Part One:", sum(1 for ing in ingredients if any(map(lambda r: r[0] <= ing <= r[1], ranges))))

part_two = 0
open_ranges = 0
range_begin = 0
for [num, desc] in sorted(chain.from_iterable([(r[0], "begin"), (r[1], "end")] for r in ranges)):
    if desc == "begin":
        if open_ranges == 0:
            range_begin = num
        open_ranges += 1
    else:
        open_ranges -= 1
        if open_ranges == 0:
            part_two += num - range_begin + 1
print("Part Two:", part_two)

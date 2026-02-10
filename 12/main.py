import re

with open("input.txt") as file:
    text_blocks = file.read().strip().split("\n\n")

present_sizes = [present.count("#") for present in text_blocks[:-1]]

regions = []
for line in text_blocks[-1].split("\n"):
    width, length, *presents = map(int, re.findall("\d+", line))
    regions.append((width*length, presents))

# This is a troll problem. This trivial approach doesn't work for the sample input :/
fitting = 0
for area, presents in regions:
    if sum(present_sizes[present]*count for present, count in enumerate(presents)) <= area:
        fitting += 1
print(fitting)

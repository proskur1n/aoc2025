import sys
import math
import itertools

def transpose(matrix):
    return list(zip(*matrix))

def solve(problems):
    grand_total = 0
    for numbers, op in zip(problems, operators):
        if op == "+":
            grand_total += sum(map(int, numbers))
        else:
            grand_total += math.prod(map(int, numbers))
    return grand_total

with open(sys.argv[1]) as f:
    *lines, operators = f.read().strip().split("\n")
    operators = operators.split()

print("Part One:", solve(transpose(line.split() for line in lines)))

problems = [[]]
for line in transpose(lines):
    number = "".join(line).strip()
    if number == "":
        problems.append([])
    else:
        problems[-1].append(number)
print("Part Two:", solve(problems))

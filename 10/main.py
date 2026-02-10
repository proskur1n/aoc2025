import sys
import pulp

next_var = 0
def new_var(**kwargs):
    global next_var
    v = pulp.LpVariable(f"var{next_var}" , **kwargs)
    next_var += 1
    return v

with open(sys.argv[1]) as file:
    lines = file.read().strip().split("\n")

part1, part2 = 0, 0
for line in lines:
    parts = line.split()
    wirings = [eval(wiring.replace("(", "[").replace(")", "]")) for wiring in parts[1:-1]]

    prob = pulp.LpProblem("aoc2025/10/part1", pulp.LpMinimize)
    vars = [new_var(cat="Binary") for _ in wirings]
    for i, indicator in enumerate(parts[0][1:-1]):
        if indicator == ".":
            prob += sum(vars[j] for j, wiring in enumerate(wirings) if i in wiring) == 2 * new_var(cat="Integer")
        else:
            prob += sum(vars[j] for j, wiring in enumerate(wirings) if i in wiring) == 2 * new_var(cat="Integer") + 1
    prob += sum(vars)
    prob.solve()
    part1 += sum(int(var.value()) for var in vars)

    prob = pulp.LpProblem("aoc2025/10/part2", pulp.LpMinimize)
    vars = [new_var(cat="Integer", lowBound=0) for _ in wirings]
    for i, joltage in enumerate(parts[-1][1:-1].split(",")):
        joltage = int(joltage)
        prob += sum(vars[j] for j, wiring in enumerate(wirings) if i in wiring) == joltage
    prob += sum(vars)
    prob.solve()
    part2 += sum(int(var.value()) for var in vars)
print(part1, part2)

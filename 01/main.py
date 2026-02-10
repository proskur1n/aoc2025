from sys import argv

with open(argv[1]) as f:
    rots = f.read().split()

pwd = 0
dial = 50
for rot in rots:
    if rot[0] == "R":
        dial += int(rot[1:])
    else:
        dial -= int(rot[1:])
    if dial % 100 == 0:
        pwd += 1
print("Part One:", pwd)

pwd = 0
dial = 50
for rot in rots:
    n = int(rot[1:])
    pwd += n // 100
    n %= 100
    if rot[0] == "L":
        n = -n
    dial += n
    if (dial - n) != 0 and (dial == 0 or dial % 100 != dial):
        pwd += 1
    dial %= 100
print("Part Two:", pwd)

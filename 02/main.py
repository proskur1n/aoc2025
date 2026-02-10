import sys
import itertools

with open(sys.argv[1]) as f:
    ranges = f.read().split(",")

def part1():
    result = 0
    for r in ranges:
        [begin, end] = map(int, r.split("-"))
        if len(str(begin)) % 2 != 0:
            begin = 10**len(str(begin))
        for n in itertools.count(start=int(str(begin)[:len(str(begin))//2])):
            id = int(str(n) + str(n))
            if id > end:
                break
            if id >= begin:
                result += id
    return result

def part2():
    invalid = set()
    for r in ranges:
        [begin, end] = map(int, r.split("-"))
        for n in itertools.count(start=1):
            if int(str(n) + str(n)) > end:
                break
            for repeats in itertools.count(start=2):
                id = int(str(n)*repeats)
                if id > end:
                    break
                if id >= begin:
                    invalid.add(id)
    return sum(invalid)

print("Part One:", part1())
print("Part Two:", part2())

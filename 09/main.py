import sys
import itertools

with open(sys.argv[1]) as f:
    reds = [tuple(map(int, line.split(","))) for line in f.read().split()]

def area(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

print("Part One:", max(area(p1, p2) for p1, p2 in itertools.combinations(reds, 2)))

def is_inside_polygon(p):
    x, y = p
    parity = 0
    for i, (x1, y1) in enumerate(reds):
        x2, y2 = reds[(i + 1) % len(reds)]
        if x1 == x2:
            # vertical edge
            if min(y1, y2) <= y < max(y1, y2):
                if x == x1:
                    return True
                if x < x1:
                    parity += 1
        else:
            # horizontal edge
            if y1 == y and min(x1, x2) <= x <= max(x1, x2):
                return True
    return parity % 2 == 1

def is_red_green(p1, p2):
    x1, x2 = sorted([p1[0], p2[0]])
    y1, y2 = sorted([p1[1], p2[1]])
    for i, (ex1, ey1) in enumerate(reds):
        ex2, ey2 = reds[(i + 1) % len(reds)]
        if min(ex1, ex2) < x2 and x1 < max(ex1, ex2) and min(ey1, ey2) < y2 and y1 < max(ey1, ey2):
            return False
    # NOTE: This particular input works even without this check. However, it is required for the
    # general solution to be correct.
    return is_inside_polygon((x1, y2)) and is_inside_polygon((x2, y1))

print("Part Two:", max(area(p1, p2) for p1, p2 in itertools.combinations(reds, 2) if is_red_green(p1, p2)))

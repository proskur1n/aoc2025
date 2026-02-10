import sys

def accessible(grid: dict[tuple[int, int], str]) -> set[tuple[int, int]]:
    result = set()
    for (x, y), cell in grid.items():
        if cell == "@" and sum(1 for dy in range(-1, 2) for dx in range(-1, 2) if grid.get((x+dx, y+dy), ".") == "@") < 5:
            result.add((x, y))
    return result

with open(sys.argv[1]) as f:
    grid = {(x, y): cell for y, line in enumerate(f.read().split()) for x, cell in enumerate(line)}
    print("Part One:", len(accessible(grid)))
    total_rolls = 0
    while True:
        rolls = accessible(grid)
        if len(rolls) == 0:
            break
        total_rolls += len(rolls)
        grid = {pos: cell for pos, cell in grid.items() if pos not in rolls}
    print("Part Two:", total_rolls)

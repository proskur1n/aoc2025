import sys

def max_joltage(bank: str, batteries: int) -> int:
    joltage = ""
    for k in range(batteries):
        i = bank.index(max(bank[:len(bank)-(batteries-1-k)]))
        joltage += bank[i]
        bank = bank[i+1:]
    return int(joltage)

with open(sys.argv[1]) as f:
    banks = f.read().split()
    print("Part One:", sum(max_joltage(bank, batteries=2) for bank in banks))
    print("Part Two:", sum(max_joltage(bank, batteries=12) for bank in banks))

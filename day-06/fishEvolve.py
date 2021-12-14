from collections import defaultdict
# Part 2 had me tripping. Thanks again mebeim! https://github.com/mebeim/aoc/
from typing import DefaultDict

def evolve(fish, days):
    for _ in range(days):
        newfish = DefaultDict(int)

        for t, n in fish.items():
            t -= 1

            if t < 0:
                newfish[6] += n
                newfish[8] += n
            else:
                newfish[t] += n
        
        fish = newfish

    return fish, sum(fish.values())

def main():
    with open("input.txt") as file:
        timers = map(int,[fish for fish in file.read().split(",")])
    fish = defaultdict(int)

    for t in timers:
        fish[t] += 1

    fish, n1 = evolve(fish, 80)
    _   , n2 = evolve(fish, 256 - 80)

    print('Part 1:', n1)
    print('Part 2:', n2)

if __name__ == "__main__":
    main()

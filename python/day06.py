from collections import deque


def calc_fishes(days, initial_fishes):
    table = deque(initial_fishes.count(k) for k in range(0, 9))
    for _ in range(0, days):
        table.rotate(-1)
        table[6] += table[8]
    return sum(table)


initial_fishes = [int(x) for x in open("assets/day06.txt").read().split(",")]
print(f"Part A: {calc_fishes(80, initial_fishes)}")
print(f"Part B: {calc_fishes(256, initial_fishes)}")

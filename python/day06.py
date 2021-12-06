from functools import lru_cache


@lru_cache(maxsize=None)
def reproduce(state, num_days):
    num_fish = 1
    for day in range(num_days - state, 0, -7):
        num_fish += reproduce(state=8, num_days=day - 1)
    return num_fish


def calc_fishes(days, initial_fishes):
    return sum(reproduce(f, days) for f in initial_fishes)


initial_fishes = [int(x) for x in open("assets/day06.txt").read().split(",")]

import sys

# print(sys.getrecursionlimit())
sys.setrecursionlimit(100000)
# print(f"Part A: {calc_fishes(80, initial_fishes)}")
print(f"Part B: {calc_fishes(50000, initial_fishes)}")

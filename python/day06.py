from functools import lru_cache


@lru_cache(maxsize=None)
def reproduce(state, num_days, num_fish=1):
    while num_days > 0:
        num_days -= 1
        if state == 0:
            num_fish += reproduce(state=8, num_days=num_days)
            state = 6
        else:
            state -= 1
    return num_fish


def calc_fishes(days, initial_fishes):
    return sum(reproduce(f, days) for f in initial_fishes)


initial_fishes = (int(x) for x in open("assets/day06.txt").read().split(","))

print(f"Part A: {calc_fishes(80, initial_fishes)}")
print(f"Part B: {calc_fishes(256, initial_fishes)}")

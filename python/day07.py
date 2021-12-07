from functools import lru_cache


@lru_cache(maxsize=None)
def eq(n):
    return (n ** 2 + n) >> 1


crabs = [int(x) for x in open("assets/day07.txt").read().split(",")]

parta = min(sum(abs(c - p) for c in crabs) for p in range(min(crabs), max(crabs)))
partb = min(sum(eq(abs(c - p)) for c in crabs) for p in range(min(crabs), max(crabs)))
print(parta)
print(partb)

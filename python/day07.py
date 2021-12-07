from functools import lru_cache


@lru_cache(maxsize=None)
def eq(n):
    return (n * (n + 1)) / 2


crabs = [int(x) for x in open("assets/day07-sample.txt").read().split(",")]

parta = min(sum(abs(c - p) for c in crabs) for p in range(min(crabs), max(crabs)))
partb = min(sum(eq(abs(c - p)) for c in crabs) for p in range(min(crabs), max(crabs)))
print(parta)
print(partb)

def eq(n):
    return int(0.5 * n ** 2 + 0.5 * n)


crabs = [int(x) for x in open("assets/day07.txt").read().split(",")]

parta = min(sum(abs(c - p) for c in crabs) for p in range(min(crabs), max(crabs)))
partb = min(sum(eq(abs(c - p)) for c in crabs) for p in range(min(crabs), max(crabs)))
print(parta)
print(partb)

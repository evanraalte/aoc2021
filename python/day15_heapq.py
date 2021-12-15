from collections import defaultdict
from heapq import *


def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))

    q, seen, mins = [(0, f, ())], set(), {f: 0}
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t:
                return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen:
                    continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf"), None


if __name__ == "__main__":
    with open("assets/day15.txt") as f:
        costs = {(x, y): int(num) for (y, line) in enumerate(f.read().split("\n")) for (x, num) in enumerate(line)}
        x_max = max(map(lambda x: x[0], costs.keys()))
        y_max = max(map(lambda y: y[1], costs.keys()))

        costs_b = {}
        for n in range(0, 5):
            for (x, y), v in costs.items():
                costs_b[((x_max + 1) * n + x, y)] = (v + n) - 9 if (v + n) >= 10 else (v + n)
        costs = costs_b
        costs_b = {}
        for n in range(0, 5):
            for (x, y), v in costs.items():
                costs_b[(x, (y_max + 1) * n + y)] = (v + n) - 9 if (v + n) >= 10 else (v + n)
        costs = costs_b

        edges = [
            ((x, y), d, costs[d])
            for (x, y) in costs.keys()
            for d in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
            if d in costs
        ]

    print(dijkstra(edges, (0, 0), (499, 499))[0])

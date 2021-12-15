from math import inf, isinf
from collections import defaultdict

# min_cost = inf


# def find_path(start, length=0):
#     global min_cost
#     if length >= min_cost:
#         return
#     x, y = start
#     search_area = [(x + 1, y), (x, y + 1)]
#     if all(map(lambda p: isinf(cavern[p]), search_area)):
#         if length < min_cost:
#             min_cost = length
#         return
#     for p in search_area:
#         if isinf(cavern[p]):
#             continue
#         find_path(p, length + cavern[p])


with open("assets/day15-sample.txt") as f:
    costs = {(x, y): int(num) for (y, line) in enumerate(f.read().split("\n")) for (x, num) in enumerate(line)}
    edges = {}
    for (x, y) in costs.keys():
        edges[(x, y)] = [
            (d, costs[d]) for d in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)] if d in costs
        ]  # source: dest, weight
    vertices = defaultdict(lambda: inf)
    vertices[(0, 0)] = 0  # update costs for first vertice


visited = set()


def update_adj_vertices(vertice):
    visited.add(vertice)
    neighbours = edges[vertice]
    for n, w in neighbours:
        if n[0] == inf or n[1] == inf:
            continue
        if n not in visited and vertices[vertice] + w < vertices[n]:
            vertices[n] = vertices[vertice] + w


while visited != set(costs.keys()):
    t = min(filter(lambda v: (v not in visited), vertices), key=lambda k: vertices[k])
    update_adj_vertices(t)

x_max = max(map(lambda x: x[0], edges.keys()))
y_max = max(map(lambda y: y[1], edges.keys()))

# buf = ""
# for y in range(0, 10):
#     for x in range(0, 10):
#         ws = 3 - len(str(vertices[(x, y)]))
#         buf += f"{vertices[(x,y)]}" + " " * ws
#     buf += '\n'
# print(buf)
print(vertices[(x_max, y_max)])

from math import inf

with open("assets/day15.txt") as f:
    costs = {(x, y): int(num) for (y, line) in enumerate(
        f.read().split("\n")) for (x, num) in enumerate(line)}
    x_max = max(map(lambda x: x[0], costs.keys()))
    y_max = max(map(lambda y: y[1], costs.keys()))

    costs_b = {}
    for n in range(0, 5):
        for (x, y), v in costs.items():
            costs_b[((x_max+1)*n+x, y)] = (v+n)-9 if (v + n) >= 10 else (v+n)
    costs = costs_b
    costs_b = {}
    for n in range(0, 5):
        for (x, y), v in costs.items():
            costs_b[(x, (y_max+1)*n+y)] = (v+n)-9 if (v + n) >= 10 else (v+n)
    costs = costs_b

    edges = {}
    for (x, y) in costs.keys():
        edges[(x, y)] = (
            (d, costs[d]) for d in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)] if d in costs
        )  # source: dest, weight
    vertices = {k: inf for k in edges.keys()}
    vertices[(0, 0)] = 0  # update costs for first vertice
    vertices_to_check = set(vertices.keys())


def update_adj_vertices(vertice):
    vertices_to_check.remove(vertice)
    neighbours = edges[vertice]
    for n, w in neighbours:
        if n in vertices_to_check and vertices[vertice] + w < vertices[n]:
            vertices[n] = vertices[vertice] + w


while vertices_to_check:
    t = min(vertices_to_check, key=lambda k: vertices[k])
    update_adj_vertices(t)
x_max = max(map(lambda x: x[0], edges.keys()))
y_max = max(map(lambda y: y[1], edges.keys()))

print(vertices[(x_max, y_max)])

from functools import reduce

with open("assets/day09.txt") as f:
    basin = {
        (x, y): int(num)
        for (y, line) in enumerate(f.read().split("\n"))
        for (x, num) in enumerate(line)
    }


def get_depth(c):
    return basin.get(c, 9)


def get_pond_coordinates(c, parent=None):
    pond_coordinates = set([c])
    x, y = c
    neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for neighbour in neighbours:
        if (neighbour != parent) and (9 > get_depth(neighbour) >= get_depth(c)):
            pond_coordinates = pond_coordinates.union(
                get_pond_coordinates(neighbour, c)
            )
    return pond_coordinates


def is_low_point(c):
    x, y = c
    coords = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return all(map(lambda n: get_depth(n) > get_depth(c), coords))


bottom_coordinates = list(filter(lambda k: is_low_point(k), basin.keys()))
parta = sum(map(lambda k: basin[k] + 1, bottom_coordinates))
print(f"Part A: {parta}")

three_largest_ponds = sorted(
    len(get_pond_coordinates(lp)) for lp in map(lambda bc: bc, bottom_coordinates)
)[-3:]
partb = reduce(lambda x, y: x * y, three_largest_ponds)
print(f"Part B: {partb}")

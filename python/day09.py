from functools import reduce

with open("assets/day09.txt") as f:
    basin = {
        (x, y): int(num)
        for (y, line) in enumerate(f.read().split("\n"))
        for (x, num) in enumerate(line)
    }


def get_pond_coordinates(basin, c, existing_pond_coordinates=None):
    if existing_pond_coordinates is None:
        existing_pond_coordinates = set()
    existing_pond_coordinates.add(c)
    x, y = c
    neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for neighbour in neighbours:
        if (neighbour not in existing_pond_coordinates) and (9 > basin.get(neighbour, 9) >= basin.get(c, 9)):
            get_pond_coordinates(basin, neighbour, existing_pond_coordinates)
    return existing_pond_coordinates


def is_low_point(basin, c):
    x, y = c
    coords = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return all(map(lambda n: basin.get(n, 9) > basin.get(c, 9), coords))


bottom_coordinates = list(
    filter(lambda k: is_low_point(basin, k), basin.keys()))
parta = sum(map(lambda k: basin[k] + 1, bottom_coordinates))
print(f"Part A: {parta}")

three_largest_ponds = sorted(
    len(get_pond_coordinates(basin, lp)) for lp in map(lambda bc: bc, bottom_coordinates)
)[-3:]
partb = reduce(lambda x, y: x * y, three_largest_ponds)
print(f"Part B: {partb}")

with open("assets/day09-sample.txt") as f:
    data = {
        (x, y): int(num)
        for (y, line) in enumerate(f.read().split("\n"))
        for (x, num) in enumerate(line)
    }
    x_max = max(list(data.keys()), key=lambda x: x[0])[0]
    y_max = max(list(data.keys()), key=lambda y: y[1])[1]


def get_coord(c):
    if c in data:
        return data[c]
    else:
        return 9


def get_basin_size(c):

    size = 1
    x, y = c
    coords = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for coord in coords:
        if 9 > get_coord(coord) >= get_coord(c):
            print(f"{coord}")
            size += get_basin_size(coord)
    return size


def is_low_point(c):
    x, y = c
    coords = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return all(map(lambda n: get_coord(n) > get_coord(c), coords))


low_points = list(filter(lambda k: is_low_point(k[0]), data.items()))
parta = sum(map(lambda v: v[1] + 1, low_points))
print(f"Part A: {parta}")

s = [get_basin_size(lp) for lp in map(lambda k: k[0], low_points)]

pass

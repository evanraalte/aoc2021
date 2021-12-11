import itertools


def print_steps(step):
    print("step ", step)
    for y in range(0, max(map(lambda y: y[1], octopuses.keys())) + 1):
        buf = ""
        for x in range(0, max(map(lambda x: x[0], octopuses.keys())) + 1):
            buf += str(octopuses[(x, y)])
        print(buf)


with open("assets/day11.txt") as f:
    octopuses = {(x, y): int(num) for (y, line) in enumerate(f.read().split("\n")) for (x, num) in enumerate(line)}
total = 0
all_flashed = False
step = 0
while not all_flashed:
    step += 1
    exploded_octopuses = set()
    for location in octopuses.keys():
        octopuses[location] += 1

    while any(map(lambda x: x == 10, octopuses.values())):
        for location, octopus in filter(lambda v: v[1] == 10, octopuses.items()):
            exploded_octopuses.add(location)  # add it to already exploded octopuses
            for dx, dy in itertools.product([-1, 0, 1], [-1, 0, 1]):
                n = (location[0] + dx, location[1] + dy)
                if octopuses.get(n) and octopuses[n] != 10 and n not in exploded_octopuses:
                    octopuses[n] += 1
            octopuses[location] = 0
    total += len(exploded_octopuses)
    if step == 100:
        print("PartA: ", total)
    if len(exploded_octopuses) == len(octopuses):
        print("PartB: ", step)
        all_flashed = True
    pass

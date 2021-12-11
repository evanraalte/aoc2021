import itertools

with open("assets/day11.txt") as f:
    octopuses = {(x, y): int(num) for (y, line) in enumerate(f.read().split("\n")) for (x, num) in enumerate(line)}
total = 0
all_flashed = False
step = 0
while not all_flashed:
    step += 1
    flashed_octopuses = set()
    for location in octopuses.keys():
        octopuses[location] += 1

    while len(flashing_octopuses := list(filter(lambda v: v[1] == 10, octopuses.items()))):
        for location, octopus in flashing_octopuses:
            flashed_octopuses.add(location)  # add it to already exploded octopuses
            for dx, dy in itertools.product([-1, 0, 1], repeat=2):
                n = (location[0] + dx, location[1] + dy)
                if octopuses.get(n) and octopuses[n] != 10 and n not in flashed_octopuses:
                    octopuses[n] += 1
            octopuses[location] = 0
    total += len(flashed_octopuses)
    if step == 100:
        print("PartA: ", total)
    if len(flashed_octopuses) == len(octopuses):
        print("PartB: ", step)
        all_flashed = True
    pass

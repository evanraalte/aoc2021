data = open("assets/day05.txt").read().split("\n")


def get_fields_larger_than_one(data, partb=False):
    vents = {}

    for line in data:
        (x_start, y_start), (x_end, y_end) = tuple(
            tuple(int(x) for x in c.split(",")) for c in line.split(" -> ")
        )
        increment_y = 1 if y_end > y_start else -1
        increment_x = 1 if x_end > x_start else -1
        if x_start == x_end or y_start == y_end:  # horizontal/vertical line
            for x in range(x_start, x_end + increment_x, increment_x):
                for y in range(y_start, y_end + increment_y, increment_y):
                    if (x, y) not in vents:
                        vents[(x, y)] = 0
                    vents[(x, y)] += 1
        elif partb:  # diagonal line
            y = y_start
            for x in range(x_start, x_end + increment_x, increment_x):
                if (x, y) not in vents:
                    vents[(x, y)] = 0
                vents[(x, y)] += 1
                y += increment_y
    return sum(1 for x in vents.values() if x > 1)


print(f"Part A: {get_fields_larger_than_one(data, partb= False)}")
print(f"Part A: {get_fields_larger_than_one(data, partb= True)}")

def count_zeros_ones(l):
    return l.count("0"), l.count("1")


def transpose(arr):
    lines = [list(line) for line in arr]
    return list(map(list, zip(*lines)))


def get_power_rate(lines):
    transposed_lines = transpose(lines)
    epsilon = 0
    gamma = 0
    for line in transposed_lines:
        gamma = gamma << 1
        epsilon = epsilon << 1
        z, o = count_zeros_ones(line)
        if o > z:  # one is most common
            gamma += 1
        elif z > o:  # zero is most common
            epsilon += 1
        else:
            raise Exception("Something went wrong here..")
    return epsilon * gamma


def find_value(lines, criteria):
    max_iterations = len(lines[1])
    mask = ""
    for i in range(0, max_iterations):
        transposed_lines = transpose(lines)
        z, o = count_zeros_ones(transposed_lines[i])
        mask += str(int(not ((z <= o) ^ bool(criteria))))
        lines = list(filter(lambda l: l.startswith(mask), lines))
        if len(lines) == 1:
            break
    return int(lines[0], 2)


report = open("assets/day03.txt").read().splitlines()

print(f"Part A: {get_power_rate(report)}")

print(f"Part B: {find_value(report, 1) * find_value(report, 0)}")

def has_more_ones(l):
    return l.count("1") >= l.count("0")


def transpose(arr):
    lines = [list(line) for line in arr]
    return list(map(list, zip(*lines)))


def get_power_rate(lines):
    transposed_lines = transpose(lines)
    gamma = 0
    for line in transposed_lines:
        gamma = gamma << 1
        gamma += int(has_more_ones(line))
    return gamma * (2 ** len(transposed_lines) - 1 - gamma)


def find_value(lines, criteria):
    max_iterations = len(lines[1])
    mask = ""
    for i in range(0, max_iterations):
        tl = list(map(lambda l: l[i], lines))
        mask += str(int(not ((has_more_ones(tl)) ^ bool(criteria))))  # NOR gate
        lines = list(filter(lambda l: l.startswith(mask), lines))
        if len(lines) == 1:
            break
    return int(lines[0], 2)


report = open("assets/day03.txt").read().splitlines()

print(f"Part A: {get_power_rate(report)}")

print(f"Part B: {find_value(report, 1) * find_value(report, 0)}")

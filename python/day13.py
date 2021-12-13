def min_max(dots):
    xmin, xmax = min(dots, key=lambda x: x[0])[0], max(dots, key=lambda x: x[0])[0]
    ymin, ymax = min(dots, key=lambda y: y[1])[1], max(dots, key=lambda y: y[1])[1]
    return ((xmin, xmax), (ymin, ymax))


def print_dots(dots):
    ((xmin, xmax), (ymin, ymax)) = min_max(dots)
    for y in range(ymin, ymax + 1):
        buf = ""
        for x in range(xmin, xmax + 1):
            buf += '#' if (x, y) in dots else ' '
        print(buf)


with open("assets/day13.txt") as f:
    dots_entry, fold_entries = tuple(f.read().split("\n\n"))
    parse = lambda x: (x[0], int(x[1]))
    folds = [parse(fold.lstrip("fold along ").split("=")) for fold in fold_entries.splitlines()]
    dots = {map(int, dot.split(",")) for dot in dots_entry.splitlines()}


def fold(dots, axis, delta):
    if axis == 'y':
        dots = {(x, (2 * delta - y) if y > delta else y) for x, y in dots}
    elif axis == 'x':
        dots = {((2 * delta - x) if x > delta else x, y) for x, y in dots}
    return dots


first = True
for instr in folds:
    dots = fold(dots, *instr)
    if first:
        print("Part A", len(dots))
        first = False
print("Part B:")
print_dots(dots)

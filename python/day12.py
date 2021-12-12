paths = [tuple(line.split("-")) for line in open("assets/day12.txt").read().split("\n")]

splits = {}
for start, end in paths:
    if start not in splits:
        splits[start] = set()
    splits[start].add(end)
    if start != "start" and end != "end":
        if end not in splits:
            splits[end] = set()
        splits[end].add(start)  # add ways back


seen = set()
paths = set()

small_letters = [l for l in splits.keys() if l.islower() and l not in ["start", "end"]]


def find_paths(start, twice=None, path=[], seen=set(["start"]), seen_twice=False):
    seen = seen.copy()
    path = path[:]
    path.append(start)
    if start == "end":
        paths.add(",".join(path))
        return

    for option in splits[start]:
        if (option not in seen) or ((twice == option) and (option in seen) and (not seen_twice)):
            seen_child = seen.copy()
            seen_twice_child = seen_twice
            if option in seen:  # this is only valid if the chosen small cave already occured
                seen_twice_child = True
            elif option.islower():  # otherwise add it to seen if it is a small cave
                seen_child.add(option)
            find_paths(option, twice, path, seen_child, seen_twice_child)


find_paths("start", twice=None)
print("Part A: ", len(paths))

seen = set()
paths = set()

for l in small_letters:
    find_paths("start", twice=l)
print("Part B: ", len(paths))

pass

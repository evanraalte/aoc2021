from collections import defaultdict

paths = [tuple(line.split("-")) for line in open("assets/day12.txt").read().split("\n")]

splits = defaultdict(set)
for start, end in paths:
    splits[start].add(end)
    splits[end].add(start)

seen = set()
paths = set()


def find_paths(start, twice=None, path=[], seen=set(["start"]), seen_twice=False):
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

small_letters = [sl for sl in splits.keys() if sl.islower() and sl not in ["start", "end"]]
for sl in small_letters:
    find_paths("start", twice=sl)
print("Part B: ", len(paths))

pass

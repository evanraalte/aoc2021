with open("assets/day14.txt") as f:
    cur_pol, pair_insertions = tuple(f.read().split("\n\n"))
    pair_insertions = {p.split(" -> ")[0]: p.split(" -> ")[1] for p in pair_insertions.splitlines()}

pass
print(f"step {0}: {cur_pol}")
for step in range(1, 40 + 1):
    print(step)
    pairs = {}
    for k, v in pair_insertions.items():
        if k in cur_pol:
            pairs[k] = k[0] + v + k[1]
    next_polymer = ""
    for chunk in [cur_pol[i : i + 2] for i in range(0, len(cur_pol))]:
        if chunk in pairs.keys():
            next_polymer += pairs[chunk][:2]
        else:
            next_polymer += chunk[0]
    cur_pol = next_polymer

    # print(f"step {step}: {len(cur_pol)}")
    if step == 10:
        num = [cur_pol.count(c) for c in set(cur_pol)]
        print("Part A: ", max(num) - min(num))
    if step == 40:
        num = [cur_pol.count(c) for c in set(cur_pol)]
        print("Part B: ", max(num) - min(num))

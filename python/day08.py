import re

data = open("assets/day08.txt").read().split("\n")

lut = {
    1: 2,
    4: 4,
    7: 3,
    8: 7
}

count = 0
for line in data:
    signals, outputs = line.split(" | ")
    for output in outputs.split(" "):
        if len(output) in map(lambda l: lut[l], [1, 4, 7, 8]):
            count += 1
print(f"Part A: {count}")

segments = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}

total = 0
for line in data:
    signals, outputs = line.split(" | ")
    options = {l: "abcdefg" for l in list("abcdefg")}

    # 6 character properties 3 chars should differ, and we know where not to place them
    tmp = [s for s in signals.split(" ") if len(s) == 6]
    chars_skip = re.sub(
        f"[{''.join(c for c in 'abcdefg' if all(c in t for t in tmp))}]", "", 'abcdefg')
    for s_id, s_value in options.items():
        if s_id not in "cde":
            options[s_id] = re.sub(f"[{chars_skip}]", "", s_value)

    # Stage two, filter out segments for known shapes
    for signal in signals.split(" "):
        for distinct_value, length in lut.items():
            if len(signal) == length:
                exclude_items = re.sub(
                    f"[{segments[distinct_value]}]", "", "abcdefg")
                for item in exclude_items:  # exclude characters
                    options[item] = re.sub(f"[{signal}]", "", options[item])
                for i in segments[distinct_value]:
                    # exclude excluded items
                    tmp = re.sub(f"[{signal}]", "", "abcdefg")
                    if tmp != '':
                        options[i] = re.sub(f"[{tmp}]", "", options[i])
    finished_chars = "".join(v for v in options.values() if len(v) == 1)
    while not all(map(lambda v: len(v) == 1, options.values())):
        for k, v in options.items():
            if len(v) != 1:
                options[k] = re.sub(f"[{finished_chars}]", "", v)

    # mapping complete yey
    inv_options = {v: k for k, v in options.items()}
    inv_segments = {v: k for k, v in segments.items()}
    num = ""
    for output in outputs.split():
        res = "".join(sorted("".join(inv_options[c] for c in output)))
        num += str(inv_segments[res])
    total += int(num)
print(f"Part B: {total}")
pass

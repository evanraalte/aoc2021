chunk_end = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">",
}

score = {
    "}": 57,
    ")": 3,
    "]": 1197,
    ">": 25137,
}


class LineNotFinishedException(Exception):
    pass


def check_chunk(chunk, remainder):
    closed = False
    msg = None
    while not closed:
        if remainder == "":
            return (msg, remainder)
        elif remainder[0] in "{([<":
            msg, remainder = check_chunk(
                remainder[0], remainder[1:]
            )  # solve a new chunk up the stack
            if msg is not None:
                return (msg, None)  # propagate error down the stack
            continue
        elif remainder[0] == chunk_end[chunk]:
            closed = True
        else:
            msg = (remainder[0], chunk_end[chunk])
            break
    return (msg, remainder[1:])


data = open("assets/day10-sample.txt").read().split("\n")
total = 0
for line in data:
    print(f"checking {line}")
    rem = line[1:]
    while rem:  # while the whole thing is not consumed
        msg, rem = check_chunk(line[0], rem)
        if msg is not None:
            found, expected = msg
            print(f"{found} -> +{score[found]}")
            total += score[found]
print(f"Part A: {total}")

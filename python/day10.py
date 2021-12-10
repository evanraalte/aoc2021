from functools import reduce

chunk_end = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">",
}

score = {
    "}": 1197,
    ")": 3,
    "]": 57,
    ">": 25137,
}


class LineNotFinishedException(Exception):
    line = ""

    def __init__(self, chunk, line=None) -> None:
        if line:
            self.line = line
        self.line += chunk_end[chunk]


class InvalidLineException(Exception):
    def __init__(self, found, expected) -> None:
        self.expected = expected
        self.found = found


def check_chunk(chunk, remainder):
    closed = False
    while not closed:
        if remainder == "":
            raise LineNotFinishedException(chunk)
        elif remainder[0] in "{([<":
            try:
                remainder = check_chunk(
                    remainder[0], remainder[1:]
                )  # solve a new chunk up the stack
            except LineNotFinishedException as e:
                raise LineNotFinishedException(chunk, e.line)
        elif remainder[0] == chunk_end[chunk]:
            closed = True
        else:
            found = remainder[0]
            expected = chunk_end[chunk]
            raise InvalidLineException(found, expected)
    return remainder[1:]


data = open("assets/day10.txt").read().split("\n")
total = 0
partb = []
for line in data:
    evaluate_line = True
    rem = line[:]
    while evaluate_line and rem:  # while the whole thing is not consumed
        try:
            rem = check_chunk(rem[0], rem[1:])
        except LineNotFinishedException as e:
            sub = 0
            for c in e.line:
                sub *= 5
                sub += ")]}>".index(c) + 1
            partb.append(sub)
            print(f"Finish line by adding: {e.line} -> + {sub}")
            evaluate_line = False
        except InvalidLineException as e:
            evaluate_line = False
            print(f"expected '{e.expected}', found '{e.found}' -> +{score[e.found]}")
            total += score[e.found]

print(f"Part A: {total}")
print(f"Part B: {sorted(partb)[(len(partb)-1)//2]}")

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


class InvalidLineException(Exception):
    def __init__(self, found, expected) -> None:
        self.expected = expected
        self.found = found


def check_chunk(chunk, remainder):
    closed = False
    while not closed:
        if remainder == "":
            raise LineNotFinishedException()
        elif remainder[0] in "{([<":
            remainder = check_chunk(
                remainder[0], remainder[1:]
            )  # solve a new chunk up the stack
            continue
        elif remainder[0] == chunk_end[chunk]:
            closed = True
        else:
            found = remainder[0]
            expected = chunk_end[chunk]
            raise InvalidLineException(found, expected)
    return remainder[1:]


data = open("assets/day10-sample.txt").read().split("\n")
total = 0
for line in data:
    evaluate_line = True
    rem = line[1:]
    while evaluate_line and rem:  # while the whole thing is not consumed
        try:
            rem = check_chunk(line[0], rem)
        except LineNotFinishedException:
            evaluate_line = False
        except InvalidLineException as e:
            evaluate_line = False
            print(f"during checking {line}")
            print(f"expected {e.expected}, found {e.found} -> +{score[e.found]}")
            total += score[e.found]
print(f"Part A: {total}")

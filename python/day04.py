class BingoCard:
    def __init__(self, data):
        self.bc = [[0] * 5 for _ in range(5)]
        self.entries = set()
        self.added_entries = set()
        self.latest_entry = 0
        for y, row in enumerate(data.splitlines()):
            for x, field in enumerate(row.split()):
                self.bc[y][x] = int(field)
                self.entries.add(int(field))

    def has_bingo(self):
        has_bingo = False
        for y in range(0, 4):

            has_bingo = all(f in self.added_entries for f in self.bc[y])
            if has_bingo:
                return True

        for x in range(0, 4):
            has_bingo = all(self.bc[i][x] in self.added_entries for i in range(5))
            if has_bingo:
                return True
        return False

    def add_entry(self, num):
        self.latest_entry = num
        self.added_entries.add(num)

    def score(self):
        return sum(self.entries.difference(self.added_entries)) * self.latest_entry


data = open("assets/day04.txt").read().split("\n\n")


def play_bingo(data):
    numbers = list(map(lambda x: int(x), data[0].split(",")))
    bingo_card_data = data[1:]
    bingo_cards = []
    for bcd in bingo_card_data:
        bingo_cards.append(BingoCard(bcd))

    for number in numbers:
        for num, bc in enumerate(bingo_cards):
            bc.add_entry(number)
            if bc.has_bingo():
                return bc.score()
        pass


def last_to_win(data):
    numbers = list(map(lambda x: int(x), data[0].split(",")))
    bingo_card_data = data[1:]
    bingo_cards = []
    for bcd in bingo_card_data:
        bingo_cards.append(BingoCard(bcd))

    won = [False] * len(bingo_cards)
    last_score = None
    for number in numbers:
        for num, bc in enumerate(bingo_cards):
            if not won[num]:
                bc.add_entry(number)
                if bc.has_bingo():
                    won[num] = True
                    last_score = bc.score()
        if all(won):
            return last_score
    return last_score


score = play_bingo(data)
print(f"Part A: {score}")
score = last_to_win(data)
print(f"Part B: {score}")

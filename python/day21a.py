p = {
    0: 5,
    1:2
}
score = {
    0: 0,
    1:0
}

class dice:
    def __init__(self):
        self.num = 100

    def __iter__(self):
        return self
    def __next__(self):
        return self.next()

    def next(self):
        if self.num < 100:
            self.num += 1
        else:
            self.num = 1
        return self.num
        raise StopIteration()


d = dice()

won = False
turn = 0
cnt = 0
while not won:
    cnt += 1
    p[turn] = (p[turn] + sum(next(d) for _ in range(0,3))) % 10
    score[turn] += p[turn] +1
    print(f"player {turn} moves to {p[turn] + 1} for total score of {score[turn]}")
    won = score[turn] >= 1000
    turn = 1 - turn

print(cnt*3*score[turn])
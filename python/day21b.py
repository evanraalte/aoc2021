from functools import cache

p = [5,2]
score = [0,0]

def add_tuple(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])



@cache
def play(scores, turn, p, throw_sum=0, throw_num=0):
    scores_new = list(scores)
    p_new = list(p)
    wins = (0,0)

    if throw_num==3: # Third throw has passed
        p_new[turn] = (p[turn] + throw_sum) % 10
        scores_new[turn] = scores[turn] + p_new[turn] +1
        # print(f"player {turn} moves to {p_new[turn] + 1} for total score of {scores_new[turn]}")
        if scores_new[turn] >= 21: # if 21 then has won, assign score and return
            tmp = [0,0]
            tmp[turn] = 1
            return tuple(tmp)
        else: # the other player can play now
            wins = play(tuple(scores_new), 1-turn, tuple(p_new))
    else: # first, second or thrid throw has to start
        for throw in range(1,3+1): # create three universes
            throw_sum_next = throw + throw_sum
            wins = add_tuple(wins, play(tuple(scores_new), turn, tuple(p_new), throw_sum_next, throw_num+1))

    return wins

res = list(play(tuple(score),0,tuple(p)))
print(res)
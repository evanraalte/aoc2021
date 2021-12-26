from math import floor, ceil
# [[[[[9,8],1],2],3],4] becomes [[[[0,9],2],3],4] (the 9 has no regular number to its left, so it is not added to any regular number).
# [7,[6,[5,[4,[3,2]]]]] becomes [7,[6,[5,[7,0]]]] (the 2 has no regular number to its right, and so it is not added to any regular number).
# [[6,[5,[4,[3,2]]]],1] becomes [[6,[5,[7,0]]],3].
# [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]] becomes [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] (the pair [3,2] is unaffected because the pair [7,3] is further to the left; [3,2] would explode on the next action).
# [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] becomes [[3,[2,[8,0]]],[9,[5,[7,0]]]].


# data = [[6,[5,[4,[3,2]]]],1]

def add_list(l0, l1):
    return [l0,l1]

data = [[3,[2,[1,[7,3]]]],[1,1]] # add_list([[[[4,3],4],4],[7,[[8,4],9]]], [1,1])
def reduce(data,depth=0, exploded=False, split=False, rem=(0,0)):
    r,l = rem
    if isinstance(data, int):
        if data >= 10:
            return ([floor(data/2), ceil(data/2)], (0,0), exploded, True)
        else:
            # absorb remainder
            return (data+r+l, (0,0), exploded, split)
    elif depth == 4:
        if not exploded:
            l,r = tuple(data)
            return (0, (l,r), True, split)
        else:
            return (data, (0,0), exploded, split)
    else:
        data[0], (left,right), exploded, split = reduce(data[0], depth+1, exploded, split, rem)
        data[1], (left,right), exploded, split = reduce(data[1], depth+1, exploded, split, rem)
        return ([data[0], data[1]], (left, right), exploded, split)
        

print(data)
done = False
while not done:
    data, rem, exploded, split = reduce(data)
    done = not exploded and not split
    print(data)
    pass
    

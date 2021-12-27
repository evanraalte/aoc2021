from math import floor, ceil
# [[[[[9,8],1],2],3],4] becomes [[[[0,9],2],3],4] (the 9 has no regular number to its left, so it is not added to any regular number).
# [7,[6,[5,[4,[3,2]]]]] becomes [7,[6,[5,[7,0]]]] (the 2 has no regular number to its right, and so it is not added to any regular number).
# [[6,[5,[4,[3,2]]]],1] becomes [[6,[5,[7,0]]],3].
# [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]] becomes [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] (the pair [3,2] is unaffected because the pair [7,3] is further to the left; [3,2] would explode on the next action).
# [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] becomes [[3,[2,[8,0]]],[9,[5,[7,0]]]].


data = "[[[[[9,8],1],2],3],4]"
data = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
def convert_to_list(hier):
    depth = 0
    buf = ""
    depth_db = {}
    # depth_complete = False
    # last_depth = None
    for d, num in hier:
        if num is None:
            depth_db[d] = not depth_db.get(d,False)
        if depth < d:
            if buf != '' and buf[-1] == ']':
                buf += ','
            if buf != '' and buf[-1] in "1234567890":
                buf += ','
            # while depth < d:
            buf += "["
            depth +=1
        elif depth > d:
            # while depth > d:
            buf += "]"
            depth -=1
        elif depth == d:
            # if last_depth == depth and depth_complete:
            #     buf += "],["
            # else:
            buf += ","
            # depth_complete = False
        # if buf[-1] == ']':
            # buf += ','
        if num is not None:
            buf += str(num)
            # if depth in depth_db and depth_db[depth]:
            #     depth_db[depth] = False
            #     depth_complete = True
            #     last_depth = depth
    while depth > 0:
        buf += "]"
        depth -= 1

    return buf
        


def convert_to_hierarchy(data):
    ptr = 0
    depth = 0
    buf = []
    while ptr < len(data):
        if data[ptr] == '[':
            depth += 1
            ptr += 1
            if ptr < len(data) and data[ptr] == '[':
                buf.append((depth, None))
        elif data[ptr] == ']':
            depth -= 1
            ptr += 1
            if ptr < len(data) and data[ptr] in '],':
                buf.append((depth, None))
        elif data[ptr] == ',':
            ptr += 1
            continue
        else:
            num_buf = ""
            while data[ptr].isdigit():
                num_buf += data[ptr]
                ptr += 1
            buf.append((depth, int(num_buf)))
    return buf

def _reduce(hier):
    pair = [(idx, h[1]) for idx, h in enumerate(hier) if h[0] == 5]
    if len(pair) >=2:
        idx0, val = pair[0]
        _idx0 = idx0
        while _idx0 > 0:
            try:
                d,v = hier[_idx0-1]
                hier[_idx0-1] = (d, v + val)
                break
            except TypeError:
                _idx0 -= 1
        idx1, val = pair[1]
        _idx1 = idx1
        while _idx1 < len(hier)-1:
            try:
                d,v = hier[_idx1+1]
                hier[_idx1+1] = (d, v + val)
                break
            except TypeError:
                _idx1 += 1
        hier.pop(idx1+1)
        hier.pop(idx1)
        hier[idx0] = (4,0)
        if hier[idx0-1] == (4,None):
            hier.pop(idx0-1)
        pass
    else:
        lgt =[idx for idx, h in enumerate(hier) if h[1] is not None and h[1]>= 10]
        if len(lgt) > 0:
            idx= lgt[0]
            d,v = hier[idx]
            hier[idx] = (d+1, floor(v/2))
            hier.insert(idx+1,(d,None))
            hier.insert(idx+1,(d+1, ceil(v/2)))
            hier.insert(idx,(d,None))
            pass
    return hier

def add_hier(h1, h2):
    fill = [(1,None)]
    h1 = [(d+1,v) for d,v in h1]
    h2 = [(d+1,v) for d,v in h2]
    buf = fill + h1 + fill + h2 + fill

    return buf

with open("assets/day18.txt") as f:
    data = f.read().splitlines()
total = None
for line in data:
    hier = convert_to_hierarchy(line)
    if total is not None:
        hier = add_hier(total,hier)
    hier_old = None
    while str(hier) != hier_old:
        hier_old = str(hier)
        hier = _reduce(hier)
    total = hier.copy()
    l = convert_to_list(hier)
    print(l)

def calc_sum(ls):
    if isinstance(ls, int):
        return ls
    return 3*calc_sum(ls[0]) + 2*calc_sum(ls[1])
    
l = eval(l)
s = calc_sum(l)
# hier = convert_to_hierarchy(l)
# print(s)
pass

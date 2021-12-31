from collections import defaultdict, Counter
import time
program = open("assets/day24.txt").read().split('\n')
stack = []
idx = 0
checklist = []
for i in range(0,14):
    a = int(program[i*18+4].split()[2])
    b = int(program[i*18+5].split()[2])
    c = int(program[i*18+15].split()[2])
    if a == 1: #push
        stack.append((idx,c))
    elif a == 26: # pop
        tmp = stack.pop()
        checklist.append(((tmp[0], tmp[1]+b), idx))
    idx += 1

I = [None]*14
for (i1, v), i2 in checklist:
    if v < 0:
        I[i1] = 9
        I[i2] = 9 + v
    else:
        I[i1] = 9 - v
        I[i2] = 9
print("".join(map(str,I)))

I = [None]*14
for (i1, v), i2 in checklist:
    if v < 0:
        I[i1] = 1 - v
        I[i2] = 1
    else:
        I[i1] = 1
        I[i2] = 1 + v
print("".join(map(str,I)))
pass
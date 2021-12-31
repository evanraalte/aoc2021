from collections import defaultdict, Counter
import time
program = open("assets/day24.txt").read().split('\n')
stack = []
idx = 0
checklist = []
for i in range(0,18*14,18):
    a = int(program[i+4].split()[2])
    b = int(program[i+5].split()[2])
    c = int(program[i+15].split()[2])
    if a == 1: #push
        stack.append((idx,c))
    elif a == 26: # pop
        tmp = stack.pop()
        checklist.append(((tmp[0], tmp[1]+b), idx))
    idx += 1
Imax = [None]*14
Imin = [None]*14
for (i1, v), i2 in checklist:
    if v < 0:
        Imax[i1] = 9
        Imax[i2] = 9 + v
        Imin[i1] = 1 - v
        Imin[i2] = 1
    else:
        Imax[i1] = 9 - v
        Imax[i2] = 9
        Imin[i1] = 1
        Imin[i2] = 1 + v
print("".join(map(str,Imax)))
print("".join(map(str,Imin)))
pass
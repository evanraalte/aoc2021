from collections import defaultdict
alg,_,*image = open("assets/day20.txt").read().split('\n')

image = {(x,y): px
      for y,row in enumerate(image)
      for x,px in enumerate(row)}
search_field = lambda x,y: [(x+dx, y+dy) for dy in [-1,0,1] for dx in [-1,0,1]]

def min_max(dots):
    xmin, xmax = min(dots, key=lambda x: x[0])[0], max(dots, key=lambda x: x[0])[0]
    ymin, ymax = min(dots, key=lambda y: y[1])[1], max(dots, key=lambda y: y[1])[1]
    return ((xmin, xmax), (ymin, ymax))


def print_dots(dots):
    ((xmin, xmax), (ymin, ymax)) = min_max(dots)
    for y in range(ymin, ymax + 1):
        buf = ""
        for x in range(xmin, xmax + 1):
            buf += dots.get((x,y),'.')
        print(buf)


for i in range(0,49+1):
    xmin,xmax = min(image.keys(),key=lambda k:k[0])[0],max(image.keys(),key=lambda k:k[0])[0]
    ymin,ymax = min(image.keys(),key=lambda k:k[1])[1],max(image.keys(),key=lambda k:k[1])[1]
    print(xmin, xmax, ymin, ymax)
    out = {}
    for x in range(xmin-1, xmax+2):
        for y in range(ymin-1, ymax+2):
            c = x,y
            binary = int("".join(map(lambda cs: image.get(cs,'#' if i%2 else '.'),search_field(*c))).replace('.','0').replace('#','1'),2)
            out[c] = alg[binary]
        pass
    image = out.copy()
    if i+1 in [2,50]:
        print(list(image.values()).count('#'))
    pass
pass
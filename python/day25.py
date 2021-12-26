from math import floor, ceil

def print_field(field):
    buf = ""
    
    for y in range(y_max+1):
        for x in range(x_max+1):
            buf += field.get((x,y),'.')
        buf += '\n'
    print(buf)


with open("assets/day25.txt") as f:
    field = {(x, y): c for (y, line) in enumerate(
        f.read().split("\n")) for (x, c) in enumerate(line) if c != '.'}
    x_max = max(map(lambda x: x[0], field.keys()))
    y_max = max(map(lambda y: y[1], field.keys()))
pass

def step(field):
    field_next = {}
    moves = 0
    for f,c in field.items():
        x,y = f
        if c == '>' and field.get(((x+1)%(x_max+1),y),'.') == '.':
            moves += 1
            field_next[((x+1)%(x_max+1),y)] = c
        else:
            field_next[f] = c
            # field_next[(x,y)] = '.'
    # print_field(field_next)
    pop_list = []
    add_list = []
    for f,c in field_next.items():
        x,y = f
        if c == 'v' and field_next.get((x,(y+1)%(y_max+1)),'.') == '.':
            moves += 1
            add_list.append((x,(y+1)%(y_max+1)))
            pop_list.append((x,y))

    for a in add_list:
        field_next[a] = 'v'
    for p in pop_list:
        field_next.pop(p)
    return field_next,moves

moves = 1
steps = 0
while moves > 0:
    # print_field(field)
    field,moves = step(field)
    steps += 1
print(steps)
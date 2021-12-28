from functools import cache

state = {
    (0,0) : '.',
    (1,0) : '.',
    (2,1) : 'B',
    (2,2) : 'D',
    (2,3) : 'D',
    (2,4) : 'D',
    (3,0) : '.',
    (4,1) : 'C',
    (4,2) : 'C',
    (4,3) : 'B',
    (4,4) : 'D',
    (5,0) : '.',
    (6,1) : 'C',
    (6,2) : 'B',
    (6,3) : 'A',
    (6,4) : 'A',
    (7,0) : '.',
    (8,1) : 'B',
    (8,2) : 'A',
    (8,3) : 'C',
    (8,4) : 'A',
    (9,0) : '.',
    (10,0) : '.'
}
rooms = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
cost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
rooms_inv = {v: k for k,v in rooms.items()}
DEPTH=4
done = False

@cache
def get_movable_coordinates(state):
    state = eval(state)
    coords = [k for k,v in state.items() if k[1] == 0 and v !='.'] # letters standing in the top
    for letter, column in rooms.items():
        base = [k for k,v in state.items() if k[0] == column and v !='.']
        pass
        base = [b for b in base if b[1] == 1 or state[(b[0], b[1] - 1)] == '.' ] # filter letters that are not on top (can't be moved)
        base = [b for b in base if not all(state[(b[0], i)] == letter for i in range(b[1], DEPTH+1))] # filter out letters that are in place
        coords.extend(base)
    return coords

#############
#...........#
###B#C#C#B###
  #D#D#A#A#
  #########

def get_column(state, num):
    return [ v for k,v in state.items() if k[0] == num]

@cache
def get_valid_moves(state, coord):
    state = eval(state)
    valid_moves = []
    ranges = [range(coord[0]-1, 0-1 , -1), range(coord[0]+1, 10+1) ]
    for rang in ranges:
        for column in rang:
            row = 0
            if column in rooms.values() and rooms_inv[column] != state[coord]: # not allowed to move to different columns
                continue
            # not allowed to move in when others are there
            elif column in rooms.values() and rooms_inv[column] == state[coord] and any(map(lambda x: x not in [rooms_inv[column],'.'], get_column(state,column))): 
                continue
            # go in the room and go as far as possible
            elif column in rooms.values() and rooms_inv[column] == state[coord] and all(map(lambda x: x in [rooms_inv[column],'.'], get_column(state,column))): 
                row = 1
                tmp = None
                while row <= DEPTH and state[(column, row)] == '.':
                    tmp = [(column, row)]
                    row += 1
                return  tmp# best move for sure
            elif state[(column, row)] != '.': # can't move further, stop
                break
            elif coord[1] != 0:
                valid_moves.append((column, row))
    return valid_moves


seen = {}
min_score = 100000
min_moves = None
@cache
def play(state,score=0, move=None, move_num = 1): 
    global min_score
    global min_moves
    if move_num > 30 or score > min_score:
        return
    if (state,move) in seen and seen[(state,move)] < score:
        return  #already been here with this planned move with lower score
    seen[(state,move)] = score
    next_state = eval(state)
    next_score = score
    dst = None
    if move is not None:
        src,dst = move
        next_state[dst] = next_state[src]
        next_state[src] = '.'
        _next_score =  abs(dst[0] - src[0]) + src[1]
        if dst[0] in rooms.values():
            _next_score += dst[1]
        next_score += cost[next_state[dst]] * _next_score
    if all(next_state[c] == room for room in "ABCD" for c in filter(lambda k: k[0] == rooms[room], next_state)):
        if next_score < min_score:
            min_score = next_score
            print(f"{min_score=}")
    # define all possible moves and play
    else:
        scores = []
        for coord in get_movable_coordinates(str(next_state)):
            for _move in get_valid_moves(str(next_state), coord):
                move = (coord,_move)
                play(str(next_state), next_score, move, move_num + 1)
        return scores

play(str(state))
print(min_score)
print(min_moves)
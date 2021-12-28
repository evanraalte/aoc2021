import numpy as np


matrices = []
def generate_matrices(rem=[0,1,2],matrix=[]):
    for idx in rem:
        for v in [-1,1]:
            b = [0,0,0]
            b[idx] = v
            if len(rem) > 1:
                generate_matrices([r for r in rem if r != idx],matrix+b)
            else:
                matrices.append(np.reshape(matrix+b,(3,3)))
            pass

generate_matrices()
matrices = [m for m in matrices if np.linalg.det(m)==1]

with open("assets/day19.txt") as f:
    scanners = f.read().split('\n\n')
    beacons = {}
    for idx, scanners in enumerate(scanners):
        beacons[idx] = list(map(lambda x: tuple(map(int,x.split(","))), scanners.split('\n')[1:]))
        pass

scanners = {}
known = {}
for scanner_idx, _beacons in beacons.items():
    if scanner_idx > 0:
        if scanner_idx not in scanners:
            scanners[scanner_idx] = {}
        scanners[scanner_idx] = _beacons
    else:  
        # for scanner 0 we know everything 
        for _beacon in _beacons:
            x1,y1,z1 = _beacon
            known[_beacon] = None # str(set((x2-x1,y2-y1,z2-z1) for x2,y2,z2 in points if (x2,y2,z2) != point))
    pass

# 
# find mapping
# try to find relative points of scanner 1...n on the known set (start with scanner0)
PT = 12

while len(scanners):
    pop_list = []
    found_match = False

    for point in known.keys():
            x1,y1,z1 = point
            known[point] = set((x2-x1,y2-y1,z2-z1) for x2,y2,z2 in known.keys() if (x2,y2,z2) != point)

    known_inv = {str(v): k for k,v in known.items()}
    pass
    for scanner_idx,beacons in scanners.items():
        # while no 12 points are found, keep rotating!    
        print(scanner_idx)
        for M in matrices:
            rotated_points = list(map(lambda p: np.matmul(M,p).astype(int), beacons))
            relative_map = {}
            for rp in rotated_points:
                x1,y1,z1 = rp
                relative_map[tuple(rp)] = set((x2-x1,y2-y1,z2-z1) for x2,y2,z2 in rotated_points if (x2,y2,z2) != tuple(rp))
            match = {}
            for p,v in relative_map.items():
                # print(p,v)
                # v in known.values is possibly faster, but might be incorrect.
                # sv = eval(v)
                for skv in known.values(): # check if there is a point with the same relative distances
                    # skv = eval(kv)
                    if len(v.intersection(skv)) >= (PT-1): #len(eval(kv).intersection(sv)) >= 3
                        match[p] = known_inv[str(skv)] # known_inv[v] # add the matching coordinate
                        break
        
            if len(match) >= PT:
                print(f"found {PT} overlapping points!\nmatrix:\n",M)
                # convert all scanner 1 beacons to known (scanner0) beacons
                x0,y0,z0 = list(match.items())[0][0] # target
                x1,y1,z1 = list(match.items())[0][1] # base
                transform = lambda x,y,z:  (x + (x1-x0), y + (y1-y0), z + (z1-z0)) 
                for p,v in relative_map.items():
                    known[transform(*p)] = None
                pop_list.append(scanner_idx)
                found_match = True
            if found_match:
                break
        if found_match:
            break
    for p in pop_list:
        scanners.pop(p)
print(len(known))
pass

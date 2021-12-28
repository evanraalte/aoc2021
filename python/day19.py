import numpy as np
import itertools

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

generate_matrices()
matrices = [m for m in matrices if np.linalg.det(m)==1]

with open("assets/day19.txt") as f:
    scanners = f.read().split('\n\n')
    beacons = {}
    for idx, scanners in enumerate(scanners):
        beacons[idx] = list(map(lambda x: tuple(map(int,x.split(","))), scanners.split('\n')[1:]))

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
            known[_beacon] = None

PT = 12
scanner_locations = {}
while len(scanners):
    pop_list = []
    found_match = False

    for point in known.keys():
            x1,y1,z1 = point
            known[point] = set((x2-x1,y2-y1,z2-z1) for x2,y2,z2 in known.keys() if (x2,y2,z2) != point)

    known_inv = {str(v): k for k,v in known.items()}
    pass
    for scanner_idx,beacons in scanners.items():    
        print(scanner_idx)
        for M in matrices:
            rotated_points = list(map(lambda p: np.matmul(M,p).astype(int), beacons))
            relative_map = {}
            for rp in rotated_points:
                x1,y1,z1 = rp
                relative_map[tuple(rp)] = set((x2-x1,y2-y1,z2-z1) for x2,y2,z2 in rotated_points if (x2,y2,z2) != tuple(rp))
            match = {}
            for p,v in relative_map.items():
                for skv in known.values(): # check if there is a point with the same relative distances
                    if len(v.intersection(skv)) >= (PT-1):
                        match[p] = known_inv[str(skv)]
                        break
        
            if len(match) >= PT:
                print(f"found {PT} overlapping points!\nmatrix:\n",M)
                # convert all scanner n beacons to known (scanner0) beacons
                x0,y0,z0 = list(match.items())[0][0] # target
                x1,y1,z1 = list(match.items())[0][1] # base
                transform = lambda x,y,z:  (x + (x1-x0), y + (y1-y0), z + (z1-z0)) 
                scanner_locations[scanner_idx] = transform(0,0,0)
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

def manhattan_distance(pt0, pt1):
    x0,y0,z0 = pt0
    x1,y1,z1 = pt1
    return abs(x1-x0)+ abs(y1-y0)+abs(z1-z0)

distances = max(map(lambda p: manhattan_distance(*p),itertools.permutations(scanner_locations.values(),2)))
print(distances)
lines = open("assets/day22-sample.txt").read().splitlines()
pass
cubes = 0
on = set()

for l in lines:
    print(l)
    cmd, rem = l.split()
    (xmin,xmax),(ymin,ymax),(zmin,zmax) = tuple(tuple(map(int,c.split("=")[1].split(".."))) for c in rem.split(","))
    if cmd == 'on':
        cubes += (xmax-xmin+1) * (ymax-ymin+1) * (zmax-zmin+1)
    else:
        pass
        # cubes -= (xmax-xmin+1) * (ymax-ymin+1) * (zmax-zmin+1)
    print(f"{cubes=}")

    # subtract overlap
    off = set()
    for c in on:
        x = set(range(xmin,xmax+1))&set(range(c[0][0],c[0][1]+1))
        y = set(range(ymin,ymax+1))&set(range(c[1][0],c[1][1]+1))
        z = set(range(zmin,zmax+1))&set(range(c[2][0],c[2][1]+1))
        cubes -= len(x)*len(y)*len(z)
        for d in off: # add overlap that was already turned off
            dx = set(range(d[0][0],d[0][1]+1))&set(range(c[0][0],c[0][1]+1))
            dy = set(range(d[1][0],d[1][1]+1))&set(range(c[1][0],c[1][1]+1))
            dz = set(range(d[2][0],d[2][1]+1))&set(range(c[2][0],c[2][1]+1))
            cubes += len(dx)*len(dy)*len(dz)
            pass
        print(f"{cubes=}")
        try:
            off.add(((min(x),max(x)),(min(y),max(y)),(min(z),max(z))))
        except ValueError:
            pass

    on.add(((xmin,xmax),(ymin,ymax),(zmin,zmax)))
    pass
    

print(cubes)
pass



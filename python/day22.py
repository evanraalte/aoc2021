lines = open("assets/day22-sample.txt").read().splitlines()
pass
cubes = []

def get_volume(cubes):
    volume = 0
    for cube in cubes:
        (xmin,xmax),(ymin,ymax),(zmin,zmax) = cube
        volume += (xmax-xmin+1)*(ymax-ymin+1)*(zmax-zmin+1)
    return volume

for l in lines:
    print(l)
    cmd, rem = l.split()
    (xmin,xmax),(ymin,ymax),(zmin,zmax) = tuple(tuple(map(int,c.split("=")[1].split(".."))) for c in rem.split(","))
    cubes_new = []
    for ((_xmin,_xmax),(_ymin,_ymax),(_zmin,_zmax)) in cubes:
        in_x = any(xmin <= x <= xmax for x in [_xmin,_xmax]) or any(_xmin <= x <= _xmax for x in [xmin,xmax])
        in_y = any(ymin <= y <= ymax for y in [_ymin,_ymax]) or any(_ymin <= y <= _ymax for y in [ymin,ymax])
        in_z = any(zmin <= z <= zmax for z in [_zmin,_zmax]) or any(_zmin <= z <= _zmax for z in [zmin,zmax])

        if in_x and in_y and in_z:
            __zmin = _zmin
            __zmax = _zmax
            __xmin = _xmin
            __xmax = _xmax

            if _zmin < zmin: #bottom
                cn = ((_xmin,_xmax),(_ymin,_ymax),(_zmin,zmin-1))
                __zmin = zmin
                cubes_new.append(cn)
            if _zmax > zmax: #top
                cn = ((_xmin,_xmax),(_ymin,_ymax),(zmax+1,_zmax))
                __zmax = zmax
                cubes_new.append(cn)
            if _xmin < xmin: #left
                cn = ((_xmin,xmin-1),(_ymin,_ymax),(__zmin,__zmax))
                cubes_new.append(cn)
                __xmin = xmin 
            if _xmax > xmax: #right
                cn = ((xmax+1,_xmax),(_ymin,_ymax),(__zmin,__zmax))
                cubes_new.append(cn)
                __xmax = xmax 
            if _ymin < ymin: #back
                cn = ((__xmin,__xmax),(_ymin,ymin-1),(__zmin,__zmax))
                cubes_new.append(cn)
            if _ymax > ymax: #front
                cn = ((__xmin,__xmax),(ymax+1,_ymax),(__zmin,__zmax))
                cubes_new.append(cn)
        else:
            cubes_new.append(((_xmin,_xmax),(_ymin,_ymax),(_zmin,_zmax)))
        pass
    pass
    # if cube was "on", then add it.
    if cmd == "on":
        cubes_new.append(((xmin,xmax),(ymin,ymax),(zmin,zmax)))
    cubes = cubes_new[:]
    pass
pass
print(get_volume(cubes))



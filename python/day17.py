# data = "target area: x=20..30, y=-10..-5"
data ="target area: x=117..164, y=-140..-89"
x_area = tuple(map(int, data.split()[2].split("x=")[1].replace(",", "").split("..")))
y_area = tuple(map(int, data.split()[3].split("y=")[1].split("..")))
pass


y_max = 0
init_vals = []
for y_start in range(-500,500):
    for x_start in range(-500,500):
        x_vel = x_start
        y_vel = y_start
        x_pos = 0
        y_pos = 0
        y_pos_max = y_pos

        in_box = False
        too_far = False
        done = False
        while not done:
            x_pos += x_vel
            y_pos += y_vel
            # print(f"{x_pos=} {y_pos=}, {x_vel=} {y_vel=}")
            y_pos_max = y_pos if y_pos > y_pos_max else y_pos_max
            y_vel = y_vel - 1
            x_vel = x_vel - 1 if x_vel > 0 else 0 if x_vel == 0 else x_vel + 1

            in_box = (x_area[1] >= x_pos >= x_area[0]) and (y_area[1] >= y_pos >= y_area[0])

            too_far_x = ((x_pos < x_area[0]) and x_vel <= 0) or ((x_pos > x_area[1]) and x_vel >= 0)
            too_far_y = ((y_pos < y_area[0]) and y_vel <= 0)#  or ((y_pos > y_area[0]) and y_vel >= 0)
            too_far = too_far_y or too_far_x
            done = too_far or in_box
            # print(f"{too_far_x=} {too_far_y=}, {too_far=}")
        if in_box:
            print(f"{x_start=}, {y_start=}: {y_pos_max}")
            init_vals.append((x_start,y_start))
            if y_pos_max > y_max:
                y_max = y_pos_max


print(y_max)
print(len(init_vals))
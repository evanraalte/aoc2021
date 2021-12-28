from collections import defaultdict, Counter

program = open("assets/day24.txt").read().split('\n')



def parse_instruction(line,data, input):
    next_input = False
    splitted_line = line.split()
    if len(splitted_line) == 2:
        cmd, a = splitted_line
        b = None
    else:
        cmd, a, b = splitted_line
    try:
        data_b = int(b)
    except ValueError:
        data_b = data[b]
    except TypeError:
        pass
    match cmd:
        case "inp": 
            data[a] = input
            next_input = True
        case "add":
            data[a] = data[a] + data_b
        case "mul":
            data[a] = data[a] * data_b
        case "div":
            data[a] = data[a] // data_b
        case "mod":
            data[a] = data[a] % data_b
        case "eql":
            data[a] = int(data[a] == data_b)
    return next_input

        
nums = (str(i).zfill(14) for i in range(11111111111111,99999999999999) if '0' not in str(i).zfill(14))
x = defaultdict(lambda: [])
for num in nums:
    # num = str(13579246899999)
    inputs = list(num)
    inputs.append(0)
    idx = 0
    data = defaultdict(lambda: 0, {})
    for line in program:
        next_inp = parse_instruction(line,data,int(inputs[idx]))
        # print(data)
        if next_inp:
            idx += 1
    # print(num, " ", data['z'])
    x[data['z']].append(num)
    if data['z'] == 0:
        print(num)
        break
# print(data)
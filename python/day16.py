from numpy import prod

# data = "A0016C880162017C3686B18A3D4780"
# data = "38006F45291200"
# data = "9C0141080250320F1802104A08"

data = open("assets/day16.txt").read()
sum_versions = 0


def parse_packet(packet, pc):
    global sum_versions
    val = 0
    # print(f"remainder: {packet[pc:]}")
    try:
        version_num = int("0b" + packet[pc : pc + 3], 0)
        pc = pc + 3
        sum_versions += version_num
        # print(f"Adds {version_num}")
        op_code = int("0b" + packet[pc : pc + 3], 0)
        pc = pc + 3
        if op_code == 4:
            buf = "0b"
            done = False
            while not done:
                last_bit = packet[pc]
                pc += 1
                buf += packet[pc : pc + 4]
                pc += 4
                if last_bit == '0':
                    done = True
            val = int(buf, 0)
            print(f"Literal: {val}")
        else:
            length_id = packet[pc]
            pc = pc + 1
            vals = []
            if length_id == '1':
                num_sub_packets = int("0b" + packet[pc : pc + 11], 0)
                pc = pc + 11
                for _ in range(0, num_sub_packets):
                    pc, val = parse_packet(binary, pc)
                    vals.append(val)

            else:
                num_bits = int("0b" + packet[pc : pc + 15], 0)
                pc = pc + 15
                pc_base = pc
                done = False
                while not done:
                    pc, val = parse_packet(packet, pc)
                    vals.append(val)
                    if pc == (num_bits + pc_base):
                        done = True
            if op_code == 0:
                val = sum(vals)
            if op_code == 1:
                val = prod(vals)
            if op_code == 2:
                val = min(vals)
            if op_code == 3:
                val = max(vals)
            if op_code == 5:
                val = int(vals[0] > vals[1])
            if op_code == 6:
                val = int(vals[0] < vals[1])
            if op_code == 7:
                val = int(vals[0] == vals[1])

    except Exception:
        return pc, None
    return pc, val


binary = "".join(format(int(f"0x{d}", 0), "04b") for d in data)
pc = 0
pc_next = 0
while pc_next < len(binary):  # version + opcode +cmd minimal size
    pc = pc_next
    pc_next, val_next = parse_packet(binary, pc)
    if val_next is not None:
        val = val_next
    if pc == pc_next:
        break


print(sum_versions)
print(val)
pass

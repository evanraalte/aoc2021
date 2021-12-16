# data = "A0016C880162017C3686B18A3D4780"
# data = "38006F45291200"
# data = "D2FE28"

data = open("assets/day16.txt").read()
sum_versions = 0


def parse_packet(packet, pc):
    global sum_versions
    print(f"remainder: {packet[pc:]}")
    try:
        version_num = int("0b" + packet[pc : pc + 3], 0)
        pc = pc + 3
        sum_versions += version_num
        print(f"Adds {version_num}")
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
            num = int(buf, 0)
            print(f"Literal: {num}")
        else:
            length_id = packet[pc]
            pc = pc + 1
            if length_id == '1':
                num_sub_packets = int("0b" + packet[pc : pc + 11], 0)
                pc = pc + 11
                for _ in range(0, num_sub_packets):
                    pc = parse_packet(binary, pc)
            else:
                num_bits = int("0b" + packet[pc : pc + 15], 0)
                pc = pc + 15
                pc_base = pc
                done = False
                while not done:
                    pc = parse_packet(packet, pc)
                    if pc == (num_bits + pc_base):
                        done = True
    except Exception:
        pass
    return pc


binary = "".join(format(int(f"0x{d}", 0), "04b") for d in data)
pc = 0
pc_next = 0
while pc_next < len(binary):  # version + opcode +cmd minimal size
    pc = pc_next
    pc_next = parse_packet(binary, pc)
    if pc == pc_next:
        break


print(sum_versions)
pass

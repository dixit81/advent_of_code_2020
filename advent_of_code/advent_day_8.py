with open('advent_day_8_input.txt') as f:
    content = f.read().strip().split('\n')


def advent_day_8_part_1():
    instruction_dict = []
    global_acc = 0

    for x in content:
        instruction_dict.append([x, 0])

    i = 0
    while i < len(instruction_dict):
        operation_tuple = instruction_dict[i]

        key = operation_tuple[0]
        value = operation_tuple[1]

        if key[:3] == "nop":
            value += 1
            operation_tuple = [key, value]
            instruction_dict[i] = operation_tuple
            if value != 2:
                i += 1

        elif key[:3] == "acc":
            value += 1
            operation_tuple = [key, value]
            instruction_dict[i] = operation_tuple
            if value != 2:
                global_acc += int(key[key.index("acc ") + len("acc "):])
                i += 1

        elif key[:3] == "jmp":
            value += 1
            operation_tuple = [key, value]
            instruction_dict[i] = operation_tuple
            if value != 2:
                i += int(key[key.index("jmp ") + len("jmp "):])

        values = [x[1] for x in instruction_dict]

        if 2 in values:
            break

    print(global_acc)


def advent_day_8_part_2_helper():
    acc = 0
    line = 0
    instruction = []

    while line not in instruction:
        instruction.append(line)

        current_inst = content[line]
        current_inst = current_inst.split()
        cmd = current_inst[0]
        num = current_inst[1]
        if '+' in num:
            num = int(num[1:])
        else:
            num = int(current_inst[1])

        if cmd == "acc":
            acc += num
            line += 1
        elif cmd == 'jmp':
            line += num
        elif cmd == "nop":
            line += 1

        if line >= len(content):
            return acc, True

    return acc, False


def advent_day_8_part_2():
    for i in range(len(content)):
        if 'jmp' in content[i]:
            content[i] = content[i].replace("jmp", "nop")
            acc, found = advent_day_8_part_2_helper()

            if found:
                print(acc)
                break
            else:
                content[i] = content[i].replace("nop", "jmp")


if __name__ == '__main__':
    advent_day_8_part_2()

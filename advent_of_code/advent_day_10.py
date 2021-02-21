with open('advent_day_10_input.txt') as f:
    content_str = f.read().strip().split('\n')
    content = [int(x) for x in content_str]


def advent_day_10_part_1():
    counter_for_1 = 0
    counter_for_3 = 0

    content.insert(0, 0)
    max_adapter = max(content) + 3
    content.append(max_adapter)
    content.sort()

    for i in range(0, len(content) - 1):
        diff = content[i + 1] - content[i]

        if diff == 1:
            counter_for_1 += 1
        elif diff == 3:
            counter_for_3 += 1

    result = counter_for_1 * counter_for_3
    print("Multiplied difference is: " + str(result))
    return result


# TODO very slow, it's O(3^n) atm...
def advent_day_10_part_2(input, index):
    if index == len(input) - 1:
        return 1

    total = 0

    for i in range(index + 1, len(input)):

        if input[i] - input[index] <= 3:
            total += advent_day_10_part_2(input, i)

    return total


if __name__ == '__main__':
    # advent_day_10_part_1()
    content.insert(0, 0)
    max_adapter = max(content) + 3
    content.append(max_adapter)
    content.sort()
    print(advent_day_10_part_2(content, 0))

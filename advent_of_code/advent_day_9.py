with open('advent_day_9_input.txt') as f:
    content_str = f.read().strip().split('\n')
    content = [int(x) for x in content_str]


def advent_day_9_part_1():
    index = 0
    i = 0

    while i <= len(content):
        preamble_list = create_preamble_list(index)
        rest_of_list = [content[x] for x in range(index + 25, len(content))]

        post_preamble_value = rest_of_list[0]

        remain_value = [post_preamble_value - i for i in preamble_list]

        if any(item in remain_value for item in preamble_list):
            index += 1
            i += 1
        else:
            return post_preamble_value


def advent_day_9_part_2_helper():
    target = advent_day_9_part_1()

    for i in range(len(content)):
        addition_array = [content[i]]
        sum_arr = content[i]
        for j in range(i+1, len(content)):
            addition_array.append(content[j])
            sum_arr += content[j]

            if sum_arr > target:
                break
            elif sum_arr == target:
                print(addition_array)
                return addition_array
        sum_arr = 0


def advent_day_9_part_2():
    contiguous_list = advent_day_9_part_2_helper()

    max_value = max(contiguous_list)
    min_value = min(contiguous_list)

    if max_value == min_value:
        print("Result is 0")
        return 0

    result = max_value + min_value

    print("Result is " + str(result))
    return result


def create_preamble_list(index):
    preamble_list = []

    for i in range(index, index + 25):
        preamble_list.append(content[i])

    return preamble_list


if __name__ == '__main__':
    advent_day_9_part_2()

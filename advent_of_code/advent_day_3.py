# Move 1 down, 3 to right
def traverse_slope(content):
    index = 0
    counter = 0

    for i in range(0, len(content), 2):
        line = content[i]
        result = line[index]
        if result == '#':
            counter += 1

        index += 1

    return counter


def advent_day_3(input_file):
    with open(input_file) as f:
        content = [x.strip() for x in (f.readlines())]
        # print(content)
        final_val = traverse_slope(content)
        print('Number of trees: ' + str(final_val))


if __name__ == '__main__':
    advent_day_3('advent_day_3_input.txt')

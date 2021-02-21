import math


def floor_midpoint(param_tuple):
    a = abs(math.floor((param_tuple[1] + param_tuple[0]) / 2))
    new_tuple = (param_tuple[0], a)
    return new_tuple


def ceiling_midpoint(param_tuple):
    b = abs(math.ceil((param_tuple[1] + param_tuple[0]) / 2))
    new_tuple = (b, param_tuple[1])
    return new_tuple


def advent_day_5_part_1(file):
    row_tuple = (0, 127)
    col_tuple = (0, 7)
    # result_row = 0
    # result_col = 0
    # list_of_results = []
    row_num = []
    col_num = []
    seats_taken = []

    with open(file) as f:
        lines = f.read().split('\n')

        for locator_pattern in lines:
            locator_length = len(locator_pattern)
            for character in range(locator_length):
                direction = locator_pattern[character]

                if direction == 'F':
                    row_tuple = floor_midpoint(row_tuple)
                elif direction == 'B':
                    row_tuple = ceiling_midpoint(row_tuple)
                elif direction == 'L':
                    col_tuple = floor_midpoint(col_tuple)
                elif direction == 'R':
                    col_tuple = ceiling_midpoint(col_tuple)

            if col_tuple[0] == col_tuple[1] and row_tuple[0] == row_tuple[1]:
                result_row = row_tuple[0]
                result_col = col_tuple[0]
                seats_taken.append((result_row, result_col))

                # seat_id = result_row * 8 + result_col
                # list_of_results.append(seat_id)
                row_tuple = (0, 127)
                col_tuple = (0, 7)
            else:
                print('Unexpected!!!')

    sorted_list = sorted(seats_taken)

    for seat in sorted_list:
        row_num.append(seat[0])
        col_num.append(seat[1])

    row_set = set(row_num)
    col_set = set(col_num)
    my_seat_row = 0
    my_seat_col = 0

    for x in row_set:
        if row_num.count(x) < 8 and (1 < x < 107):
            my_seat_row = x

    for y in col_set:
        if col_num.count(y) < 106 and y != 3:
            my_seat_col = y

    my_seat_id = my_seat_row * 8 + my_seat_col
    print(my_seat_id)
    return my_seat_id

    # final_value = max(list_of_results)
    # print("Max seat id: " + str(final_value))
    # return final_value


if __name__ == '__main__':
    advent_day_5_part_1('advent_day_5_input.txt')

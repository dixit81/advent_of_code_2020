import re


# 4 inputs = lb, ub, letter, password
# 1 output = number of valid passwords
# find occurrence of letter in password

def advent_day_2_part_1_helper(lower_bound, upper_bound, letter, password):
    if lower_bound <= len(re.findall(letter, password)) <= upper_bound:
        return 1
    else:
        return 0


def advent_day_2(input_file):
    count = 0
    with open(input_file) as f:
        content = [x.strip() for x in (f.readlines())]
        for line in content:
            params = re.split('-| |: ', line)
            final_val = advent_day_2_part_2_helper(int(params[0]), int(params[1]), params[2], params[3])
            count += final_val

    print("Valid number of passwords: " + str(count))


def advent_day_2_part_2_helper(lower_position, upper_position, letter, password):
    if password[lower_position - 1] == password[upper_position - 1]:
        return 0

    if password[lower_position - 1] == letter or password[upper_position - 1] == letter:
        return 1
    else:
        return 0


if __name__ == '__main__':
    advent_day_2('advent_day_2_input.txt')

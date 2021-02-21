# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
import re


def advent_day_4_part_1(keys):
    count = 0
    needed_details = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    sneaky_details = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    key_set = set(keys)
    passport_set = set(needed_details)
    sneaky_set = set(sneaky_details)

    if key_set == passport_set:
        count += 1
    elif len(key_set) == 7 and key_set == sneaky_set:
        count += 1

    return count


def validate_passport(dictionary_values):
    possible_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    byr_check = False
    eyr_check = False
    iyr_check = False
    hgt_check = False
    hcl_check = False
    ecl_check = False
    pid_check = False

    for key, value in dictionary_values.items():
        if key == 'byr' and 1920 <= int(value) <= 2002:
            byr_check = True
        elif key == 'iyr' and 2010 <= int(value) <= 2020:
            iyr_check = True
        elif key == 'eyr' and 2020 <= int(value) <= 2030:
            eyr_check = True
        elif key == 'hgt' and re.search('\d*[cmin]', value):
            unit = value[-2:]
            int_hgt = int(value[:-2])
            if unit == 'cm' and 150 <= int_hgt <= 193:
                hgt_check = True
            elif unit == 'in' and 59 <= int_hgt <= 76:
                hgt_check = True
            else:
                hgt_check = False
        elif key == 'hcl' and re.search('#[0-9a-f]{6}', value):
            hcl_check = True
        elif key == 'ecl' and any(x in value for x in possible_eye_colors):
            ecl_check = True
        elif key == 'pid' and len(value) == 9:
            pid_check = True
        elif key == 'cid':
            pass
        else:
            return False

    if byr_check and eyr_check and iyr_check and hgt_check and hcl_check and ecl_check and pid_check:
        return True
    else:
        return False


def advent_day_4_part_2(all_values):
    dictionary_values = dict(s.split(":") for s in all_values)

    # Copying validation of part 1
    needed_details = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    sneaky_details = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    key_set = dictionary_values.keys()
    passport_set = set(needed_details)
    sneaky_set = set(sneaky_details)

    if key_set == passport_set or (len(dictionary_values) == 7 and key_set == sneaky_set):
        if validate_passport(dictionary_values):
            return 1
        else:
            return 0
    else:
        return 0


def get_input_from_file(file):
    result = 0

    with open(file) as f:
        lines = f.read().split('\n\n')
        content = [x.replace('\n', ' ') for x in lines]

    for i in range(len(content)):
        passport_detail_list = content[i].split(' ')
        # keys = [k.split(':')[0] for k in passport_detail_list]
        # values = [v.split(':')[1] for v in passport_detail_list]
        # result += advent_day_4_part_2(keys, values)
        result += advent_day_4_part_2(passport_detail_list)
        # advent_day_4_part_2(passport_detail_list)

    return result


if __name__ == '__main__':
    print("Valid passports: " + str(get_input_from_file('advent_day_4_input.txt')))

def determine_total_for_anyone(groups):
    number_of_questions = 0
    total = 0
    set_of_questions = set()

    for i in groups:
        for j in i:
            refined_group = j.split('\n')

            if len(refined_group) == 1:
                number_of_questions = len(j)
            else:
                no_newline_string_input = j.replace('\n', "")
                for k in no_newline_string_input:
                    set_of_questions.add(k)
                number_of_questions = len(set_of_questions)
                set_of_questions.clear()

        total += number_of_questions

    return total


def determine_total_for_everyone(groups):
    total = 0
    occurance_dict = {}
    letters = set()

    for i in groups:
        for j in i:
            refined_group = j.split('\n')
            if refined_group.__contains__(''):
                refined_group.remove('')
            no_newline_string_input = j.replace("\n", "")
            for k in no_newline_string_input:
                letters.add(k)
                letter_in_question = letters.pop()
                number_of_occurances = no_newline_string_input.count(letter_in_question)
                occurance_dict[letter_in_question] = number_of_occurances

            dict_values = occurance_dict.values()
            for values in dict_values:
                if values == len(refined_group):
                    total += 1
                else:
                    total += 0
            occurance_dict.clear()

    return total


def advent_day_6(file):
    groups = []
    singular_group = []

    with open(file) as f:
        lines = f.read().split('\n\n')
        for i in lines:
            count = 0
            singular_group.append(i)
            groups.insert(count, singular_group)
            singular_group = []
            count += 1
        groups.reverse()

    print('Total number of questions are: ' + str(determine_total_for_everyone(groups)))


if __name__ == '__main__':
    advent_day_6('advent_day_6_input.txt')

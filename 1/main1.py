import re

data = []
total_part1 = 0
total_part2 = 0
letter_numbers = {'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}


def gather_input():
    file = open("1_data.txt", "r")
    for line in file:
        data.append(line.lower())


def get_answer_part1(part1_input):
    m = re.search("(\\d)(.*)(\\d)", part1_input)
    if m is not None:
        value = int(m.groups()[0] + m.groups()[2])
    else:
        f = re.search("(\\d)", part1_input)
        value = int(f.group() + f.group())
    return value


def get_answer_part2(part2_input):
    input_copy = part2_input
    for letter_number in letter_numbers:
        input_copy = input_copy.replace(letter_number, letter_numbers.get(letter_number))
    return get_answer_part1(input_copy)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gather_input()
    for row in data:
        total_part1 += get_answer_part1(row)
        total_part2 += get_answer_part2(row)
    print(total_part1, total_part2)
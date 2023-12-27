import re

data = []
total_part1 = 0
total_part2 = 0
num_list = []
char_list = []


def gather_input():
    file = open("3_data.txt", "r")
    for line in file:
        data.append(line.lower())


def get_answer_part1():
    for char in char_list:
        nums_we_give_a_shit_about = list(filter(lambda number: char['line'] - 1 <= number['coords']['line'] <= char['line'] + 1, num_list))
        for idx, num in enumerate(nums_we_give_a_shit_about):
            if char['column'] - 1 <= num['coords']['column'] <= char['column'] + 1:
                num['enabled'] = True
    print('sup')


def build_data(row_number):
    num_match = re.findall("(\\d+)", row)
    if num_match is not None:
        for group in num_match:
            index = row.find(group)
            columns = []
            col = index
            while col < index + len(group):
                columns.append(col)
                col += 1
            num_list.append({'value': group, 'coords': {'line': row_number, 'column': columns}, 'enabled': False})
    char_match = re.finditer("[^A-Za-z0-9.\n\r]", row)
    if char_match is not None:
        for char_idx, match in enumerate(char_match):
            char_list.append({'line': row_number, 'column': match.regs[0][0]})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gather_input()
for idx, row in enumerate(data):
    build_data(idx)
total_part1 += get_answer_part1()
# total_part2 += get_answer_part2(row)
print(total_part1, total_part2)

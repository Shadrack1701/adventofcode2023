import re

data = []
total_part1 = 0
total_part2 = 0
char_list = []
num_list = []


def gather_input():
    file = open("3_data.txt", "r")
    for line in file:
        data.append(line.lower())


def get_answer_part1():
    global total_part1
    for char in char_list:
        nums_we_give_a_shit_about = list(filter(lambda number: char['line'] - 1 <= number['coords']['line'] <= char['line'] + 1, num_list))
        for num in nums_we_give_a_shit_about:
            for n in num['coords']['column']:
                if char['column'] - 1 <= n <= char['column'] + 1:
                    num['enabled'] = True
    for num in num_list:
        if num['enabled']:
            total_part1 += num['value']


def get_answer_part2():
    global total_part2
    gears = list(filter(lambda char_instance: char_instance['value'] == '*', char_list))
    for char in gears:
        gear_numbers = []
        nums_we_give_a_shit_about = list(filter(lambda number: char['line'] - 1 <= number['coords']['line'] <= char['line'] + 1, num_list))
        for num in nums_we_give_a_shit_about:
            for n in num['coords']['column']:
                if char['column'] - 1 <= n <= char['column'] + 1:
                    if not gear_numbers.__contains__(num):
                        gear_numbers.append(num)
        if len(gear_numbers) == 2:
            total_part2 += (int(gear_numbers[0]['value']) * int(gear_numbers[1]['value']))


def build_data(row_number):
    columns = []
    num_boi = ''
    for row_index, char in enumerate(row):
        if char == '.' or char == '\n':
            if num_boi:
                num_list.append({'value': int(num_boi), 'coords': {'line': row_number, 'column': columns.copy()}, 'enabled': False})
                num_boi = ''
                columns.clear()
            continue
        if char.isnumeric():
            num_boi += char
            columns.append(row_index)
        else:
            char_list.append({'value': char, 'line': row_number, 'column': row_index})
            if num_boi:
                num_list.append({'value': int(num_boi), 'coords': {'line': row_number, 'column': columns.copy()}, 'enabled': False})
                num_boi = ''
                columns.clear()
    if num_boi:
        num_list.append({'value': int(num_boi), 'coords': {'line': row_number, 'column': columns.copy()}, 'enabled': False})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gather_input()
for idx, row in enumerate(data):
    build_data(idx)
get_answer_part1()
get_answer_part2()
print(total_part1, total_part2)

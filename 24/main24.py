import shapely
from shapely.geometry import LineString, Point

data = []
total_part1 = 0
total_part2 = 0
hail_list = []
box_min = 200000000000000
box_max = 400000000000000


def gather_input():
    file = open("24_data.txt", "r")
    for line in file:
        data.append(line.lower())


def get_answer_part1():
    global total_part1
    pos = 0
    index = 1
    length = len(hail_list)
    while True:
        if pos >= length - 1:
            break
        line1 = LineString([hail_list[pos]['start'], hail_list[pos]['end']])
        line2 = LineString([hail_list[index]['start'], hail_list[index]['end']])

        int_pt = line1.intersection(line2)
        if len(int_pt.xy[0]) > 0:
            point_of_intersection = [int_pt.xy[0][0], int_pt.xy[1][0]]
            if box_min <= point_of_intersection[0] <= box_max and box_min <= point_of_intersection[1] <= box_max:
                total_part1 += 1
        if index < length - 1:
            index += 1
        else:
            pos += 1
            index = pos + 1


def get_answer_part2():


def build_data():
    split_data = row.split('@')
    raw_coords = split_data[0].split(',')
    raw_speeds = split_data[1].split(',')
    coords = []
    speeds = []
    for raw_coord in raw_coords:
        coords.append(int(raw_coord))
    for raw_speed in raw_speeds:
        speeds.append(int(raw_speed))
    hail_list.append({'start': coords, 'speeds': speeds, 'end': []})


def simulate_to_boundary():
    for hail in hail_list:
        hail['end'] = [hail['start'][0] + hail['speeds'][0] * box_min, hail['start'][1] + hail['speeds'][1] * box_min,
                       hail['start'][2] + hail['speeds'][2] * box_min]


if __name__ == '__main__':
    gather_input()
for row in data:
    build_data()
simulate_to_boundary()
get_answer_part1()
# get_answer_part2()
print(total_part1, total_part2)

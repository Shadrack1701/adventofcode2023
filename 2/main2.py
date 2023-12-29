import re
from Games import Games

data = []
red = 12
green = 13
blue = 14
total_part1 = 0
total_part2 = 0


def gather_input():
    file = open("2_data.txt", "r")
    for line in file:
        data.append(line.lower())


def get_answer_part1():
    global total_part1
    for game_id in games.games_dict.keys():
        game_possible = True
        for game in games.games_dict[game_id]:
            if game.red > red or game.green > green or game.blue > blue:
                game_possible = False
        if game_possible:
            total_part1 += game_id


def get_answer_part2():
    global total_part2
    for game_id in games.games_maxs.keys():
        total_part2 += games.games_maxs[game_id].power


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gather_input()
    games = Games()
    for row in data:
        games.add_game(row)
    get_answer_part1()
    get_answer_part2()
    print(total_part1, total_part2)

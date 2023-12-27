import re


class Game:
    red = 0
    green = 0
    blue = 0

    def __init__(self, game_string):
        red_match = re.search("(\\d+)( red)", game_string)
        if red_match is not None:
            self.red = int(red_match.group(1))
        green_match = re.search("(\\d+)( green)", game_string)
        if green_match is not None:
            self.green = int(green_match.group(1))
        blue_match = re.search("(\\d+)( blue)", game_string)
        if blue_match is not None:
            self.blue = int(blue_match.group(1))


class GameMaxs:
    max_red = 0
    max_green = 0
    max_blue = 0
    power = 0

    def __init__(self, max_red, max_green, max_blue):
        self.max_red = max_red
        self.max_green = max_green
        self.max_blue = max_blue
        self.power = max_red * max_green * max_blue


class Games:
    games_dict = dict()
    games_maxs = dict()

    def add_game(self, game_string):
        game_id = 0
        id_match = re.search("(game )(\\d+):", game_string)
        if id_match is not None:
            game_id = int(id_match.group(2))
        game_string = game_string.split(':')[1]
        game_string = game_string.split(';')
        games = []
        for game in game_string:
            games.append(Game(game))

        max_red = 0
        max_green = 0
        max_blue = 0
        for game in games:
            if 0 < game.red > max_red:
                max_red = game.red
            if 0 < game.blue > max_blue:
                max_blue = game.blue
            if 0 < game.green > max_green:
                max_green = game.green

        self.games_dict.update({game_id: games})
        self.games_maxs.update({game_id: GameMaxs(max_red, max_green, max_blue)})

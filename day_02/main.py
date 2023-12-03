import dataclasses
from typing import Literal


@dataclasses.dataclass
class NumColorPair:
    color: Literal["r", "g", "b"] 
    num: int

def part1() -> None: 
    with open("input.txt", "r") as f:
        games = f.read().split("\n")
    game_id_sum: int = 0
    for idx, game in enumerate(games):
    
        parsed_game, game_id = parse_game(game)
        if is_possible(parsed_game, r=12, g=13, b=14):
            game_id_sum = game_id_sum + game_id 
    print(game_id_sum)

def part2():
    with open("input.txt", "r") as f:
        games = f.read().split("\n")
    power_sum: int = 0
    for game in games:

        parsed_game, game_id = parse_game(game)
        min_power = get_min(parsed_game)
        power_sum = power_sum + min_power
    print(power_sum)

def get_digit(in_str: str) -> int:
    digit: str = ""
    for char in in_str:
        if char.isdigit():
            digit = digit + char
    if digit == "":
        raise RuntimeError(f"No digit could be found in the input string: {in_str}")
    return int(digit) 

def get_min(game: list[list[NumColorPair]]) -> int:
    red_array: list[int] = []
    green_array: list[int] = []
    blue_array: list[int] = []
    for game_set in game:
        for num_color_pair in game_set:
            if num_color_pair.color == "r":
                red_array.append(num_color_pair.num)
            if num_color_pair.color == "g":
                green_array.append(num_color_pair.num)
            if num_color_pair.color == "b":
                blue_array.append(num_color_pair.num)
    
    red_max = max(red_array)
    green_max = max(green_array)
    blue_max = max(blue_array)
    return red_max * green_max * blue_max

def is_possible(game: list[list[NumColorPair]], r: int, g: int, b: int) -> bool:
    for game_set in game:
        for num_color_pair in game_set:
            if num_color_pair.color == "r":
                if num_color_pair.num > r:
                    return False
            if num_color_pair.color == "g":
                if num_color_pair.num > g:
                    return False
            if num_color_pair.color == "b":
                if num_color_pair.num > b:
                    return False
    return True


def parse_game(game: str) -> list[list[NumColorPair]]:
    parsed_game_set: list[NumColorPair] = []
    parsed_game: list = []
    game_id = get_digit(game.split(":")[0])
    game = game.split(":")[1]
    game_sets = game.split(";")
    digit: int = 0
    for game_set in game_sets:
        num_color_pairs = game_set.split(",")
        for num_color_pair in num_color_pairs:
            digit = get_digit(num_color_pair)         
            if "blue" in num_color_pair:
                parsed_game_set.append(NumColorPair(num=digit, color="b"))
            if "red" in num_color_pair:
                parsed_game_set.append(NumColorPair(num=digit, color="r"))
            if "green" in num_color_pair:
                parsed_game_set.append(NumColorPair(num=digit, color="g"))

        parsed_game.append(parsed_game_set.copy())
        parsed_game_set.clear()
    return parsed_game, game_id

        
if __name__ == "__main__":
    part2()
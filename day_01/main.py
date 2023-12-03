digit_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def is_int(value: str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False

def main():
    int_value: int = 0
    with open("input.txt", "r") as f:
        lines = f.read().split("\n")
    for line in lines:
        int_value = int_value + int(
            get_value_left(line) + get_value_right(line))
    print(f"final value {int_value}")

def get_value_left(line: str) -> str:
    left_value: str = "0"
    char_snake_left: str = ""
    for char in line:
        char_snake_left = char_snake_left + char
        for digit_str in digit_map.keys():
            if digit_str in char_snake_left:
                left_value = str(digit_map[digit_str])
                return left_value
        if is_int(char):
            left_value = char
            return left_value 
    return left_value

def get_value_right(line: str) -> str:
    right_value: str = "0"
    char_snake_right: str = ""
    for char in line[::-1]:
        char_snake_right = char + char_snake_right
        for digit_str in digit_map.keys():
            if digit_str in char_snake_right:
                right_value = str(digit_map[digit_str])
                return right_value
        if is_int(char):
            right_value = char
            return right_value 
    return right_value

if __name__ == "__main__":
    main()
from contextlib import suppress
from dataclasses import dataclass
from typing import Union, Generator


def part1() -> None:
    with open("input.txt", "r") as f: 
        content = f.read().split("\n")
    solution: int = 0 
    neighbor: bool = False            
    for idx_row, row in enumerate(content):    
        num: str = ""
        for idx_char, char in enumerate(row):
            if char.isdigit():
                num = num + char
                if neighbor is False:
                    neighbor = has_neighbor(content, row=idx_row, column=idx_char)  

            if is_end_list(content, idx_char):
                if not neighbor:
                    print(f"num with no n: {num}")
                    num = ""
                    neighbor = False
                else:
                    solution = solution + int(num) 
                    num = ""
                    neighbor = False
            else:
                if num != "" and not char.isdigit():
                    if not neighbor:
                        print(f"num with no n: {num}")
                        num = ""
                        neighbor = False
                    else:
                        solution = solution + int(num) 
                        num = ""
                        neighbor = False
    print(solution)


def part2() -> None:
    with open("test_input.txt", "r") as f: 
        content = f.read().split("\n")
    two_nums: list[int] = []
    idx_list: list[int] = []
    for idx_row, row in enumerate(content):
        for idx_char, char in enumerate(row):
            if char == "*":
                should_have_two_n: int = 0
                idx_list.clear()
                for row, column in has_neighbor(content, idx_row, idx_char, neighbor_is_num=True): 
                    if should_have_two_n == 2:
                        break
                    if row is None:
                        continue
                    all_nums = store_all_numbers(content)
                    num, idx = get_num_by_cor(all_nums, row, column)
                    if idx not in idx_list:
                        two_nums.append(num)
                        should_have_two_n = should_have_two_n + 1
                        idx_list.append(idx)  
                else:
                    if len(idx_list) != 2:
                        two_nums.pop()
                        should_have_two_n = 0
                    continue
    list_of_gear_ratios: list[int] = []
    for i in range(0, len(two_nums) - 1, 2):
        product = int(two_nums[i]) * int(two_nums[i + 1])
        list_of_gear_ratios.append(product)
    result: int = 0
    for gear_ratio in list_of_gear_ratios:
        result = result + gear_ratio
    print(result)

@dataclass
class NumAndCor:
    num: str
    cor: list[tuple]

def store_all_numbers(content: list[str]) -> list[NumAndCor]:
    cor: list[tuple] = []
    cor_list: list[NumAndCor] = []
    num: str = ""
    for idx_row, row in enumerate(content):
        for idx_char, char in enumerate(row):
            if char.isdigit():
                num = num + char
                cor_char = (idx_row, idx_char)  
                cor.append(cor_char)
            if is_end_list(content, idx_char):
                if num != "" and not char.isdigit():
                    cor_list.append(NumAndCor(num=num, cor=cor.copy()))
                    num = ""
                    cor.clear()
            else:       
                if num != "" and not char.isdigit():
                    cor_list.append(NumAndCor(num=num, cor=cor.copy()))
                    num = ""
                    cor.clear()
    return cor_list

def get_num_by_cor(nums: list[NumAndCor], row: int, column: int) -> tuple[int, int]:
    for idx, num in enumerate(nums):
        for cor in num.cor:
            if cor[0] == row and cor[1] == column:
                return (num.num, idx) 
    raise RuntimeError(f"Could not find the number under cor {row},{column}")

def is_end_list(content: list, index: int) -> bool:
    try:
        content[index + 1]
        return False
    except IndexError:
        return True

def has_neighbor(content: list[str], row: int, column: int, neighbor_is_num: bool = False) -> Union[bool, Generator[int, int, None]]:
    """checks if there are any neighbor symbols that are not '.' or a digit.
    If neighbor_is_num is set to true, then it just checks if its an int and yields the field.
    """

    if str(column - 1)[0]!='-': 
        char = content[row][column - 1] #left
        if neighbor_is_num:
            if char.isdigit():
                yield (row, column - 1)
            else:
                yield (None, None) 
        else:
            if char != "." and not char.isdigit():
                return True
    with suppress(IndexError): # if index error occurs, that means we reached either the last row or last column -> no neighbors
        char = content[row][column + 1] #right
        if neighbor_is_num:
            if char.isdigit():
                yield (row, column + 1)
            else:
                yield (None, None) 
        else:
            if char != "." and not char.isdigit():
                return True
    with suppress(IndexError):
        char = content[row + 1][column] #down
        if neighbor_is_num:
            if char.isdigit():
                yield (row + 1, column)
            else:
                yield (None, None)
        else:
            if char != "." and not char.isdigit():
                return True
    if str(row - 1)[0]!='-':
        char = content[row - 1][column] #up
        if neighbor_is_num:
            if char.isdigit():
                yield (row - 1, column)
            else:
                yield (None, None)
        else:
            if char != "." and not char.isdigit():
                return True
    with suppress(IndexError):  #down,left
        if str(column - 1)[0]!='-':
            char = content[row + 1][column - 1]
            if neighbor_is_num:
                if char.isdigit():
                    yield (row + 1, column - 1)
                else:
                    yield (None, None) 
            else:
                if char != "." and not char.isdigit():
                    return True
    with suppress(IndexError):
        char = content[row + 1][column + 1] #downright
        if neighbor_is_num:
            if char.isdigit():
                yield (row + 1, column + 1)
            else:
                yield (None, None) 
        else:
            if char != "." and not char.isdigit():
                return True
    if str(column - 1)[0]!='-':
        if str(row - 1)[0]!='-':
            char = content[row - 1][column - 1] #up,left
            if neighbor_is_num:
                if char.isdigit():
                    yield (row - 1, column -1)
                else:
                    yield (None, None)
            else:
                if char != "." and not char.isdigit():
                    return True
    with suppress(IndexError):
        if str(row - 1)[0]!='-':
            char = content[row - 1][column + 1] #up,right
            if neighbor_is_num:
                if char.isdigit():
                    yield (row - 1, column + 1)
                else:
                    yield (None, None) 
            else:
                if char != "." and not char.isdigit():
                    return True
    return False

if __name__ == "__main__":
    part2()
        
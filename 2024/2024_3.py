
import re


def get_input_string(file) -> str:
    program_string = ""
    with open(file, 'r') as f:
        while line := f.readline():
            program_string = program_string + line

    return program_string


def get_output(input: str) -> int:
    sum = 0
    lst = re.findall("mul\\((\\d{1,3}),(\\d{1,3})\\)", input)
    for input in lst:
        mul = int(input[0]) * int(input[1])
        sum = sum + mul
    return sum


input = get_input_string("./inputs/2024_3")

print(get_output(input))

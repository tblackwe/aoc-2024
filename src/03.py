from utils.api import get_input
import re

input_str = get_input(3)

# WRITE YOUR SOLUTION HERE

def process_commands(commands):
    result = 0
    for command in commands:
        multiples = re.findall("\d+", command)
        result += int(multiples[0]) * int(multiples[1])
    return result

# Part 1
valid_commands = re.findall("mul\(\d+,\d+\)", input_str)
result = process_commands(valid_commands)
print(f"Day 3 Part 1: {result}")

# Part 2
result = 0
do_commands = input_str.split("do()")
for do_command in do_commands:
    commands = do_command.split("don't()")
    valid_commands = re.findall("mul\(\d+,\d+\)", commands[0])
    result += process_commands(valid_commands)

print(f"Day 3 Part 2: {result}")

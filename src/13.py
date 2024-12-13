from utils.api import get_input, load_sample
import re

input_str = get_input(13)
test_data = load_sample(13)

# WRITE YOUR SOLUTION HERE

def arrange_input(input_str):
    input = [{}]
    input_lines = input_str.splitlines()
    button_re = "Button\s(\w):\sX\+(\d+),\sY\+(\d+)"
    prize_re = "Prize:\sX=(\d+),\sY=(\d+)"
    for line in input_lines:
        if re.search(button_re,line):
            groups = re.match(button_re,line)
            input[-1]['Button_'+groups[1]] = {}
            input[-1]['Button_'+groups[1]]['X'] = int(groups[2])
            input[-1]['Button_'+groups[1]]['Y'] = int(groups[3])
        elif re.search(prize_re,line):
            groups = re.match(prize_re,line)
            input[-1]['Prize'] = {}
            input[-1]['Prize']['X'] = int(groups[1])
            input[-1]['Prize']['Y'] = int(groups[2])
        else:
            input.append({})
    return input

# Part 1

def solution_1(input_str):
    possible_prizes = []
    for input in arrange_input(input_str):
        possible_prize = []
        for A in range(100):
            for B in range(100):
                claw_X = (input['Button_A']['X'] * A) + (input['Button_B']['X'] * B)
                claw_Y = (input['Button_A']['Y'] * A) + (input['Button_B']['Y'] * B)   
                if (claw_X == input['Prize']['X'] and claw_Y == input['Prize']['Y']):
                    possible_prize.append(((A)*3) + B)
        if possible_prize: possible_prizes.append(min(possible_prize))
    return sum(possible_prizes)
                
            

print(f"Day 13 Test 1: {solution_1(test_data)}")
print(f"Day 13 Test 1: {solution_1(input_str)}")

# Part 2

print(f"Day 13 Part 2:")
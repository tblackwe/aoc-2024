from utils.api import get_input, load_sample
import numpy as np

input_str = get_input(10)
test_data = load_sample(10)

# WRITE YOUR SOLUTION HERE


def arrange_data(input):
    input_rows = input.splitlines()
    temp = []
    for row in input_rows:
        temp.append(list(row))
    matrix = np.array(temp)
    return matrix


up = [-1, 0]
down = [1, 0]
left = [0, -1]
right = [0, 1]

def lookaround(coord, map, next_level):
    next_coords = []
    up_coord = coord+up
    down_coord = coord+down
    right_coord = coord+right
    left_coord = coord+left
    if up_coord[0] >= 0 and up_coord[1] >= 0 and up_coord[0] < map.shape[0] and up_coord[0] < map.shape[0] and up_coord[1] < map.shape[1] and map[up_coord[0], up_coord[1]] == str(next_level):
        next_coords.append(up_coord)
    if down_coord[0] >= 0 and down_coord[1] >= 0 and down_coord[0] < map.shape[0] and down_coord[0] < map.shape[0] and down_coord[1] < map.shape[1] and map[down_coord[0], down_coord[1]] == str(next_level):
        next_coords.append(down_coord)
    if right_coord[0] >= 0 and right_coord[1] >= 0 and right_coord[0] < map.shape[0] and right_coord[0] < map.shape[0] and right_coord[1] < map.shape[1] and map[right_coord[0], right_coord[1]] == str(next_level):
        next_coords.append(right_coord)
    if left_coord[0] >= 0 and left_coord[1] >= 0 and left_coord[0] < map.shape[0] and left_coord[0] < map.shape[0] and left_coord[1] < map.shape[1] and map[left_coord[0], left_coord[1]] == str(next_level):
        next_coords.append(left_coord)
    return next_coords

def get_ascents(coord, map, height=0):
    next_level = height + 1
    next_levels = lookaround(coord, map, next_level)
    valid_ascents = []
    if next_level >= 9 and next_levels:
        return [np.array2string(x) for x in next_levels]
    for next_coord in next_levels:
        valid_ascents+= get_ascents(next_coord, map, next_level)
    return valid_ascents
# Part 1


def solution_1(input):
    map = arrange_data(input)
    scores = []
    trailheads = np.argwhere(map == '0')
    for trailhead in trailheads:
        ascents = set(get_ascents(trailhead, map))
        scores.append(len(ascents))

    return sum(scores)

def solution_2(input):
    map = arrange_data(input)
    scores = []
    trailheads = np.argwhere(map == '0')
    for trailhead in trailheads:
        ascents = get_ascents(trailhead, map)
        scores.append(len(ascents))

    return sum(scores)

print(f"Day 10 Test 1: {solution_1(test_data)}")
print(f"Day 10 Part 1: {solution_1(input_str)}")

# Part 2
print(f"Day 10 Test 2: {solution_2(test_data)}")
print(f"Day 10 Part 2: {solution_2(input_str)}")

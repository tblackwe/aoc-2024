from utils.api import get_input, load_sample
import numpy as np
import string

input_str = get_input(8)
test_data = load_sample(8)

# WRITE YOUR SOLUTION HERE


def arrange_data(input):
    input_rows = input.splitlines()
    temp = []
    for row in input_rows:
        temp.append(list(row))
    matrix = np.array(temp)
    return matrix


def find_antennas(matrix):
    antennas = {}

    for letter in string.ascii_letters:
        tmp = np.argwhere(matrix == letter)
        if tmp.size > 0:
            antennas[letter] = tmp
    for number in range(10):
        tmp = np.argwhere(matrix == str(number))
        if tmp.size > 0:
            antennas[str(number)] = tmp
    return antennas


def is_between(value, lower, upper):
    return lower <= value < upper


def solution_1(input):
    matrix = arrange_data(input)
    antennas = find_antennas(matrix)
    antinodes = set()

    for frequency in antennas:
        sub_list = list(antennas[frequency])
        for antenna in antennas[frequency]:
            sub_list.pop(0)
            for paired_antenna in sub_list:
                antinode_diff = paired_antenna - antenna
                antinode_1 = antenna - antinode_diff
                antinode_2 = paired_antenna + antinode_diff
                if (is_between(antinode_1[0], 0, matrix.shape[0]) and is_between(antinode_1[1], 0, matrix.shape[1])):
                    antinodes.add(np.array2string(antinode_1))
                if (is_between(antinode_2[0], 0, matrix.shape[0]) and is_between(antinode_2[1], 0, matrix.shape[1])):
                    antinodes.add(np.array2string(antinode_2))
    return len(antinodes)


def solution_2(input):
    matrix = arrange_data(input)
    antennas = find_antennas(matrix)
    antinodes = set()

    for frequency in antennas:
        sub_list = list(antennas[frequency])
        for antenna in antennas[frequency]:
            antinodes.add(np.array2string(antenna))
            sub_list.pop(0)
            for paired_antenna in sub_list:
                antinode_diff = paired_antenna - antenna
                antinode = antenna - antinode_diff
                while is_between(antinode[0], 0, matrix.shape[0]) and is_between(antinode[1], 0, matrix.shape[1]):
                    antinodes.add(np.array2string(antinode))
                    antinode = antinode - antinode_diff
                antinode = antenna + antinode_diff
                while is_between(antinode[0], 0, matrix.shape[0]) and is_between(antinode[1], 0, matrix.shape[1]):
                    antinodes.add(np.array2string(antinode))
                    antinode = antinode + antinode_diff
    return len(antinodes)


# Part 1
print(f"Day 8 Test 1: {solution_1(test_data)}")
print(f"Day 8 Part 1: {solution_1(input_str)}")

# Part 2
print(f"Day 8 Test 2: {solution_2(test_data)}")
print(f"Day 8 Part 2: {solution_2(input_str)}")

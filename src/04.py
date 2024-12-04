from utils.api import get_input
import numpy as np

input_str = get_input(4)

# WRITE YOUR SOLUTION HERE

# Arrange the input data
input_rows = input_str.splitlines()
temp = []
for row in input_rows:
    temp.append(list(row))
matrix = np.array(temp)

# Part 1


def xmas_count(row):
    joined = ''.join(row)
    return joined.count('XMAS') + joined.count('SAMX')


# Arrange rows to check
to_check = []
found_count = 0
rot_matrix = np.rot90(matrix)
for row in matrix:
    to_check.append(row)
for row in np.rot90(matrix):
    to_check.append(row)
for i in range(len(matrix)):
    to_check.append(np.diag(matrix, k=i))
    if i != 0:
        to_check.append(np.diag(matrix, k=-i))
for i in range(len(rot_matrix)):
    to_check.append(np.diag(rot_matrix, k=i))
    if i != 0:
        to_check.append(np.diag(rot_matrix, k=-i))
for row in to_check:
    found_count += xmas_count(row)

print(f"Day 4 Part 1: {found_count}")

# Part 2


def check_for_x_mas(matrix, coord):
    if (coord[0] > 0 and coord[0] < matrix.shape[0]-1 and coord[1] > 0 and coord[1] < matrix.shape[1]-1):
        top_left = matrix[coord[0]-1][coord[1]-1]
        top_right = matrix[coord[0]-1][coord[1]+1]
        bottom_left = matrix[coord[0]+1][coord[1]-1]
        bottom_right = matrix[coord[0]+1][coord[1]+1]
        top_mas = (top_left == 'M' and bottom_right == 'S') or (
            top_left == 'S' and bottom_right == 'M')
        bottom_mas = (bottom_left == 'M' and top_right == 'S') or (
            bottom_left == 'S' and top_right == 'M')
        return top_mas and bottom_mas
    else:
        return False


found_count = 0
a_locations = np.argwhere(matrix == 'A')

for coord in a_locations:
    if check_for_x_mas(matrix, coord):
        found_count += 1

print(f"Day 4 Part 2: {found_count}")

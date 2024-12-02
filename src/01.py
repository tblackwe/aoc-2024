from utils.api import get_input
import numpy as np


input_str = get_input(1)

# WRITE YOUR SOLUTION HERE

temp_left = []
temp_right = []

for line in input_str.split("\n"):
    parts = line.split()
    temp_left.append(int(parts[0]))
    temp_right.append(int(parts[1]))

left_list = np.array(temp_left)
right_list = np.array(temp_right)

left_list.sort()
right_list.sort()

# Part 1
total_distance = 0
for idx, x in enumerate(left_list):
    total_distance += abs(x-right_list[idx])

print(f"Day 1 Part 1: {total_distance}")

# Part 2
unique, counts = np.unique(right_list, return_counts=True)
count_dict = dict(zip(unique, counts))

similarity_score = 0

for num in left_list:
    if num in count_dict:
        similarity_score += num * count_dict[num]

print(f"Day 1 Part 2: {similarity_score}")
from utils.api import get_input, load_sample

input_str = get_input(9)
test_data = load_sample(9)

# WRITE YOUR SOLUTION HERE


def arrange_input(input):
    filesystem = list(input)
    files = []
    freespace = []
    working_list = []
    for idx, char in enumerate(filesystem):
        if idx % 2 == 0:
            files.append(char)
        else:
            freespace.append(char)
    freespace.append('0')  # normalize length of freespace array
    for idx, file in enumerate(files):
        for i in range(int(file)):
            working_list.append(idx)
        for i in range(int(freespace[idx])):
            working_list.append('.')
    return working_list

# Part 1


def solution_1(input):
    working_list = arrange_input(input)
    final_result = []
    while working_list:
        element = working_list.pop(0)
        while (element == '.'):
            if not working_list:
                break
            element = working_list.pop()
        if element != '.':
            final_result.append(element)
    answer = 0
    for idx, file in enumerate(final_result):
        answer += idx * int(file)
    return answer


def solution_2(input):
    working_list = arrange_input(input)
    working_string = "".join(str(x) for x in working_list)

    while working_list:
        if working_list[-1] == '.':
            working_list.pop() # remove trailing 'free space'
        if all(i == working_list[0] for i in working_list):
            break # down to the 1 file left
        file = [working_list.pop()]
        while working_list[-1] == file[0]:
            file.append(working_list.pop())
        file_string = "".join(str(x) for x in file)
        to_search = []
        for _ in range(len(file_string)):
            to_search.append('.')
        to_search = "".join(to_search)
        file_start_index = len(working_list)
        free_space_index = working_string.find(to_search)
        if free_space_index != -1 and free_space_index < file_start_index:
            working_string = working_string.replace(file_string, to_search, 1)
            working_string = working_string.replace(to_search, file_string, 1)

    answer = 0
    for idx, file in enumerate(working_string):
        if file != '.':
            answer += idx * int(file)
    return answer


print(f"Day 9 Test 1: {solution_1(test_data)}")
print(f"Day 9 Part 1: {solution_1(input_str)}")

# Part 2

print(f"Day 9 Test 2: {solution_2(test_data)}")  # Correct answer
print(f"Day 9 Test 2: {solution_2(input_str)}")  # Wrong answer

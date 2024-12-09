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
            
    checksum = 0
    for idx, file in enumerate(final_result):
        checksum += idx * int(file)
    return checksum


def solution_2(input):
    filesystem = arrange_input(input)
    working_list = filesystem.copy()
    free_space_tracker = "".join(["X" if isinstance(item, (int)) else item for item in filesystem])
    # print(filesystem)
    while working_list:
        # remove trailing 'free space' leftover from previous loop
        if working_list[-1] == '.':
            working_list.pop() 
        
        # if there is only 1 thing left in the working list, break the loop
        if all(i == working_list[0] for i in working_list):
            break

        # pop off the highest file number
        file = [working_list.pop()]
        while working_list[-1] == file[0]:
            file.append(working_list.pop()) 
        file_string = "".join('X' for x in file)
        
        # build a string of `.` same length as file
        to_search = [] 
        for _ in range(len(file)):
            to_search.append('.')
        to_search = "".join(to_search)

        # figure out the indices of everything
        file_start_index = len(working_list) 
        free_space_index = free_space_tracker.find(to_search)

        # if there is enough freespace before the file, move it 
        if free_space_index != -1 and free_space_index < file_start_index:
            free_space_tracker = free_space_tracker.replace(to_search, file_string, 1)
            for idx,x in enumerate(file):
                filesystem[free_space_index+idx] = x
                filesystem[file_start_index+idx] = '.'

    checksum = 0
    for idx, file in enumerate(filesystem):
        if file != '.':
            checksum += idx * int(file)
    return checksum


print(f"Day 9 Test 1: {solution_1(test_data)}")
print(f"Day 9 Part 1: {solution_1(input_str)}")

# Part 2

print(f"Day 9 Test 2: {solution_2(test_data)}")  # Correct answer
print(f"Day 9 Test 2: {solution_2(input_str)}")  # Wrong answer

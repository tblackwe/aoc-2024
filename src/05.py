from utils.api import get_input, load_sample

input_str = get_input(5)
test_data = load_sample(5)

# WRITE YOUR SOLUTION HERE

def arrange(input_str):
    input = {}
    input['rules'] = {}
    input['print_orders'] = []
    input_rows = input_str.splitlines()

    for row in input_rows:
        if "|" in row:
            rule = row.split("|")
            if rule[0] not in input['rules']:
                input['rules'][rule[0]] = []
            input['rules'][rule[0]].append(rule[1])
        elif "," in row:
            input['print_orders'].append(row.split(","))
    

    return input

def findMiddle(input_list):
        middle = float(len(input_list))/2
        if middle % 2 != 0:
            return input_list[int(middle - .5)]
        else:
            return (input_list[int(middle)], input_list[int(middle-1)])
# Part 1

def solution_1(input_str):

    def check_left(idx, order, rules):
        if idx == 0:
            return True
        page = order[idx]
        preceding_pages = order[:idx]
        for preceding_page in preceding_pages:
            # print(f"Checking {preceding_page} is satisfied for {page} | rules = {rules}")
            if page in rules and preceding_page in rules[page]:
                return False
        return True
    
    def check_right(idx, order, rules):
        if idx == len(order) - 1:
            return True
        page = order[idx]
        following_pages = order[idx+1:]
        for following_page in following_pages:
            if page in rules and following_page not in rules[page]:
                return False
        return True
    
    def check_print(order, rules):
        for idx in range(len(order)):
            if not check_left(idx, order,rules) or not check_right(idx, order, rules):
                return False
        return True
    
   
    middle_sum = 0
    input = arrange(input_str)
    for order in input['print_orders']:
        if check_print(order, input['rules']):
            middle_sum += int(findMiddle(order))

    return middle_sum

def solution_2(input_str):

    def fix_print(order, rules):
        for idx in range(len(order)):
            if not check_left(idx, order,rules) or not check_right(idx, order, rules):
                return False
        return True
    middle_sum = 0
    input = arrange(input_str)
    for order in input['print_orders']:
        if fix_print(order, input['rules']):
            middle_sum += int(findMiddle(order))

    return middle_sum


print(f"Day 5 Test 1: {solution_1(test_data)}")
print(f"Day 5 Part 1: {solution_1(input_str)}")

# Part 2
print(f"Day 5 Test 2: {solution_2(test_data)}")

print(f"Day 5 Part 2:")
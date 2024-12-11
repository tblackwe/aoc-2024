from utils.api import get_input, load_sample

input_str = get_input(11)
test_data = load_sample(11)

# WRITE YOUR SOLUTION HERE

# Part 1

def rule_1(stone):
    return '1' if stone == '0' else stone
def rule_2(stone):
    if len(stone) % 2 == 0:
        mid_index = len(stone) // 2
        first_stone = str(int(stone[:mid_index]))
        second_stone = str(int(stone[mid_index:]))
        return [first_stone, second_stone]
    else:
        return stone
def rule_3(stone):
    return str(int(stone) * 2024)

def blink(stones):
    updated_stones = []
    for stone in stones:
        updated_stone = rule_1(stone)
        if updated_stone != stone:
            updated_stones.append(updated_stone)
        else:
            updated_stone = rule_2(stone)
            if updated_stone != stone:
                updated_stones+= updated_stone
                # updated_stones.append(updated_stone[1])

            else:
                updated_stones.append(rule_3(stone))
    return updated_stones

def solution(input, blinks):
    stones = input.split(" ")
    for i in range(blinks):
        print(f"Blink {i+1}:")
        stones = blink(stones)
    return len(stones)

print(f"Day 11 Test 1: {solution(test_data, 25)}")
print(f"Day 11 Test 1: {solution(input_str, 25)}")

# Part 2

print(f"Day 11 Test 2: {solution(input_str, 75)}")
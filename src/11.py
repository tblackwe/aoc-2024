from utils.api import get_input, load_sample
from collections import defaultdict

input_str = get_input(11)
test_data = load_sample(11)

# WRITE YOUR SOLUTION HERE

# Part 1

def rule_1(stone):
    return 1 if stone == 0 else stone
def rule_2(stone):
    str_stone = str(stone)
    if len(str_stone) % 2 == 0:
        mid_index = len(str_stone) // 2
        first_stone = int(str_stone[:mid_index])
        second_stone = int(str_stone[mid_index:])
        return [first_stone, second_stone]
    else:
        return stone
def rule_3(stone):
    return int(stone) * 2024



def solution_1(input):
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

    stones = [int(x) for x in input.split(" ")]
    for _ in range(25):
        stones = blink(stones)
    return len(stones)

def solution_2(input):
    temp = [int(x) for x in input.split(" ")]
    stones = defaultdict(int)
    for stone in temp:
        stones[stone] += 1
    def blink(stones):
        updated_stones = defaultdict(int)
        for stone, count in stones.items():
            updated_stone = rule_1(stone)
            if updated_stone != stone:
                updated_stones[updated_stone] += count
            else:
                updated_stone = rule_2(stone)
                if updated_stone != stone:
                    updated_stones[updated_stone[0]] += count
                    updated_stones[updated_stone[1]] += count
                else:
                    updated_stones[rule_3(stone)] += count
        return updated_stones
    
    for _ in range(75):
        stones = blink(stones)
    return sum(stones.values())


print(f"Day 11 Test 1: {solution_1(test_data)}")
print(f"Day 11 Test 1: {solution_1(input_str)}")

# Part 2

print(f"Day 11 Test 2: {solution_2(input_str)}")
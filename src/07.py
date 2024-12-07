from utils.api import get_input, load_sample
import itertools


input_str = get_input(7)
test_data = load_sample(7)

# WRITE YOUR SOLUTION HERE


class Calibration:
    def __init__(self, line):
        temp = line.split(': ')
        self.result = int(temp[0])
        self.values = [int(x) for x in temp[1].split(" ")]

    def valid(self, isPart2):
        if isPart2:
            operations = ['+', '*', '||']
        else:
            operations = ['+', '*']
        combination_length = len(self.values)-1
        combinations = list(itertools.product(
            operations, repeat=combination_length))
        for combination in combinations:
            result = self.values[0]
            for idx, operator in enumerate(combination):
                match operator:
                    case '+':
                        result += self.values[idx+1]
                    case '*':
                        result *= self.values[idx+1]
                    case '||':
                        result = int(str(result)+str(self.values[idx+1]))

            if result == self.result:
                return True
        return False


def arrange_input(input):
    input_lines = input.splitlines()
    calibrations = []
    for line in input_lines:
        calibrations.append(Calibration(line))
    return calibrations


def solution(input, isPart2):
    calibrations = arrange_input(input)
    result = 0
    for calibration in calibrations:
        if calibration.valid(isPart2):
            result += calibration.result
    return result

# Part 1

print(f"Day 7 Test 1: {solution(test_data, isPart2=False)}")
print(f"Day 7 Part 1: {solution(input_str, isPart2=False)}")

# Part 2

print(f"Day 7 Test 2: {solution(test_data, isPart2=True)}")
print(f"Day 7 Part 2: {solution(input_str, isPart2=True)}")

from utils.api import get_input, load_sample
import numpy as np

input_str = get_input(6)
test_data = load_sample(6)

# WRITE YOUR SOLUTION HERE


def arrange(input):
    # Arrange matrix
    input_rows = input.splitlines()
    temp = []
    for row in input_rows:
        temp.append(list(row))
    return np.array(temp)


class Guard:
    def __init__(self):
        self.direction = [-1, 0]  # up

    def turn(self):
        match self.direction:
            case [-1, 0]:
                self.direction = [0, 1]  # was up, now right
            case [0, 1]:
                self.direction = [1, 0]  # was right, now down
            case [1, 0]:
                self.direction = [0, -1]  # was down, now left
            case [0, -1]:
                self.direction = [-1, 0]  # was left, now up


def p1_solution(input):
    matrix = arrange(input)
    guard_location = np.argwhere(matrix == '^')[0]
    visited_locations = set()
    
    guard = Guard()
    on_grid = True
    while on_grid:
        lookahead = guard_location + guard.direction
        if lookahead[0] < 0 or lookahead[0] >= matrix.shape[0] or lookahead[1] < 0 or lookahead[1] >= matrix.shape[1]:
            visited_locations.add(guard_location.tobytes())
            break
        if matrix[lookahead[0], lookahead[1]] == '#':
            guard.turn()
        else: 
            visited_locations.add(guard_location.tobytes())
            guard_location = lookahead
    return len(visited_locations)


def p2_solution(input):
    matrix = arrange(input)
    guard_location = np.argwhere(matrix == '^')
    print(guard_location)

# Part 1


print(f"Day 6 Part 1 Test:{p1_solution(test_data)}")
print(f"Day 6 Part 1:{p1_solution(input_str)}")

# Part 2

print(f"Day 6 Part 1 Test:{p2_solution(test_data)}")
print(f"Day 6 Part 2:{p2_solution(input_str)}")

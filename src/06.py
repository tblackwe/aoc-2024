from utils.api import get_input, load_sample
import numpy as np
from datetime import datetime

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

class Coord:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return str(self.x) + ',' + str(self.y)
    def __hash__(self):
        return hash(str(self))
    def __eq__(self,other):
        return self.x == other.x and self.y== other.y


def p1_solution(input):
    matrix = arrange(input)
    guard_location = np.argwhere(matrix == '^')[0]
    visited_locations = set()
    
    guard = Guard()
    on_grid = True
    while on_grid:
        lookahead = guard_location + guard.direction
        if lookahead[0] < 0 or lookahead[0] >= matrix.shape[0] or lookahead[1] < 0 or lookahead[1] >= matrix.shape[1]:
            visited_locations.add(Coord(guard_location[0],guard_location[1]))
            break
        if matrix[lookahead[0], lookahead[1]] == '#':
            guard.turn()
        else: 
            visited_locations.add(Coord(guard_location[0],guard_location[1]))
            guard_location = lookahead
    return visited_locations



def p2_solution(input):

    def create_candidates(matrix,visited_locations):
        candidates = []
        for location in visited_locations:
                duplicate_matrix = matrix.copy()
                if (duplicate_matrix[location.x,location.y] == '.'):
                    duplicate_matrix[location.x,location.y] = '#'
                    candidates.append(duplicate_matrix)
        return candidates

    def check_candidate(matrix):
        guard_location = np.argwhere(matrix == '^')[0]
        visited_locations = set()
        
        guard = Guard()
        infinite_loop = False
        while True:
            lookahead = guard_location + guard.direction
            if lookahead[0] < 0 or lookahead[0] >= matrix.shape[0] or lookahead[1] < 0 or lookahead[1] >= matrix.shape[1]:
                break
            if matrix[lookahead[0], lookahead[1]] == '#':
                guard.turn()
            else: 
                location_with_direction = np.array2string(guard_location) + ''.join(str(x) for x in guard.direction)
                if location_with_direction in visited_locations:
                    infinite_loop = True
                    break
                visited_locations.add(location_with_direction)
                guard_location = lookahead
        return infinite_loop

    matrix = arrange(input)
    visited_locations = p1_solution(input)
    candidates = create_candidates(matrix,visited_locations)
    print(f"Candidates: {len(candidates)}")
    valid_candidate_count = 0
    for idx,candidate in enumerate(candidates):
        if check_candidate(candidate): valid_candidate_count += 1
    return valid_candidate_count
    

# Part 1


print(f"Day 6 Test 1:\t{len(p1_solution(test_data))}")
print(f"Day 6 Part 1:\t{len(p1_solution(input_str))}")

# Part 2

print(f"Day 6 Test 2:\t{p2_solution(test_data)}")
print(f"Day 6 Part 2:\t{p2_solution(input_str)}")
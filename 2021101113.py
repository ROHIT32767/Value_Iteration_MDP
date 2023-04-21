# Implementing Value Iteration for MDP
import numpy as np
grid = [
    [0, 1, -1],
    [0, 0, 0],
    [0, 'wall', 0],
    [0, 0, 0]
]
gamma = 0.95
theta = 0.0001
actions = ['up', 'down', 'left', 'right']
step_cost = -0.040
prob_correct = 0.700
prob_wrong = 0.150
rows = len(grid)
cols = len(grid[0])
current_grid = [
    [0.000, 1.000, -1.000],
    [0.000, 0.000, 0.000],
    [0.000, 0.000, 0.000],
    [0.000, 0.000, 0.000]
]
# global iterations
iterations = 0

import numpy as np

def print_grid(current_grid):
    grid_str = []
    for row in current_grid:
        row_str = []
        for num in row:
            rounded_num = round(num, 4)
            num_str = str(rounded_num)
            row_str.append(num_str)
        grid_str.append(row_str)
    # print the array of strings
    print(grid_str)
    for row in grid_str:
       print('|' + '|'.join(row) + '|')


def get_policy_string(grid, grid2):
    actions = ['↑', '↓', '←', '→']
    policy = ''
    rows, cols = len(grid), len(grid[0])
    current_grid = [[0]*cols for i in range(rows)]
    for row in range(rows):
        for col in range(cols):
            cell = grid[row][col]
            if grid2[row][col] == 'wall':
                current_grid[row][col] = ' W '
            elif cell == 1:
                current_grid[row][col] = ' R ' 
            elif cell == -1:
                current_grid[row][col] = ' P '
            else:
                max_value = float('-inf')
                for action in actions:
                    if action == '↑':
                        if grid[max(row - 1, 0)][col] > max_value:
                            max_value = grid[max(row - 1, 0)][col]
                            current_grid[row][col] = ' ↑ '
                    elif action == '↓':
                        if grid[min(row + 1, rows - 1)][col] > max_value:
                            max_value = grid[min(row + 1, rows - 1)][col]
                            current_grid[row][col] = ' ↓ '
                    elif action == '←':
                        if grid[row][max(col - 1, 0)] > max_value:
                            max_value = grid[row][max(col - 1, 0)]
                            current_grid[row][col] = ' ← '
                    elif action == '→':
                        if grid[row][min(col + 1, cols - 1)] > max_value:
                            max_value = grid[row][min(col + 1, cols - 1)]
                            current_grid[row][col] = ' → '
    return current_grid

def print_grid(grid):
    print('+' + '---+' * len(grid[0]))
    for row in grid:
        print('|' + '|'.join(row) + '|')
        print('+' + '---+' * len(grid[0]))


while True:
    prev_grid = current_grid.copy()
    current_grid = [[0]*cols for i in range(rows)]
    max_diff = 0
    for i in range(rows):
        for j in range(cols):
            # print(i,j)
            if grid[i][j] == 'wall':
                # Agent stays in the same cell if it moves onto a wall
                current_grid[i][j] = 0
                continue
            if grid[i][j] == 1:
                # Agent stays in the same cell if it moves onto a wall
                current_grid[i][j] = 1
                continue
            if grid[i][j] == -1:
                # Agent stays in the same cell if it moves onto a wall
                current_grid[i][j] = -1
                continue
            max_value = float('-inf')
            for action in actions:
                if action == 'up':
                    # Check if the agent hits the upper boundary
                    next_i = max(i - 1, 0)
                    if grid[next_i][j] == 'wall':
                        next_i = i  # Agent stays in the same cell if it moves onto a wall
                    # print(prob_correct,prev_grid[next_i][j],prob_correct*prev_grid[next_i][j])
                    value = prob_correct * prev_grid[next_i][j]
                    # Check if the agent hits the left boundary
                    next_j = max(j - 1, 0)
                    if grid[i][next_j] == 'wall':
                        next_j = j
                    value += prob_wrong * prev_grid[i][next_j]
                    # Check if the agent hits the right boundary
                    next_j = min(j + 1, cols-1)
                    if grid[i][next_j] == 'wall':
                        next_j = j
                    value += prob_wrong * prev_grid[i][next_j]
                elif action == 'down':
                    # Check if the agent hits the lower boundary
                    next_i = min(i + 1, rows-1)
                    if grid[next_i][j] == 'wall':
                        next_i = i  # Agent stays in the same cell if it moves onto a wall
                    value = prob_correct * prev_grid[next_i][j]
                    # Check if the agent hits the left boundary
                    next_j = max(j - 1, 0)
                    if grid[i][next_j] == 'wall':
                        next_j = j
                    value += prob_wrong * prev_grid[i][next_j]
                    # Check if the agent hits the right boundary
                    next_j = min(j + 1, cols-1)
                    if grid[i][next_j] == 'wall':
                        next_j = j
                    value += prob_wrong * prev_grid[i][next_j]
                elif action == 'left':
                    # Check if the agent hits the left boundary
                    next_j = max(j - 1, 0)
                    if grid[i][next_j] == 'wall':
                        next_j = j  # Agent stays in the same cell if it moves onto a wall
                    value = prob_correct * prev_grid[i][next_j]
                    # Check if the agent hits the upper boundary
                    next_i = max(i - 1, 0)
                    if grid[next_i][j] == 'wall':
                        next_i = i
                    value += prob_wrong * prev_grid[next_i][j]
                    # Check if the agent hits the lower boundary
                    next_i = min(i + 1, rows-1)
                    if grid[next_i][j] == 'wall':
                        next_i = i
                    value += prob_wrong * prev_grid[next_i][j]
                elif action == 'right':
                    # Check if the agent hits the right boundary
                    next_j = min(j + 1, cols-1)
                    if grid[i][next_j] == 'wall':
                        next_j = j  # Agent stays in the same cell if it moves onto a wall
                    value = prob_correct * prev_grid[i][next_j]
                    # Check if the agent hits the upper boundary
                    next_i = max(i - 1, 0)
                    if grid[next_i][j] == 'wall':
                        next_i = i
                    value += prob_wrong * prev_grid[next_i][j]
                    # Check if the agent hits the lower boundary
                    next_i = min(i + 1, rows-1)
                    if grid[next_i][j] == 'wall':
                        next_i = i
                    value += prob_wrong * prev_grid[next_i][j]
                if value > max_value:
                    max_value = value
            current_grid[i][j] = step_cost + gamma * max_value
            if abs((current_grid[i][j] - prev_grid[i][j])) > max_diff:  # Update max_diff
                max_diff = abs(current_grid[i][j] - prev_grid[i][j])
    iterations += 1
    # print(np.array(current_grid))
    print('Grid after Iteration -',iterations)
    print((np.array(current_grid)))
    print()
    # print_grid(get_policy_string(current_grid, grid))
    if max_diff < theta:  # Check if max_diff is less than theta
        break
    # print("next iteration")


# print("Number of iterations:", iterations)
# print("Optimal value function:")
# print((np.array(current_grid)))
print('Policy after Grid Converges')
print_grid(get_policy_string(current_grid, grid))


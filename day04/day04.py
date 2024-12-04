import requests
import re


def read_input():
    url = "https://adventofcode.com/2024/day/4/input"
    headers = {
        "cookie": "session=53616c7465645f5f63a856ba19e95367fa21132c7b88d7080837ed80307fc185733755862375aad5db6b377b1e6d65d5063eceaf76b33ac4a571295f8969ee78"
    }
    response = requests.get(url, headers=headers)
    return response.text

# create_grid for coordinates
def create_grid(input):
    input = input.split("\n")
    # split input into rows and columns and add those elements to 2d array

    for i in range(len(input)):
        input[i] = list(input[i])

    return input


def calc(input):
    sequences = re.findall(r'mul\(\d{1,3},\d{1,3}\)', input)
    sum = 0
    for sequence in sequences:
        digits = re.findall(r'\d{1,3}', sequence)
        mul = int(digits[0]) * int(digits[1])
        sum += mul
    return sum

dir_part1 = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
sequence_part1 = ['M', 'A', 'S']

def scan_dir(grid, row, col, dir):
    for i in range(3):
        (move_x, move_y) = dir
        row += move_x
        col += move_y
        if(row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row])):
            return False
        if(grid[row][col] != sequence_part1[i]):
            return False
            
    return True

def part1(grid):
    count = 0
    # go through grid and find all 'X' characters
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'X':
                #print(f'start from:{row}-{col}')
                for d in dir_part1:
                    if(scan_dir(grid, row, col, d)):
                        #print(f'found at:{row}-{col}')
                        count += 1

                
    return count

def scan_subgrid(subgrid):
    if(subgrid[1][1] != 'A'):
        return False
    if((subgrid[0][0] == 'M' and subgrid[2][2] == 'S') or (subgrid[0][0] == 'S' and subgrid[2][2] == 'M')):
        if((subgrid[0][2] == 'M' and subgrid[2][0] == 'S') or (subgrid[0][2] == 'S' and subgrid[2][0] == 'M')):
            return True
        
    return False

def part2(grid):
    count = 0
    for row in range(len(grid)-3):
        for col in range(len(grid[row])-2):
            # making 3x3 subgrids
            subgrid = []
            for i in range(3):
                subgrid.append(grid[row+i][col:col+3])

            if(scan_subgrid(subgrid)):
                #print(f'found at:{row}-{col}')
                count += 1      
    return count

input = read_input()
grid = create_grid(input)
print(part1(grid))
print(part2(grid))


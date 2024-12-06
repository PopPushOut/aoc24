import requests

def read_input():
    url = "https://adventofcode.com/2024/day/6/input"
    headers = {
        "cookie": "session=53616c7465645f5f63a856ba19e95367fa21132c7b88d7080837ed80307fc185733755862375aad5db6b377b1e6d65d5063eceaf76b33ac4a571295f8969ee78"
    }
    response = requests.get(url, headers=headers)
    return response.text

test_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


def create_grid(input):
    input = input.split("\n")
    # split input into rows and columns and add those elements to 2d array
    for i in range(len(input)):
        if(input[i] == ''):
            continue
        input[i] = list(input[i])
        # find if there is a '^' character in the row
        if '^' in input[i]:
            sx = input[i].index('^')
            sy = i

    return input, sx, sy

dir = [[0, -1], [1, 0], [0, 1], [-1, 0]] # N, E, S, W

def rotate_to_right(dir_index):
    if(dir_index == 3):
        return 0
    return dir_index + 1

def in_bounds(grid, x, y):
    return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)
 
def part1(grid, sx, sy, visited):
    dir_index = 0
    # go through grid and find all 'X' characters
    while in_bounds(grid, sx, sy):
        #print(f'x:{sx}, y:{sy} grid:{grid[sy]} dir:{dir[dir_index]}')
        if(grid[sy][sx] == '#'):
            #print(f'x:{sx}, y:{sy} grid:{grid[sy][sx]}')
            sx -= dir[dir_index][0]
            sy -= dir[dir_index][1]
            dir_index = rotate_to_right(dir_index)
        visited[sy][sx] = True
        
        sx += dir[dir_index][0]
        sy += dir[dir_index][1]
        
    return sum([sum([1 for i in row if i]) for row in visited])

def hit_obstacle_twice(grid, sx, sy):
    dir_index = 0
    # create data structure to keep track of keys
    hit_obstacle = {}
    # go through grid and find all 'X' characters
    while in_bounds(grid, sx, sy):
        if(grid[sy][sx] == '#' or grid[sy][sx] == 'O'):
            #print(f'x:{sx}, y:{sy} grid:{grid[sy][sx]} dir:{dir[dir_index]}')
            # add key to hit_obstacle of sx,sy,dir_index
            key = f'{sx},{sy},{dir_index}'
            if key in hit_obstacle:
                return True
            hit_obstacle[key] = True
            #print(f'x:{sx}, y:{sy} grid:{grid[sy][sx]}')
            sx -= dir[dir_index][0]
            sy -= dir[dir_index][1]
            dir_index = rotate_to_right(dir_index) 
        sx += dir[dir_index][0]
        sy += dir[dir_index][1]

    return False
def part2(grid, sx, sy, visited):
    sum = 0
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            if visited[i][j] and grid[i][j] != '^':
                #place obstacle
                grid[i][j] = 'O'
                #print(f'x:{j}, y:{i}')
                if(hit_obstacle_twice(grid, sx, sy)):
                    sum += 1
                #remove obstacle
                grid[i][j] = '.'
                #print(f'x:{j}, y:{i}')
    return sum
    
#add execution time in milliseconds with 3 decimal points

input = read_input()
#input = test_input
grid, sx, sy = create_grid(input)
print(f'sx:{sx} sy:{sy}')
grid.pop()
import time
start_time = time.time()
#print(f'grid rows:{len(grid)} cols:{len(grid[0])}')
visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
print(part1(grid, sx, sy, visited))
print("--- %.2f milliseconds ---" % ((time.time() - start_time) * 1000))
start_time = time.time()
print(part2(grid, sx, sy, visited))
print("--- %.2f milliseconds ---" % ((time.time() - start_time) * 1000))
# print(part2(grid))


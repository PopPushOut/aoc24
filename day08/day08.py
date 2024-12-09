import requests
import time

def read_input():
    url = "https://adventofcode.com/2024/day/8/input"
    headers = {
        "cookie": "session=53616c7465645f5f63a856ba19e95367fa21132c7b88d7080837ed80307fc185733755862375aad5db6b377b1e6d65d5063eceaf76b33ac4a571295f8969ee78"
    }
    response = requests.get(url, headers=headers)
    return response.text

test_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


def parse_input(input, output):
    for row, line in enumerate(input.strip().split("\n")):
        if not line:
            continue
        for col,c in enumerate(line):
            if c != '.':
                if(output.get(c) == None):
                    output[c] = [[row, col]]
                else:
                    output[c].append([row, col])
    return row, col

operations1 = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
}
operations2 = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
    '||': lambda x, y: int(str(x) + str(y)),
}
def calculate(numbers, result, operations):
    if(len(numbers) == 1):
        return numbers[0] == result
 
    for op in operations:
        temp = operations[op](numbers[0], numbers[1])

        if calculate([temp] + numbers[2:], result, operations):
            return True
    
    return False
def get_antinote1_location(frd, fcd, freq):
    if(frd < 0):
        r = freq[0] + abs(frd)
    elif(frd > 0):
        r = freq[0] - abs(frd)
    else:
        r = freq[0]

    if(fcd < 0):
        c = freq[1] + abs(fcd)
    elif(fcd > 0):
        c = freq[1] - abs(fcd)
    else:
        c = freq[1]
    return [r, c]
def get_antinote2_location(frd, fcd, freq):
    if(frd < 0):
        r = freq[0] - abs(frd)
    elif(frd > 0):
        r = freq[0] + abs(frd)
    else:
        r = freq[0]

    if(fcd < 0):
        c = freq[1] - abs(fcd)
    elif(fcd > 0):
        c = freq[1] + abs(fcd)
    else:
        c = freq[1]
    return [r, c]

def antinode_search(freq1, freq2, max_row_index, max_col_index, visited):
    frd, fcd = freq2[0] - freq1[0], freq2[1] - freq1[1]

    ant1 = get_antinote1_location(frd, fcd, freq1)
    while in_bounds(ant1, max_row_index, max_col_index):
        #print(f'ant1: {ant1}')
        if(visited.get(f'{ant1[0]}-{ant1[1]}') == None):
             visited[f'{ant1[0]}-{ant1[1]}'] = 1
        ant1 = get_antinote1_location(frd, fcd, ant1)

    ant2 = get_antinote1_location(frd, fcd, freq2)
    while in_bounds(ant2, max_row_index, max_col_index):
        #print(f'ant2: {ant2}')
        if(visited.get(f'{ant2[0]}-{ant2[1]}') == None):
             visited[f'{ant2[0]}-{ant2[1]}'] = 1
        ant2 = get_antinote2_location(frd, fcd, ant2)


    #print(f'visited: {len(visited)}')
    #print(f'antinode1: {antinode1} antinode2: {antinode2}')

    return len(visited)
def in_bounds(antinode, max_row_index, max_col_index):
    return antinode[0] >= 0 and antinode[0] <= max_row_index and antinode[1] >= 0 and antinode[1] <= max_col_index

def part1(frequencies, max_row_index, max_col_index):
    visited = {}
    for key in frequencies:
        freq = frequencies[key]
        for i in range(len(freq)):
            # loop again from i+1 to the end of the list
            for j in range(i+1, len(freq)):
                antinode_search(freq[i], freq[j], max_row_index, max_col_index, visited)

    return len(visited)


def part2(frequencies, max_row_index, max_col_index):
    visited = {}
    for key in frequencies:
        freq = frequencies[key]
        for i in range(len(freq)):
            # loop again from i+1 to the end of the list
            for j in range(i+1, len(freq)):
                antinode_search(freq[i], freq[j], max_row_index, max_col_index, visited)

    return len(visited)
    
#add execution time in milliseconds with 3 decimal points

input = read_input()
#input = test_input
frequencies = {}
total_rows, total_cols = parse_input(input, frequencies)
#print(total_rows, total_cols)
#print(frequencies)
start_time = time.time()
print(part1(frequencies, total_rows, total_cols))
print("--- %.2f milliseconds ---" % ((time.time() - start_time) * 1000))


start_time = time.time()
print(part2(frequencies, total_rows, total_cols))
print("--- %.2f milliseconds ---" % ((time.time() - start_time) * 1000))
# print(part2(grid))


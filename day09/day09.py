import requests
import time


def read_input():
    url = "https://adventofcode.com/2024/day/9/input"
    headers = {
        "cookie": "session=53616c7465645f5f63a856ba19e95367fa21132c7b88d7080837ed80307fc185733755862375aad5db6b377b1e6d65d5063eceaf76b33ac4a571295f8969ee78"
    }
    response = requests.get(url, headers=headers)
    return response.text

test_input = """2333133121414131402"""


def parse_input(input, output):
    starting_number = 0
    for line in input.strip().split("\n"):
        for i, char in enumerate(line):
            if i % 2 != 0:
                for x in range(int(char)):
                    output.append('.')

                #print(f'empty slots: {char}')
            else:
                for x in range(int(char)):
                    output.append(starting_number)
                #print(f'filled slots: {starting_number} x {int(char)}')
                starting_number += 1
                
    return output

def part1(memory):
    sum = 0
    # iterate backwards
    for i in range(len(memory) - 1, -1, -1):
        index = memory.index('.')
        if(index >= i):
            break
        if memory[i] == '.':
            continue
        else:
            memory[index] = memory[i]
            memory[i] = '.'

    for i in range(len(memory)):
        if memory[i] == '.':
            break
        sum += int(memory[i]) * i
    return sum


def part2(memory):
    sum = 0
    # create ordered dict with contigues fragments
    fragment_block = {}
    previous = -1
    idx = -1
    for i in range(len(memory)):
        if memory[i] == '.':
            if previous != '.':
                idx = i
                fragment_block[idx] = 1
            else:
                fragment_block[idx] += 1
        previous = memory[i]

    print(fragment_block)

    memory_blocks = {}
    previous = -1
    idx = 0
    for i in range(len(memory)):
        if memory[i] != '.':
            if previous == '.' or previous != memory[i]:
                idx = i
                memory_blocks[idx] = 1
            else:
                memory_blocks[idx] += 1
        previous = memory[i]
    print(memory_blocks)

    # iterate through object keys in reverse
    for memory_loc in reversed(memory_blocks):
        mem_block = memory_blocks[memory_loc]
        #print(f'location: {memory_loc} block_size: {mem_block}')
        # find where it fitys in fragment block
        for fragment_loc in fragment_block:
            f_block = fragment_block[fragment_loc]
            if memory_loc > fragment_loc and mem_block <= f_block:
                if(mem_block == f_block):
                    del fragment_block[fragment_loc]
                else:
                    fragment_block = {(fragment_loc + mem_block) if k == fragment_loc else k:v for k,v in fragment_block.items()}
                    fragment_block[(fragment_loc + mem_block)] = f_block - mem_block

                #print(f'fragment_loc: {fragment_loc} fragment_block: {fragment_block}')

                memory[fragment_loc:fragment_loc + mem_block] = [memory[memory_loc]] * mem_block
                # fill memory from memory_loc to memory_loc + memory_blocks[memory_loc] with '.'
                memory[memory_loc:memory_loc + mem_block] = ['.'] * mem_block
                
                break

    print(memory)
    for i in range(len(memory)):
        if memory[i] == '.':
            continue
        sum += int(memory[i]) * i
    return sum
    
#add execution time in milliseconds with 3 decimal points

input = read_input()
#input = test_input
memory = []
parse_input(input, memory)
print(memory)
start_time = time.time()
#print(part1(memory))
print("--- %.2f milliseconds ---" % ((time.time() - start_time) * 1000))
start_time = time.time()
print(part2(memory))
print("--- %.2f milliseconds ---" % ((time.time() - start_time) * 1000))
# print(part2(grid))


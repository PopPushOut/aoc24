import requests
import re


def read_input():
    url = "https://adventofcode.com/2024/day/5/input"
    headers = {
        "cookie": "session=53616c7465645f5f63a856ba19e95367fa21132c7b88d7080837ed80307fc185733755862375aad5db6b377b1e6d65d5063eceaf76b33ac4a571295f8969ee78"
    }
    response = requests.get(url, headers=headers)
    return response.text
test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def move_element(lst, current_index, target_index):
    # Remove the element at the current index
    element = lst.pop(current_index)
    # Insert the element at the target index
    lst.insert(target_index, element)

def validate_number(index, sequence, b_map, a_map):
    number = sequence[index]
    b_array = b_map.get(number) or []
    a_array = a_map.get(number) or []

    for j in range(index, 0, -1):
        if sequence[j] in b_array:
            return False
        
    # check elements after
    for j in range(index+1, len(sequence)):
        if sequence[j] in a_array:
            return False
    
    return True

def left(index, sequence, b_map, a_map):
    number = sequence[index]
    a_array = a_map.get(number) or []
    index_to_switch = -1
    for j in range(index+1, len(sequence)):
        if sequence[j] in a_array:
            index_to_switch = j
    
    if(index_to_switch != -1):
        move_element(sequence, index, index_to_switch)
        return False
    return True

def right(index, sequence, b_map, a_map):
    number = sequence[index]
    b_array = b_map.get(number) or []
    index_to_switch = -1
    for j in range(index, 0, -1):
        if sequence[j] in b_array:
            index_to_switch = j
    if(index_to_switch != -1):
        move_element(sequence, index, index_to_switch)
        return False
    return True

def parse_input(input, before_map, after_map, sequences):
    # read input until empty line
    input = input.split("\n")
    for i in input:
        if i == "":
            sequences = input[input.index(i)+1:]
            break
        before, after = i.split("|")
        if(after not in after_map):
            after_map[after] = [before]
        else:
            after_map[after].append(before)

        if(before not in before_map):
            before_map[before] = [after]
        else:   
            before_map[before].append(after)
    sequences.pop()

    return before_map, after_map, sequences

def part1(b_map, a_map, sequences):
    sum = 0
    for sequence in sequences:
        sequence = sequence.split(",")
        invalid = False
        for i in range(len(sequence)):
            if not validate_number(i, sequence, b_map, a_map):
                invalid = True
                break

        if not invalid:
            sum += int(sequence[len(sequence) // 2])

    return sum

def part2(b_map, a_map, sequences):
    sum = 0
    for sequence in sequences:
        sequence = sequence.split(",")
        invalid = False
        for i in range(len(sequence)-1, -1, -1):
            if not left(i, sequence, b_map, a_map):
                invalid = True
        for i in range(len(sequence)-1, -1, -1):
            if not right(i, sequence, b_map, a_map):
                invalid = True
        if invalid:
            sum += int(sequence[len(sequence) // 2])

    return sum
    

input = read_input()
#input = test_input

before_map, after_map, sequences = parse_input(input, {}, {}, [])

print(part1(before_map, after_map, sequences))
print(part2(before_map, after_map, sequences))
# print(part2(grid))


import requests
import time

def read_input():
    url = "https://adventofcode.com/2024/day/7/input"
    headers = {
        "cookie": "session=53616c7465645f5f63a856ba19e95367fa21132c7b88d7080837ed80307fc185733755862375aad5db6b377b1e6d65d5063eceaf76b33ac4a571295f8969ee78"
    }
    response = requests.get(url, headers=headers)
    return response.text

test_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


def parse_input(input, output):
    for line in input.strip().split("\n"):
        if not line:
            continue
        parts = line.replace(':', '').split()
        output.append([int(parts[0])] + list(map(int, parts[1:])))
    return output

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
def part1(equations):
    sum = 0
    for equation in equations:
        result = equation[0]
        numbers = equation[1:]
        if calculate(numbers, result, operations1):
            sum += result
    return sum


def part2(equations):
    sum = 0
    for equation in equations:
        result = equation[0]
        numbers = equation[1:]
        if calculate(numbers, result, operations2):
            sum += result
    return sum
    
#add execution time in milliseconds with 3 decimal points

input = read_input()
#input = test_input
equations = []
parse_input(input, equations)
#print(equations)
start_time = time.time()
print(part1(equations))
print("--- %.2f milliseconds ---" % ((time.time() - start_time) * 1000))
start_time = time.time()
print(part2(equations))
print("--- %.2f milliseconds ---" % ((time.time() - start_time) * 1000))
# print(part2(grid))


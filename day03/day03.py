import requests
import re

def read_input():
    url = "https://adventofcode.com/2024/day/3/input"
    headers = {
        "cookie": "session=53616c7465645f5f63a856ba19e95367fa21132c7b88d7080837ed80307fc185733755862375aad5db6b377b1e6d65d5063eceaf76b33ac4a571295f8969ee78"
    }
    response = requests.get(url, headers=headers)
    return response.text

def calc(input):
    sequences = re.findall(r'mul\(\d{1,3},\d{1,3}\)', input)
    sum = 0
    for sequence in sequences:
        digits = re.findall(r'\d{1,3}', sequence)
        mul = int(digits[0]) * int(digits[1])
        sum += mul
    return sum

def part1(input):
    return calc(input)

def part2(input):
    total = calc(input)
    sequencesToIgnore = re.findall(r"don't\(\).*?do\(\)", input, re.DOTALL)
    mul_to_ignore = 0
    for sequence in sequencesToIgnore:
        print("\033[1;32;40m" + sequence + "\033[m")
        mul_to_ignore += calc(sequence)
    return total - mul_to_ignore

input = read_input()
print(part1(input))
print(part2(input))

